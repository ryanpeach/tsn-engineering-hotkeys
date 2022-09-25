from tsn.io import StateController

def print_help():
    # TODO: print help
    print("help")

def main():
    STATE = StateController()
    while True:
        print("> ", end="")
        cmd = input()
        match cmd.split():

            # Basic commands
            case ["exit"]:
                break
            case ["help"]:
                print_help()
            case ["reset"]:
                STATE.reset()

            # Energy Coolant Commands
            case ["b", energy, coolant]:
                STATE.set_beams(energy, coolant)
            case ["t", energy, coolant]:
                STATE.set_torpedos(energy, coolant)
            case ["s", energy, coolant]:
                STATE.set_sensors(energy, coolant)
            case ["m", energy, coolant]:
                STATE.set_maneuver(energy, coolant)
            case ["i", energy, coolant]:
                STATE.set_impulse(energy, coolant)
            case ["w", energy, coolant]:
                STATE.set_warp(energy, coolant)
            case ["f", energy, coolant]:
                STATE.set_front_shields(energy, coolant)
            case ["r", energy, coolant]:
                STATE.set_rear_shields(energy, coolant)

            # Energy Commands
            case ["be", energy]:
                STATE.set_beams(energy, None)
            case ["te", energy]:
                STATE.set_torpedos(energy, None)
            case ["se", energy]:
                STATE.set_sensors(energy, None)
            case ["me", energy]:
                STATE.set_maneuver(energy, None)
            case ["ie", energy]:
                STATE.set_impulse(energy, None)
            case ["we", energy]:
                STATE.set_warp(energy, None)
            case ["fe", energy]:
                STATE.set_front_shields(energy, None)
            case ["re", energy]:
                STATE.set_rear_shields(energy, None)

            # Coolant commands
            case ["bc", coolant]:
                STATE.set_beams(None, coolant)
            case ["tc", coolant]:
                STATE.set_torpedos(None, coolant)
            case ["sc", coolant]:
                STATE.set_sensors(None, coolant)
            case ["mc", coolant]:
                STATE.set_maneuver(None, coolant)
            case ["ic", coolant]:
                STATE.set_impulse(None, coolant)
            case ["wc", coolant]:
                STATE.set_warp(None, coolant)
            case ["fc", coolant]:
                STATE.set_front_shields(None, coolant)
            case ["rc", coolant]:
                STATE.set_rear_shields(None, coolant)

            # Default
            case _:
                print("invalid command")
