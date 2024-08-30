import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtCore import Qt

from MainWindow_ui import Ui_MainWindow
from InfoWindow_ui import Ui_info_win
from ErrorWindow_ui import Ui_ErrorWindow
from ErrorInputWindow_ui import Ui_Error_input_Window


class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_info_win()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)


class ErrorWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)

        self.ui.button_error_ok.clicked.connect(self.close)


class ErrorInputWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Error_input_Window()
        self.ui.setupUi(self)

        self.ui.button_error_ok.clicked.connect(self.close)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Привязка кнопок к методам
        self.ui.button_info.clicked.connect(self.open_info_window)
        self.ui.button_start.clicked.connect(self.generate_graph)
        self.ui.button_reset.clicked.connect(self.restart_graph)
        self.ui.button_print.clicked.connect(self.print_graph)

        # Отключение кнопок до генерации графика
        self.ui.button_reset.setEnabled(False)
        self.ui.button_print.setEnabled(False)
        self.ui.button_excel.setEnabled(False)

        self.info_window = None
        self.error_window = None
        self.error_input_window = None
        self.pixmap = None

    def open_info_window(self):
        if self.info_window is None:
            self.info_window = InfoWindow()
        self.info_window.show()

    def open_error_window(self):
        if self.error_window is None:
            self.error_window = ErrorWindow()
        self.error_window.show()

    def open_error_input_window(self):
        if self.error_input_window is None:
            self.error_input_window = ErrorInputWindow()
        self.error_input_window.show()

    def generate_graph(self):
        try:
            # Получение данных из полей ввода
            t0 = float(self.ui.entry_t0.text().replace(',', '.'))  # начальный момент времени
            tk = float(self.ui.entry_tk.text().replace(',', '.'))  # конечный момент времени
            dt1 = float(self.ui.entry_dt1.text().replace(',', '.'))  # период расчетов (вывод значений)
            dt2 = float(self.ui.entry_dt2.text().replace(',', '.'))  # параметр дискретизации
            x0 = float(self.ui.entry_x0.text().replace(',', '.'))  # начальное положение груза
            v0 = float(self.ui.entry_v0.text().replace(',', '.'))  # начальная скорость
            w0 = float(self.ui.entry_w0.text().replace(',', '.'))  # собственная частота колебаний осциллятора
            y = float(self.ui.entry_y.text().replace(',', '.'))  # коэффициент трения

            # Проверка введенных данных на корректность
            if t0 >= tk or dt1 <= 0 or dt2 <= 0 or dt1 < dt2 or y < 0 or w0 <= 0:
                self.open_error_input_window()
                return

        except ValueError:
            self.open_error_window()
            return

        # Временные шаги
        t = np.arange(t0, tk, dt2)

        # Массивы для хранения значений скорости и положения
        x = np.zeros_like(t)
        v = np.zeros_like(t)

        # Начальные условия
        x[0] = x0
        v[0] = v0

        # Численное решение уравнения методом Эйлера
        for i in range(1, len(t)):
            v[i] = v[i - 1] + (-w0**2 * x[i] - y * v[i]) * dt2
            x[i] = x[i - 1] + v[i] * dt2

        # Создание графика
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor((1, 1, 1, 0))  # Устанавливаем прозрачный фон для холста
        ax.plot(t, x, label='x(t) - Положение')
        ax.set_title('Колебания линейного гармонического осциллятора с учётом трения')
        ax.set_xlabel('t - Время')
        ax.set_ylabel('x - Положение')
        ax.grid(True)
        ax.legend()

        # Проверка, существует ли директория "graph"
        if not os.path.exists("graph"):
            os.makedirs("graph")

        # Сохранение графика в файл с прозрачным фоном
        graph_path = "graph/oscillator_graph.png"
        plt.savefig(graph_path, transparent=True)

        # Создаем QPixmap из сохраненного файла
        self.pixmap = QPixmap(graph_path)

        # Масштабируем изображение, сохраняя пропорции
        scaled_pixmap = self.pixmap.scaled(self.ui.label_graph.width(), self.ui.label_graph.height(),
                                           Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Устанавливаем масштабированное изображение в QLabel
        self.ui.label_graph.setPixmap(scaled_pixmap)

        # Блокировка кнопки "Сгенерировать", разблокировка кнопок "Сброс", "Печать", "Excel"
        self.ui.button_reset.setEnabled(True)
        self.ui.button_print.setEnabled(True)
        self.ui.button_excel.setEnabled(True)
        self.ui.button_start.setEnabled(False)

    def restart_graph(self):
        # Очищение полей ввода
        self.ui.entry_t0.clear()
        self.ui.entry_tk.clear()
        self.ui.entry_dt1.clear()
        self.ui.entry_dt2.clear()
        self.ui.entry_x0.clear()
        self.ui.entry_v0.clear()
        self.ui.entry_w0.clear()
        self.ui.entry_y.clear()

        # Очищение лейбла с графиком
        self.ui.label_graph.clear()

        # Блокировка кнопок "Сброс", "Печать", "Excel", разблокировка кнопки "Сгенерировать"
        self.ui.button_reset.setEnabled(False)
        self.ui.button_print.setEnabled(False)
        self.ui.button_excel.setEnabled(False)
        self.ui.button_start.setEnabled(True)

        # Сброс pixmap для предотвращения случайной печати старого изображения
        self.pixmap = None

    def print_graph(self):
        # Проверяем, что pixmap был создан (график существует)
        if self.pixmap:
            # Создаем объект QPrinter для настройки параметров печати
            printer = QPrinter()

            # Открываем диалог печати с использованием QPrintDialog,
            # предоставляя ему объект QPrinter для отображения диалога
            dialog = QPrintDialog(printer, self)

            # Если пользователь подтверждает диалог печати
            if dialog.exec():
                # Создаем объект QPainter, который будет использоваться для рисования на принтере
                painter = QPainter(printer)

                # Получаем прямоугольник видимой области для рисования на принтере
                rect = painter.viewport()

                # Получаем размер pixmap, который будет напечатан
                size = self.pixmap.size()

                # Масштабируем размер pixmap так, чтобы он вписывался в область видимости принтера,
                # сохраняя пропорции изображения
                size.scale(rect.size(), Qt.KeepAspectRatio)

                # Устанавливаем видимую область для рисования на принтере
                painter.setViewport(rect.x(), rect.y(), size.width(), size.height())

                # Устанавливаем окно для рисования на pixmap
                painter.setWindow(self.pixmap.rect())

                # Рисуем pixmap в указанной области
                painter.drawPixmap(0, 0, self.pixmap)

                # Завершаем работу с QPainter
                painter.end()

    def excel(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
