import json
from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Callable, Iterator, List
from pathlib import Path
import pyautogui
from tsn.settings import load_settings


@dataclass
class EnergyCoolant:
    """Representing a rig's energy and coolant levels."""

    energy_percent: int = Field(100, gt=0, le=300)
    coolant_level: int = Field(0, ge=0, le=8)


@dataclass
class _Rigging:
    rigging: str
    description: str
    settings: List[EnergyCoolant]


@dataclass
class Rigging:
    rigging: str
    description: str
    beams: EnergyCoolant
    torpedoes: EnergyCoolant
    sensors: EnergyCoolant
    maneuver: EnergyCoolant
    impulse: EnergyCoolant
    warp: EnergyCoolant
    front_shields: EnergyCoolant
    rear_shields: EnergyCoolant

    def __init__(self, rigging: _Rigging):
        """
        Convert from the list format to named values.
        :param rigging: A _Rigging object.
        """
        self.rigging = rigging.rigging
        self.description = rigging.description
        self.beams = rigging.settings[0]
        self.torpedoes = rigging.settings[1]
        self.sensors = rigging.settings[2]
        self.maneuver = rigging.settings[3]
        self.impulse = rigging.settings[4]
        self.warp = rigging.settings[5]
        self.front_shields = rigging.settings[6]
        self.rear_shields = rigging.settings[7]

    def __iter__(self) -> Iterator[EnergyCoolant]:
        """
        Iterate over the rigging's settings.
        :return: An iterable of EnergyCoolant objects.
        """
        return iter(
            [
                self.beams,
                self.torpedoes,
                self.sensors,
                self.maneuver,
                self.impulse,
                self.warp,
                self.front_shields,
                self.rear_shields,
            ]
        )

    def __call__(
        self, error_callback: Callable[[str], None], return_to_vis: Callable[[], bool]
    ) -> None:
        """
        Set up the rigging.
        """

        # Load the settings (allows for dynamic reload)
        settings = load_settings()

        # Save the current mouse position for later
        currentMousePosition = pyautogui.position()

        # Activate the artemis window
        # Because we want to be multi platform,
        # we will do this by looking for the engineering button
        # and clicking it twice. The first time to activate the window,
        # the second time to focus the engineering console.
        engr = pyautogui.locateOnScreen(
            str(settings.ENGINEERING_BUTTON), confidence=0.5
        )
        if engr is None:
            error_callback("ERROR: Could not find engineering button!")
            return
        print(f"Found engineering button at {engr}. Clicking it.")
        pyautogui.click(engr, clicks=1)  # , interval=settings.PRESS_INTERVAL_SEC)

        # Restore the mouse position
        print("Restoring mouse position")
        pyautogui.moveTo(currentMousePosition)

        # Reset energy and coolant with a double click of the spacebar
        print("Pressing spacebar twice to reset energy and coolant")
        pyautogui.press("space", presses=2, interval=settings.PRESS_INTERVAL_SEC)

        # Assume we are starting with the cursor at the beams setting
        # and iterate over the rigging's settings
        for energycoolant in self:
            # Set the energy
            if energycoolant.energy_percent > 100:
                presses = (energycoolant.energy_percent - 100) // 30
                print("Pressing W {} times to increase energy".format(presses))
                pyautogui.press(
                    "W", presses=presses, interval=settings.PRESS_INTERVAL_SEC
                )
            elif energycoolant.energy_percent < 100:
                presses = -(100 - energycoolant.energy_percent) // 30
                print("Pressing S {} times to decrease energy".format(presses))
                pyautogui.press(
                    "S", presses=presses, interval=settings.PRESS_INTERVAL_SEC
                )

            # Set the coolant
            print(
                "Pressing E {} times to increase coolant".format(
                    energycoolant.coolant_level
                )
            )
            pyautogui.press(
                "E",
                presses=energycoolant.coolant_level,
                interval=settings.PRESS_INTERVAL_SEC,
            )

            # Move to the next setting
            print("Pressing D to move to the next setting")
            pyautogui.press("D")

        # If the settings are to return to the vis console, do so
        if return_to_vis():
            # Activate the artemis window
            # Because we want to be multi platform,
            # we will do this by looking for the vis button
            # and clicking it twice. The first time to activate the window,
            # the second time to focus the vis console.
            vis = pyautogui.locateOnScreen(str(settings.VIS_BUTTON), confidence=0.5)
            if vis is None:
                error_callback("ERROR: Could not find vis button!")
                return
            pyautogui.click(vis, clicks=2)

            # Restore the mouse position
            pyautogui.moveTo(currentMousePosition)


def get_rigging_list(path: Path) -> List[Rigging]:
    """
    Get a list of rigging settings from a file.
    :param path: The path to the rigging file.
    :return: A list of Rigging objects.
    """
    rigging_list = []
    with open(path, "r") as f:
        rigging_list = json.load(f)

    return [
        Rigging(
            _Rigging(
                rigging=rigging["rigging"],
                description=rigging["description"],
                settings=[EnergyCoolant(*s) for s in rigging["settings"]],
            )
        )
        for rigging in rigging_list
    ]
