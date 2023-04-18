from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from serde import Strict, serde
from serde.toml import from_toml


class ServerPaths(str, Enum):
    uploaded_images = "uploaded_images"


@dataclass
@serde(type_check=Strict)
class ServerInfo:
    host: str
    port: int


@dataclass
@serde(type_check=Strict)
class ClientInfo:
    server_url: str
    prediction_endpoint: str
    model: str

    def get_post_request_url(self) -> str:
        return self.server_url + self.prediction_endpoint + "?model=" + self.model


@dataclass
@serde
class Config:
    server_info: ServerInfo
    client_info: ClientInfo


def load_config(path: Path = Path("config.toml")) -> Config:
    with open(path) as f:
        return from_toml(Config, f.read())
