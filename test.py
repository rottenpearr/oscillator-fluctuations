from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример окна")
        self.setGeometry(100, 100, 1000, 800)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1000, 800)

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Первая горизонтальная компоновка
        h_layout1 = QHBoxLayout()
        label1 = QLabel("Лейбл 1", self)
        label2 = QLabel("Лейбл 2", self)
        h_layout1.addWidget(label1)
        h_layout1.addWidget(label2)

        # Вторая горизонтальная компоновка
        h_layout2 = QHBoxLayout()
        label3 = QLabel("Лейбл 3", self)
        label4 = QLabel("Лейбл 4", self)
        h_layout2.addWidget(label3)
        h_layout2.addWidget(label4)

        # Добавляем первую горизонтальную компоновку в основную вертикальную
        main_layout.addLayout(h_layout1)

        # Создаем и добавляем отступ между горизонтальными компоновками
        spacer = QSpacerItem(0, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)
        main_layout.addItem(spacer)

        # Добавляем вторую горизонтальную компоновку в основную вертикальную
        main_layout.addLayout(h_layout2)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
