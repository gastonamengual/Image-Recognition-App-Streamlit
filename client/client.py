import base64
import io

import requests
import streamlit as st
from PIL import ImageFile

USERNAME = "ezepiola"
TOKEN_URL = "http://localhost:8000/token"
API_URL = "http://localhost:8000/detect_objects"  # "https://image-recognition-app-fastapi.vercel.app/detect_objects"


def get_payload(
    image: ImageFile, filename: str, ai_model_interface: str
) -> dict[str, bytes]:
    buffer = io.BytesIO()
    image.save(buffer, format="jpeg")
    image_bytes = buffer.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "filename": filename,
        "image_bytes": image_base64,
        "ai_model_interface": ai_model_interface,
    }

    return payload


def get_token():
    try:
        response = requests.post(TOKEN_URL, json={"username": USERNAME})

        if response.ok:
            token = response.json().get("token")
            if token:
                st.session_state.token = token
                st.success("Token obtained!")
                return

        st.error(
            f"ERROR {response.status_code} - Token not obtained: {response.json()}"
        )
        st.stop()

    except Exception as ex:
        raise ValueError(f"Token request failed: {ex}")


def detect_objects(payload: dict[str, bytes]):
    if "token" not in st.session_state or not st.session_state.token:
        st.error("ERROR: No valid token available")

    headers = {
        "Authorization": f"Bearer {st.session_state.token}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        st.session_state.token = None
        if response.ok:
            return response

        st.error(
            f"ERROR {response.status_code} - Image could not be processed: {response.json()}"
        )
        st.stop()
    except Exception as e:
        st.error(f"ERROR: Request process failed: {e}")
        st.stop()
