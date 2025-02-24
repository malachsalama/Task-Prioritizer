# Task Prioritizer Integration

## Overview

Task Prioritizer is a FastAPI-based integration that detects overdue tasks from Jira and notifies team members automatically. This helps ensure that high-priority issues get the attention they need.

## Features

- Listens for Jira webhook events (`jira:issue_created`).
- Extracts task details (issue key, summary, priority, assignee).
- Filters and processes only high-priority tasks.
- Sends real-time notifications to a telex channel.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/malachsalama/Task-Prioritizer.git
cd Task-Prioritizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root and define:

```ini
TICK_URL=your_server_url/jira-webhook
SLACK_WEBHOOK_URL=telex-channel-url
```

### 4. Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Testing the Integration

### 1. Manually Trigger a Webhook Event

Send a test request to the webhook endpoint:

```bash
curl -X POST   https://task-prioritizer.onrender.com/api/v1/jira-webhook   -H 'Content-Type: application/json'   -d '{
  "webhookEvent": "jira:issue_created",
  "issue": {
    "key": "TEST-123",
    "fields": {
      "summary": "Test issue from Jira.",
      "priority": { "name": "High" },
      "assignee": { "displayName": "Malach Salama" }
    }
  },
  "webhookUrl": "https://task-prioritizer.onrender.com/api/v1/jira-webhook"
}'
```

### Expected Response

```
{
    "status": "success",
    "message": "Notification sent to Telex."
}
```

### 2. Verify Telex Notification

- If successful, a Slack message should appear in the configured channel.
- If it fails, an error message is sent instead.

## Contributing

Feel free to open an issue or submit a pull request if you have improvements!

## License

MIT License
