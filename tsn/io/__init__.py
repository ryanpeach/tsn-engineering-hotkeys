from dataclasses import dataclass
from typing import Optional
import pyautogui as gui
class StateController:
    

    def __init__(self):
        self.reset()

    def reset(self):
        self.beams = EnergyCoolant(0, 0)
        self.torpedoes = EnergyCoolant(0, 0)
        self.sensors = EnergyCoolant(0, 0)
        self.maneuver = EnergyCoolant(0, 0)
        self.impulse = EnergyCoolant(0, 0)
        self.warp = EnergyCoolant(0, 0)
        self.front_shields = EnergyCoolant(0, 0)
        self.rear_shields = EnergyCoolant(0, 0)

    def set_beams(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.beams.energy = energy
        if coolant is not None:
            self.beams.coolant = coolant

    def set_torpedos(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.torpedoes.energy = energy
        if coolant is not None:
            self.torpedoes.coolant = coolant

    def set_sensors(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.sensors.energy = energy
        if coolant is not None:
            self.sensors.coolant = coolant

    def set_maneuver(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.maneuver.energy = energy
        if coolant is not None:
            self.maneuver.coolant = coolant

    def set_impulse(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.impulse.energy = energy
        if coolant is not None:
            self.impulse.coolant = coolant

    def set_warp(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.warp.energy = energy
        if coolant is not None:
            self.warp.coolant = coolant

    def set_front_shields(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.front_shields.energy = energy
        if coolant is not None:
            self.front_shields.coolant = coolant

    def set_rear_shields(self, energy: Optional[int] = None, coolant: Optional[int] = None) -> None:
        if energy is not None:
            self.rear_shields.energy = energy
        if coolant is not None:
            self.rear_shields.coolant = coolant
