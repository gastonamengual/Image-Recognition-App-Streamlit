from dataclasses import dataclass

import requests
import streamlit as st

from client.model import ImagePayload

from .utils import stop_execution


@dataclass
class API_Connector:
    username: str
    base_url: str

    @property
    def token_url(self):
        return f"{self.base_url}/token"

    @property
    def api_url(self):
        return f"{self.base_url}/detect_objects"

    def authenticate(self):
        try:
            response = requests.post(self.token_url, json={"username": self.username})
            if not response.ok:
                stop_execution(
                    f"ERROR {response.status_code} - Token not obtained: {response.json()}"
                )
            return response
        except Exception as ex:
            raise ValueError(f"Token request failed: {ex}")

    def detect_objects(self, image_payload: ImagePayload):

        headers = {
            "Authorization": f"Bearer {st.session_state.token}",
            "Content-Type": "application/json",
        }
        payload = image_payload.__dict__

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            return response
        except Exception as e:
            stop_execution(f"ERROR: Request process failed: {e}")
