from io import BufferedReader

import requests
from requests import Response
from streamlit.runtime.uploaded_file_manager import UploadedFile


def get_server_response(
    url: str, image_file: BufferedReader | UploadedFile, *, verbose: bool = True
) -> Response:
    file = {"file": image_file}
    response = requests.post(url, files=file)

    if verbose:
        if response.status_code == 200:
            msg = "Everything went well"
        else:
            msg = "There was an error when handling the request."
        print(msg)

    return response
