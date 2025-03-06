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
    VERCEL = "Vercel"
    RENDER_DOCKER = "Render + Docker"


backend_service_urls = {
    BackendService.RENDER_DOCKER.value: Settings.RENDER_DOCKER_BASE_URL,
    BackendService.VERCEL.value: Settings.VERCEL_BASE_URL,
}
