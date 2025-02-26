import streamlit as st
from PIL import Image

from client.client import detect_objects, get_payload, get_token

st.title("Image Recognition App")
st.header("By Gastón Amengual")


placeholder = st.empty()

uploaded_image = st.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False
)
filename = uploaded_image.name

if uploaded_image is not None:

    image = Image.open(uploaded_image)
    placeholder.image(image, use_container_width=True)
    payload = get_payload(image, filename)

    if st.button("Detect objects!"):
        get_token()
        response = detect_objects(payload)
        st.header("Objects detected!")
        placeholder.empty()
        st.image(response.content, use_container_width=True)
