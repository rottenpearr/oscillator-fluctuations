import sys
from PySide6 import QtCore, QtWidgets, QtGui
from settings import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Заголовок окна и иконка
        self.setWindowTitle("Моделирование колебаний линейного гармонического осциллятора")
        # self.setWindowIcon(icon)

        # Размеры окна
        self.resize(1000, 800)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1000, 800)

        # Стиль окна
        self.setStyleSheet(global_bg)

        # Флаги для окна
        # Окно всегда поверх других
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # Заголовок для ввода данных
        self.data_input = QtWidgets.QLabel("Ввод данных")
        self.data_input.setFont(title_font)
        self.data_input.setStyleSheet(color_font)
        self.data_input.setAlignment(QtCore.Qt.AlignLeft)
        self.data_input.setContentsMargins(0, 0, 0, 0)

        # Переменные для ввода
        variables = ["t<sub>0</sub>", "t<sub>k</sub>", "dt<sub>1</sub>", "dt<sub>2</sub>",
                     "x<sub>0</sub>", "v<sub>0</sub>", "w<sub>0</sub>", "y<sub>0</sub>"]
        self.labels = []
        for var in variables:
            label = QtWidgets.QLabel(var)
            label.setFont(title_font)
            label.setStyleSheet(color_font)
            label.setAlignment(QtCore.Qt.AlignLeft)
            label.setContentsMargins(0, 0, 0, 0)
            self.labels.append(label)

        # Создание центрального виджета
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Создание основной компоновки
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        main_layout.addWidget(self.data_input)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Отступы для main_layout

        # Создание компоновки для элементов вводимых данных
        layout_data = QtWidgets.QVBoxLayout()
        main_layout.addLayout(layout_data)

        for label in self.labels:
            layout_data.addWidget(label)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
