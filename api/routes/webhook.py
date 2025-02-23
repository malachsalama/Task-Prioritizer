from fastapi import APIRouter, Request
import httpx
import logging
from core.config import settings

router = APIRouter()

logging.basicConfig(level=logging.INFO)

@router.post("/jira-webhook")
async def jira_webhook(request: Request):
    try:
        payload = await request.json()
        logging.info(f"Received Jira webhook: {payload}")

        # Ensure it's an "issue_created" event
        if payload.get("webhookEvent") != "jira:issue_created":
            return {"status": "ignored", "message": "Not an issue_created event"}

        # Extract issue details
        issue = payload.get("issue", {})
        issue_key = issue.get("key", "Unknown")
        issue_summary = issue.get("fields", {}).get("summary", "No summary")
        issue_priority = issue.get("fields", {}).get("priority", {}).get("name", "Unknown")
        assignee = issue.get("fields", {}).get("assignee", {}).get("displayName", "Unassigned")

        # Only notify for high-priority issues
        if issue_priority.lower() not in ["high", "urgent", "critical"]:
            return {"status": "ignored", "message": "Issue priority is not high"}

        # Format notification message
        message = (
            f"🚨 *High-Priority Task Created!*\n"
            f"*Task:* `{issue_key}` - {issue_summary}\n"
            f"*Priority:* {issue_priority}\n"
            f"*Assignee:* {assignee}"
        )

        # Send notification to Telex
        telex_webhook_url = settings.TELEX_WEBHOOK_URL
        async with httpx.AsyncClient() as client:
            response = await client.post(telex_webhook_url, json={"text": message})
            response.raise_for_status()

        logging.info("High-priority notification sent to Telex successfully!")
        return {"status": "success", "message": "Notification sent to Telex."}

    except Exception as e:
        logging.error(f"Error processing Jira webhook: {str(e)}")
        return {"status": "error", "message": str(e)}
