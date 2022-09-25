from tsn.riglist import get_rigging_list
from pathlib import Path

def test_get_rigging_list():
    get_rigging_list(Path("./tsn/tests/data/rig_list_example.json"))