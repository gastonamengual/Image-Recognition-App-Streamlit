from dataclasses import dataclass
from enum import StrEnum

from app.settings import Settings


@dataclass
class ImagePayload:
    filename: str
    image_bytes: bytes
    model_service: str


@dataclass
class BackendService(StrEnum):
    RENDER_DOCKER = "Render + Docker"
    VERCEL = "Vercel"


backend_service_urls = {
    BackendService.RENDER_DOCKER.value: Settings.RENDER_DOCKER_BASE_URL,
    BackendService.VERCEL.value: Settings.VERCEL_BASE_URL,
}
