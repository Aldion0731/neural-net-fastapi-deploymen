import io
from pathlib import Path

import cv2
import numpy as np


def convert_bytes_to_image_array(img_bytes: bytes) -> np.ndarray:
    image_stream = io.BytesIO(img_bytes)
    image_stream.seek(0)

    bytes_array = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    return cv2.imdecode(bytes_array, cv2.IMREAD_COLOR)


def load_image_as_bytes(img: Path) -> bytes:
    with open(img, "rb") as f:
        return f.read()
