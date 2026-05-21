from fastapi import APIRouter
from app.schemas.health import HealthResponse
from app.core.config import settings

router = APIRouter(prefix="/health",tags=["Health"])

@router.get("",response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status= "ok",
        version= settings.app_version,
        environment= settings.environment
        )