import base64
import io

import streamlit as st
from PIL import ImageFile


def preprocess_image(image: ImageFile) -> str:
    buffer = io.BytesIO()
    image.save(buffer, format="jpeg")
    image_bytes = buffer.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    return image_base64


def get_token() -> str:
    return st.session_state.token


def stop_execution(message: str):
    st.error(message)
    st.stop()
