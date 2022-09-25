import json
from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Iterable, List, Tuple
from pathlib import Path

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

    def __iter__(self) -> Iterable[EnergyCoolant]:
        """
        Iterate over the rigging's settings.
        :return: An iterable of EnergyCoolant objects.
        """
        return iter([self.beams, self.torpedoes, self.sensors, self.maneuver, self.impulse, self.warp, self.front_shields, self.rear_shields])

def get_rigging_list(path: Path) -> List[Rigging]:
    """
    Get a list of rigging settings from a file.
    :param path: The path to the rigging file.
    :return: A list of Rigging objects.
    """
    rigging_list = []
    with open(path, 'r') as f:
        rigging_list = json.load(f)
    return [Rigging(_Rigging(**rigging)) for rigging in rigging_list]