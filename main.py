import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from MainWindow_ui import Ui_MainWindow
from InfoWindow_ui import Ui_info_win
import matplotlib.pyplot as plt


class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Информация")
        self.ui = Ui_info_win()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_info.clicked.connect(self.open_info_window)

        self.info_window = None

        self.button_reset

    def open_info_window(self):
        if self.info_window is None:
            self.info_window = InfoWindow()
        self.info_window.show()


if __name__ == "__main__":
    app = QApplication()

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
