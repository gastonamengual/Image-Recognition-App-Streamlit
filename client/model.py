from dataclasses import dataclass


@dataclass
class ImagePayload:
    filename: str
    image_bytes: bytes
    model_service: str
