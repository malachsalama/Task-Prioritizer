from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-23",
      "updated_at": "2025-02-23"
    },
    "descriptions": {
      "app_name": "Task Prioritizer",
      "app_description": "A custom integration that automatically notifies slack team members of High priority tasks from jira",
      "app_logo": "https://iili.io/dmHVsZG.png",
      "app_url": "http://ec2-51-20-251-125.eu-north-1.compute.amazonaws.com",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "integration_category": "Monitoring & Logging",
    "key_features": [
      "auto alerts",
      "realtime updates"
    ],
    "author": "Malach Salama",
    "settings": [
      {
        "label": "slack channel",
        "type": "text",
        "required": True,
        "default": "high priority task"
      }
    ],
    "target_url": settings.TELEX_WEBHOOK_URL,
    "tick_url": settings.TICK_URL
  }
}
@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)