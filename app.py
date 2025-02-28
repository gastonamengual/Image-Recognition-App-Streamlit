import streamlit as st
from PIL import Image

from client.client import detect_objects, get_payload, get_token

st.title("Image Recognition App")
st.header("By Gastón Amengual")


placeholder = st.empty()

uploaded_image = st.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False
)

options = ["HuggingFace"]

model_service = st.selectbox("Choose an AI model interface:", options)


if uploaded_image is not None:

    filename = uploaded_image.name

    image = Image.open(uploaded_image)
    placeholder.image(image, use_container_width=True)
    payload = get_payload(image, filename, model_service)

    if st.button("Detect objects!"):
        get_token()
        response = detect_objects(payload)
        st.header("Objects detected!")
        placeholder.empty()
        st.image(response.content, use_container_width=True)
