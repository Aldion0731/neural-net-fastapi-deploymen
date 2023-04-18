import streamlit as st

from src.server_client_utils.client_funcs import get_server_response
from src.utils.configurations import Config, load_config
from src.utils.image_processing import convert_bytes_to_image_array


def run(config: Config) -> None:
    st.title("Object Detector")
    img = st.file_uploader("Upload an image file", type=[".png", ".jpg"])

    if img is None:
        return

    url = config.client_info.get_post_request_url()
    res = get_server_response(url, img)

    st.image(convert_bytes_to_image_array(res.content))


if __name__ == "__main__":
    run(load_config())
