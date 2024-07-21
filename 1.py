import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QSpacerItem,
                               QSizePolicy, QMainWindow)
from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui
from settings import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Заголовок окна и иконка
        self.setWindowTitle("Моделирование колебаний линейного гармонического осциллятора")
        # self.setWindowIcon(icon)

        # Размеры окна
        self.resize(1000, 800)

        # Стиль окна
        self.setStyleSheet(global_bg)

        # Флаги для окна (окно всегда поверх других)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # Создание центрального виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создание вертикальной левой компоновки (она зависит от центрального виджета)
        left_vertical_layout = QVBoxLayout(central_widget)

        # Создание компоновки для заголовка ввода данных
        data_label_layout = QVBoxLayout()

        # Создание компоновки для элементов ввода
        data_input_layout = QGridLayout()

        # Заголовок для ввода данных
        self.data_input = QLabel("Ввод данных")
        self.data_input.setFont(title_font)
        self.data_input.setStyleSheet(color_font)
        data_label_layout.addWidget(self.data_input, alignment=Qt.AlignTop)

        # Переменные для ввода
        variables_data = ["t<sub>0</sub>", "t<sub>k</sub>", "dt<sub>1</sub>", "dt<sub>2</sub>",
                          "x<sub>0</sub>", "v<sub>0</sub>", "w<sub>0</sub>", "y"]
        self.labels = []
        self.inputs = []

        for index, element in enumerate(variables_data):
            # Создание виджета для элемента
            label = QLabel(element)
            label.setFont(title_font)
            label.setStyleSheet(color_font)
            self.labels.append(label)

            # Создание виджета для поля элемента
            input_field = QLineEdit()
            input_field.setFont(title_font)
            input_field.setStyleSheet(input_bg)
            self.inputs.append(input_field)

            data_input_layout.addWidget(label, index, 0)
            data_input_layout.addWidget(input_field, index, 1)

        # Создание спейсера для разграничивания компоновок в вертикальной левой компоновке
        spacer_1 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Добавление компоновок и спейсера в основную
        left_vertical_layout.addLayout(data_label_layout)
        left_vertical_layout.addItem(spacer_1)
        left_vertical_layout.addLayout(data_input_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
