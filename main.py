import streamlit as st
from PIL import Image
from numpy.typing import ArrayLike
import numpy as np

from app.models.model import Model, ModelConfig


ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


def validate_image_filename(image_filename: str):
    if image_filename is "":
        raise ValueError("No image Selected")


def validate_correct_extension(image_filename: str):
    if (
        not "." in image_filename
        and image_filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    ):
        raise ValueError("Wrong filename format")


def process_image(image_file: bytes) -> ArrayLike:
    processed_image = np.frombuffer(image_file, dtype=np.uint8)
    return processed_image


st.markdown("# Object Dection App")

image = st.file_uploader("Upload an image", accept_multiple_files=False)

if image is not None:
    bytes_data = image.read()
    image_filename: str = image.name

    validate_image_filename(image_filename)
    validate_correct_extension(image_filename)

    processed_image = process_image(bytes_data)


    model = Model(config=ModelConfig())
    img_bytes = model.detect_object(processed_image)

    image = Image.open(img_bytes)

    st.image(image, output_format="JPEG")
