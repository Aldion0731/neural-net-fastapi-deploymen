import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from src.models.models import Models
from src.utils.configurations import ServerPaths
from src.utils.image_processing import convert_bytes_to_image_array
from src.utils.validate_files import validate_upload_file

app = FastAPI(title="FastAPI Deployment")


@app.get("/")
def home() -> str:
    return "Server was successfully deployed. Check out http://localhost:8000/docs."


@app.post("/predict")
def prediction(model: Models, file: UploadFile = File(...)) -> StreamingResponse:
    validate_upload_file(file)

    image = convert_bytes_to_image_array(file.file.read())
    bbox, label, conf = cv.detect_common_objects(image, model=model)
    output_image = draw_bbox(image, bbox, label, conf)

    img_path = f"{ServerPaths.uploaded_images}/{file.filename}"
    cv2.imwrite(img_path, output_image)
    file_image = open(img_path, mode="rb")

    return StreamingResponse(file_image, media_type="image/jpeg")
