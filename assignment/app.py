from mongoengine import Document, StringField, DateTimeField
from flask import Flask, request, jsonify, render_template
from mongoengine import connect
from datetime import datetime,timedelta,timezone
import os

class git_hub_event(Document):
    action_type = StringField(required=True)
    author = StringField(required=True)
    from_branch = StringField()
    to_branch = StringField(required=True)
    timestamp = DateTimeField(required=True)
    meta={
        'collection':'githubrepo'
    }


app = Flask(__name__)
mongo_uri=os.getenv("MONGODB_URI")
connect(host=mongo_uri)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    author = data.get('pusher', {}).get('name') or data.get('sender', {}).get('login')
    utc_plus_530=timezone(timedelta(hours=5,minutes=30))
    timestamp = datetime.now(utc_plus_530)
    to_branch = data.get('ref', '').split('/')[-1] if data.get('ref') else None
    from_branch = data.get('pull_request', {}).get('head', {}).get('ref')
    to_branch_pr = data.get('pull_request', {}).get('base', {}).get('ref')

    event = git_hub_event(
        action_type=event_type.upper(),
        author=author,
        from_branch=from_branch if from_branch else None,
        to_branch=to_branch_pr if event_type == "pull_request" else to_branch,
        timestamp=timestamp
    )
    event.save()
    return jsonify({"status": "saved"}), 200

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/events')
def get_events():
    events = git_hub_event.objects.order_by('-timestamp')[:10]
    return jsonify([{
        "action_type": e.action_type,
        "author": e.author,
        "from_branch": e.from_branch,
        "to_branch": e.to_branch,
        "timestamp": e.timestamp.strftime("%d %B %Y - %I:%M %p")
    } for e in events])

if __name__ == '__main__':
    port=int(os.environ("PORT",4000))
    app.run(host="0.0.0.0",port=port)
