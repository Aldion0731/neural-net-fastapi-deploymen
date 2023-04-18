### YOLOv3 and YOLOv3-Tiny Object Detection via Streamlit

This project builds a web application that performs object detection using `YOLOv3` and `YOLOv3-Tiny` neural networks. It comprises of a server built with `FastAPI` and `uvicorn`, and a web application built with `Streamlit`. The web application allows users to upload an image and receive a labeled image with the names of the objects within the image, along with bounding boxes around them.
___
### Installation

##### Requirements

- `Python 3.10`
- `pipenv`

##### Clone Repository

Clone this repository to your local machine using:

```bash
git clone git@github.com:Aldion0731/neural-net-fastapi-deployment.git
```

##### Install Dependencies

```bash
pipenv sync
```

___

### Usage

##### Start Server

```bash
python -m src.scripts.server
```


##### Run the web application

```bash
python -m streamlit run src/scripts/client.py
```

##### Using `just`

```
just run-server
just run-client
# see Justfile for more details
```

##### Perform Object Detection
To perform object detection, follow these steps:

In the Streamlit app, click on the "Upload Image" button and select an image from your local machine.
Wait for the model to finish processing the image. Once completed, the labeled image will be displayed along with bounding boxes around the detected objects and their corresponding names.


##### Customization

Choosing YOLOv3 or YOLOv3-Tiny
By default, the web application uses the YOLOv3 neural network for object detection. If you would like to use the YOLOv3-Tiny network instead, set the model parameter in the "client_info" section of the config.toml file, to "yolov3-tiny"
