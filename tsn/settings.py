# Currently the only dimensions supported (because I use them)
from pydantic import Field
from typing import Tuple
from pydantic.dataclasses import dataclass
import json
from pathlib import Path


@dataclass
class Settings:
    WINDOW_DIMENSIONS: Tuple[int, int]
    PRESS_INTERVAL_SEC: float
    BUTTON_WIDTH: int
    IMAGE_DETECTION_CONFIDENCE: float = Field(..., gt=0.0, lt=1.0)

    def __post_init__(self):
        # Derivative settings
        self.ASSETS_PATH = Path(
            f"./assets/{self.WINDOW_DIMENSIONS[0]}x{self.WINDOW_DIMENSIONS[1]}"
        )
        self.ENGINEERING_BUTTON = self.ASSETS_PATH / "enginr.png"
        self.VIS_BUTTON = self.ASSETS_PATH / "vis.png"


def load_settings():
    """
    Load the settings from the settings file.
    :return: A dictionary of settings.
    """

    with open("settings.json", "r") as f:
        settings = json.load(f)

    # Here is where you specify your defaults and their overwrites
    return Settings(
        WINDOW_DIMENSIONS=settings.get("WINDOW_DIMENSIONS", (2048, 1536)),
        PRESS_INTERVAL_SEC=settings.get("PRESS_INTERVAL_SEC", 0.1),
        BUTTON_WIDTH=settings.get("BUTTON_WIDTH", 400),
        IMAGE_DETECTION_CONFIDENCE=settings.get("IMAGE_DETECTION_CONFIDENCE", 0.5),
    )
