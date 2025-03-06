import os
from app.utils import preprocess_image
from PIL import Image


def test_preprocess_image():
    current_dir = os.getcwd()
    sample_img_url = f"{current_dir}/computer.jpg"

    image = Image.open(sample_img_url)

    image_base64 = preprocess_image(image)
    assert image_base64 is not None
