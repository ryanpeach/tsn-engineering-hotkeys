# Currently the only dimensions supported (because I use them)
from typing import Tuple
from pydantic.dataclasses import dataclass
import json
from pathlib import Path

@dataclass
class Settings:
    WINDOW_DIMENSIONS: Tuple[int, int]
    PRESS_INTERVAL_SEC: float
    BUTTON_WIDTH: int = 400

    def __post_init__(self):
        # Derivative settings
        self.ASSETS_PATH = Path(f'./assets/{self.WINDOW_DIMENSIONS[0]}x{self.WINDOW_DIMENSIONS[1]}')
        self.ENGINEERING_BUTTON = self.ASSETS_PATH / 'enginr.png'
        self.VIS_BUTTON = self.ASSETS_PATH / 'vis.png'

def load_settings():
    """
    Load the settings from the settings file.
    :return: A dictionary of settings.
    """

    with open('settings.json', 'r') as f:
        settings = json.load(f)

    if "WINDOW_DIMENSIONS" in settings:
        WINDOW_DIMENSIONS = tuple(settings["WINDOW_DIMENSIONS"])
    else:
        WINDOW_DIMENSIONS = (2048, 1536)

    if "PRESS_INTERVAL_SEC" in settings:
        PRESS_INTERVAL_SEC = settings["PRESS_INTERVAL_SEC"]
    else:
        PRESS_INTERVAL_SEC = 0.1

    if "BUTTON_WIDTH" in settings:
        BUTTON_WIDTH = settings["BUTTON_WIDTH"]
    else:
        BUTTON_WIDTH = 400

    return Settings(WINDOW_DIMENSIONS=WINDOW_DIMENSIONS, PRESS_INTERVAL_SEC=PRESS_INTERVAL_SEC, BUTTON_WIDTH=BUTTON_WIDTH)