from dataclasses import asdict, dataclass

import requests  # type: ignore

from app.error import DetectionNotObtained, TokenNotObtainedError
from app.model import ImagePayload

from .utils import get_token


@dataclass
class API_Client:
    username: str
    base_url: str

    @property
    def token_url(self):
        return f"{self.base_url}/token"

    @property
    def api_url(self):
        return f"{self.base_url}/detect_objects"

    def authenticate(self) -> str:
        try:
            response = requests.post(self.token_url, json={"username": self.username})

            if not response.ok:
                raise TokenNotObtainedError(
                    f"ERROR {response.status_code} - Token was not obtained: {response.json()}"
                )
            token = response.json().get("token")

            return token

        except Exception as ex:
            raise TokenNotObtainedError(f"Token request failed: {ex}")

    def detect_objects(self, image_payload: ImagePayload) -> bytes:
        token = get_token()

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        payload = asdict(image_payload)

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)

            if not response.ok:
                raise DetectionNotObtained(
                    f"ERROR {response.status_code} - Image could not be processed: {response.json()}"
                )
            detected_image = response.content

            return detected_image

        except Exception as e:
            raise DetectionNotObtained(f"Detection request failed: {e}")
