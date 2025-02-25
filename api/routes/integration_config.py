from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-23",
      "updated_at": "2025-02-23"
    },
    "descriptions": {
      "app_name": "Task Prioritizer",
      "app_description": "A custom integration that automatically notifies Telex team members of High priority tasks from jira",
      "app_logo": "https://iili.io/dmHVsZG.png",
      "app_url": "https://task-prioritizer.onrender.com",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "output",
    "integration_category": "Project Management",
    "key_features": [
      "Auto alerts for high-priority Jira issues",
      "Seamless integration with Telex",
      "Realtime updates"
    ],
    "author": "Malach Salama",
    "settings": [
      {
        "label": "task-prioritizer",
        "type": "text",
        "required": True,
        "default": "High priority task"
      }
    ],
    "target_url": "https://ping.telex.im/v1/webhooks/01951eae-6cb0-720c-bfd5-0a345fae22fa",
  }
}
@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)