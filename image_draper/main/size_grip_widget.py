"""QWidget for containing the QSizeGrip.

This widget is used to contain the QSizeGrips and nothing else.

The wigdget must the exact same size and location as the transparent_image passed to it.

The widget itself uses the WA_TransparentForMouseEvents flag for when the user
hovers over the widget, except for the QSizeGrip, which is still able to be
clicked and dragged.

The QSizeGrips are used to allow the user to resize the window. The transparent_image
widget must also be resized when the QSizeGrips are moved.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QMainWindow, QSizeGrip, QWidget


class SizeGripWidget(QWidget):
    """Widget for containing the QSizeGrip."""

    def __init__(self, transparent_image: QMainWindow) -> None:
        """Initialise the widget."""
        super().__init__()

        self.transparent_image = transparent_image

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            grip.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
            self.grips.append(grip)

        self.resize_grips()

        # Set size and location to be the same as the transparent_image
        self.setGeometry(transparent_image.geometry())

    def resize_grips(self) -> None:
        """Resize the QSizeGrips."""
        for i, grip in enumerate(self.grips):
            if i == 0:
                grip.move(0, 0)
            elif i == 1:
                grip.move(self.width() - self.gripSize, 0)
            elif i == 2:
                grip.move(0, self.height() - self.gripSize)
            else:
                grip.move(self.width() - self.gripSize, self.height() - self.gripSize)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Handle the resize event."""
        QWidget.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

        # Now resize the transparent_image
        self.transparent_image.setGeometry(self.geometry())
