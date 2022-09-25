import sys
from tsn.riglist import get_rigging_list
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox
from tsn.settings import load_settings


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    settings = load_settings()

    # Load the rig list
    rig_list = get_rigging_list("rig_list.json")

    # Error callback
    errorLabel = QLabel(widget)
    errorLabel.setGeometry(10, 10, settings.BUTTON_WIDTH, 50)

    return_to_vis = QCheckBox(widget)
    return_to_vis.setText("Return to VIS on Completion")
    return_to_vis.setChecked(False)
    return_to_vis.move(50, 50)

    # Add a button for each item on the rig list
    y = 100
    dy = 50
    for rig in rig_list:
        button = QPushButton(widget)
        # Common mistakes:
        # https://stackoverflow.com/questions/40705063/pyqt-pushbutton-connect-creation-within-loop
        button.clicked.connect(
            lambda checked, _rig=rig: _rig(errorLabel.setText, return_to_vis.isChecked)
        )
        button.setText(rig.rigging)
        button.setStyleSheet("QPushButton { text-align: left; }")
        button.setGeometry(50, y, settings.BUTTON_WIDTH, 50)
        button.move(50, y)
        y += dy

    errorLabel.move(50, y)

    widget.setGeometry(50, 50, settings.BUTTON_WIDTH + 100, y + dy)
    widget.setWindowTitle("Engineering Presets")
    widget.show()
    sys.exit(app.exec_())
