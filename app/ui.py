import streamlit as st
from PIL import Image

from app.api_client import API_Client
from app.model import BackendService, ImagePayload, backend_service_urls
from app.utils import preprocess_image


def main():
    st.title("Image Recognition App")
    st.header("By Gastón Amengual")

    placeholder = st.empty()
    uploaded_image = st.file_uploader(
        "Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False
    )

    backend_service = st.selectbox(
        "Choose a Backend Service:",
        [option.value for option in BackendService],
    )
    backend_service_url = backend_service_urls[backend_service]

    model_service = st.selectbox("Choose an AI Model Registry", ["HuggingFace"])
    username = st.text_input("Enter your username")

    if uploaded_image is not None:
        filename = uploaded_image.name

        image = Image.open(uploaded_image)
        placeholder.image(image, use_container_width=True)
        preprocessed_image = preprocess_image(image)

        if st.button("Detect objects!"):
            api_connector = API_Client(username=username, base_url=backend_service_url)

            token = api_connector.authenticate()

            st.session_state.token = token
            st.success("User authenticated!")

            image_payload = ImagePayload(
                filename=filename,
                image_bytes=preprocessed_image,
                model_service=model_service,
            )
            detected_image = api_connector.detect_objects(image_payload)

            st.header("Objects detected!")
            placeholder.empty()
            st.image(detected_image, use_container_width=True)


if __name__ == "__main__":
    main()
