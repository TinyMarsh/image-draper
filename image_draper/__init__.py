"""Entry point for the Image Draper program.

Image Draper is a software for overlaying a transparent image on top of other windows.

Run the software with: python -m image_draper.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication


def run() -> None:
    """Main entry point to program."""
    from .main.main_window import MainWindow

    app = QApplication(sys.argv)

    hidden_main_window = MainWindow()
    hidden_main_window.setWindowFlag(Qt.WindowStaysOnTopHint)
    hidden_main_window.show()

    # app.aboutToQuit.connect(hidden_main_window.close)

    sys.exit(app.exec())
