# 🚀 GitHub Webhook Event Tracker

A Flask-based web application that listens to GitHub webhook events
(Push, Pull Request, Merge) and stores them in MongoDB. The application
displays the latest events in a clean UI that auto-refreshes every 15
seconds.

------------------------------------------------------------------------

## 📌 Features

-   Capture GitHub **Push** events
-   Capture **Pull Request** events
-   Detect and store **Merge** events
-   Store events in MongoDB using MongoEngine
-   Display latest 10 events in real-time
-   Auto-refresh frontend every 15 seconds
-   Clean and responsive UI

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Backend: Flask (Python)
-   Database: MongoDB
-   ODM: MongoEngine
-   Frontend: HTML, CSS, JavaScript
-   Webhook Provider: GitHub

------------------------------------------------------------------------

## 📂 Project Structure

project/ │ ├── app.py ├── templates/ │ └── index.html ├──
requirements.txt └── README.md

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/github-webhook-tracker.git cd
github-webhook-tracker

------------------------------------------------------------------------

### 2️⃣ Create Virtual Environment

python -m venv venv source venv/bin/activate (Mac/Linux)
venv`\Scripts`{=tex}`\activate      `{=tex}(Windows)

------------------------------------------------------------------------

### 3️⃣ Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

### 4️⃣ Set Environment Variables

Mac/Linux:

export MONGODB_URI="your_mongodb_connection_string" export PORT=4000

Windows:

set MONGODB_URI=your_mongodb_connection_string set PORT=4000

------------------------------------------------------------------------

### 5️⃣ Run the Application

python app.py

Application will run on:

http://localhost:4000

------------------------------------------------------------------------

## 🔔 Setting Up GitHub Webhook

1.  Go to your GitHub repository
2.  Click Settings → Webhooks
3.  Click Add Webhook
4.  Set:

Payload URL: http://your-domain.com/webhook

Content Type: application/json

Select Events: - Push - Pull requests

5.  Click Add Webhook

------------------------------------------------------------------------

## 📡 API Endpoints

POST /webhook\
Receives GitHub webhook payloads.

GET /events\
Returns latest 10 events in JSON format.

GET /\
Renders frontend dashboard.

------------------------------------------------------------------------

## 🧠 How It Works

-   GitHub sends event data to `/webhook`
-   Backend parses event type
-   Event is stored in MongoDB
-   Frontend fetches `/events` every 15 seconds
-   Latest events are displayed dynamically

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Webhook secret verification
-   Pagination
-   Real-time updates with WebSockets
-   Docker support
-   Cloud deployment
-   Event analytics dashboard

------------------------------------------------------------------------

## 👨‍💻 Author

Mohd Saad

------------------------------------------------------------------------

## 📄 License

This project is for educational and portfolio purposes.
