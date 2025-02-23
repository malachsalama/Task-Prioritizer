from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.integration_config import router as integration_router
from api.routes.webhook import router as webhook_router
from core.config import settings

app = FastAPI()

# Define the allowed origins
allowed_origins = [
    "https://telex.im",
    "https://staging.telex.im",
    "https://telextest.im",
    "https://staging.telextest.im"
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(integration_router, prefix=settings.API_PREFIX)
app.include_router(webhook_router, prefix=settings.API_PREFIX)

# Health check endpoint
@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}