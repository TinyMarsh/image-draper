"""Code for the main window containing all the frames and menus of the GUI."""

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow


class TransparentImage(QMainWindow):
    """Main window containing the image selection and visualisation."""

    def __init__(self) -> None:
        """Initialise the main window."""
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        image = QImage()
        image.load("test.jpg")
        image = image.convertToFormat(QImage.Format.Format_ARGB32)

        newImg = QImage(image.size(), QImage.Format.Format_ARGB32)
        newImg.fill(Qt.GlobalColor.transparent)

        painter = QPainter(newImg)
        painter.setOpacity(0.5)
        painter.drawImage(QRect(0, 0, image.width(), image.height()), image)
        painter.end()

        pixmap = QPixmap(newImg)
        pixmap = pixmap.scaledToHeight(300, Qt.TransformationMode.SmoothTransformation)

        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        self.setCentralWidget(label)
