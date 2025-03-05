import streamlit as st
from PIL import Image

from client.api_connector import API_Connector
from client.model import BackendService, ImagePayload, backend_service_urls
from client.utils import preprocess_image, stop_execution

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

        api_connector = API_Connector(username=username, base_url=backend_service_url)

        response = api_connector.authenticate()
        token = response.json().get("token")
        st.session_state.token = token
        st.success("User authenticated!")

        image_payload = ImagePayload(
            filename=filename,
            image_bytes=preprocessed_image,
            model_service=model_service,
        )
        response = api_connector.detect_objects(image_payload)
        if not response.ok:
            stop_execution(
                f"ERROR {response.status_code} - Image could not be processed: {response.json()}"
            )

        st.header("Objects detected!")
        placeholder.empty()
        st.image(response.content, use_container_width=True)
