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
                STATE.beam(energy, coolant)
            case ["t", energy, coolant]:
                STATE.torpedo(energy, coolant)
            case ["s", energy, coolant]:
                STATE.sensors(energy, coolant)
            case ["m", energy, coolant]:
                STATE.maneuver(energy, coolant)
            case ["i", energy, coolant]:
                STATE.impulse(energy, coolant)
            case ["w", energy, coolant]:
                STATE.warp(energy, coolant)
            case ["f", energy, coolant]:
                STATE.front_shields(energy, coolant)
            case ["r", energy, coolant]:
                STATE.rear_shields(energy, coolant)

            # Energy Commands
            case ["be", energy]:
                STATE.beam(energy, None)
            case ["te", energy]:
                STATE.torpedo(energy, None)
            case ["se", energy]:
                STATE.sensors(energy, None)
            case ["me", energy]:
                STATE.maneuver(energy, None)
            case ["ie", energy]:
                STATE.impulse(energy, None)
            case ["we", energy]:
                STATE.warp(energy, None)
            case ["fe", energy]:
                STATE.front_shields(energy, None)
            case ["re", energy]:
                STATE.rear_shields(energy, None)

            # Coolant commands
            case ["bc", coolant]:
                STATE.beam(None, coolant)
            case ["tc", coolant]:
                STATE.torpedo(None, coolant)
            case ["sc", coolant]:
                STATE.sensors(None, coolant)
            case ["mc", coolant]:
                STATE.maneuver(None, coolant)
            case ["ic", coolant]:
                STATE.impulse(None, coolant)
            case ["wc", coolant]:
                STATE.warp(None, coolant)
            case ["fc", coolant]:
                STATE.front_shields(None, coolant)
            case ["rc", coolant]:
                STATE.rear_shields(None, coolant)

            # Default
            case _:
                print("invalid command")
