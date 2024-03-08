"""Entry point for the Image Draper program.

Image Draper is a software for overlaying a transparent image on top of other windows.

Run the software with: python -m image_draper.
"""

import sys

from PySide6.QtWidgets import QApplication

from .main.size_grip_widget import SizeGripWidget
from .main.transparent_image import TransparentImage


def run() -> None:
    """Main entry point to program."""
    app = QApplication(sys.argv)

    transparent_image = TransparentImage()
    transparent_image.show()

    size_grip_widget = SizeGripWidget(transparent_image)
    size_grip_widget.show()

    app.exec()

    sys.exit()
