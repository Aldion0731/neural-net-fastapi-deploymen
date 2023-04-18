import os

from src.config.configurations import ServerPaths


def run() -> None:
    os.makedirs(ServerPaths.uploaded_images, exist_ok=True)


if __name__ == "__main__":
    run()
