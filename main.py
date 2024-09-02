import sys
import os
from math import ceil

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtCore import Qt

from MainWindow_ui import Ui_MainWindow
from InfoWindow_ui import Ui_info_win

from pathlib import Path


class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_info_win()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)


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
        self.ui.button_excel.clicked.connect(self.open_excel)
        self.ui.pushButton.clicked.connect(self.show_previous_graph)
        self.ui.pushButton_2.clicked.connect(self.show_next_graph)
        self.ui.button_upload.clicked.connect(self.upload_excel)

        # Отключение кнопок до генерации графика
        self.ui.button_reset.setEnabled(False)
        self.ui.button_reset.setEnabled(False)
        self.ui.button_print.setEnabled(False)
        self.ui.button_excel.setEnabled(False)

        # Кнопки стрелок до генерации графика невидимы
        self.ui.pushButton.setHidden(True)
        self.ui.pushButton_2.setHidden(True)

        # Привязываем изменения в каждом поле ввода к методу check_input_fields
        self.ui.entry_t0.textChanged.connect(self.check_input_fields)
        self.ui.entry_tk.textChanged.connect(self.check_input_fields)
        self.ui.entry_dt1.textChanged.connect(self.check_input_fields)
        self.ui.entry_dt2.textChanged.connect(self.check_input_fields)
        self.ui.entry_x0.textChanged.connect(self.check_input_fields)
        self.ui.entry_v0.textChanged.connect(self.check_input_fields)
        self.ui.entry_w0.textChanged.connect(self.check_input_fields)
        self.ui.entry_y.textChanged.connect(self.check_input_fields)

        self.info_window = None
        self.pixmap = None

        # Создание счётчика графиков для перелистывания
        self.graph_counter = 0
        self.graph_paths = []
        self.excel_paths = []

    def open_info_window(self):
        if self.info_window is None:
            self.info_window = InfoWindow()
        self.info_window.show()

    def check_input_fields(self):
        # Если хотя бы одно поле ввода не пустое, активируем кнопку
        if (self.ui.entry_t0.text() or self.ui.entry_tk.text() or self.ui.entry_dt1.text() or self.ui.entry_dt2.text()
                or self.ui.entry_x0.text() or self.ui.entry_v0.text() or self.ui.entry_w0.text()
                or self.ui.entry_y.text()):
            self.ui.button_reset.setEnabled(True)
        else:
            self.ui.button_reset.setEnabled(False)

    def error_incorrect_input_message(self, title, message):
        error_dialog = QMessageBox()
        icon = QPixmap(Path("images/error.svg"))
        error_dialog.setWindowIcon(icon)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec()

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
            if t0 >= tk or dt1 <= 0 or dt2 <= 0 or dt1 < dt2 or y < 0 or w0 < 0:
                self.error_incorrect_input_message("Ошибка ввода данных",
                                                   "Убедитесь, что введённые данные соответствуют"
                                                   " следующим условиям: "
                                                   "t0 < tk; "
                                                   "dt1 > 0; dt2 > 0; dt1 >= dt2; "
                                                   "γ >= 0; ω0 >= 0.")
                return

        except ValueError:
            self.error_incorrect_input_message("Ошибка ввода данных",
                                               "Убедитесь, что все поля заполнены корректно "
                                               "(введены только цифры"
                                               " и цифры через запятую или точку).")
            return

        N = ceil((tk - t0) / dt1)
        M = ceil(dt1 / dt2)

        # Временные шаги
        t = list(False for _ in range(0, N * M + 2, 1))

        # Массивы для хранения значений скорости и положения
        x = list(False for _ in range(0, N * M + 2, 1))
        v = list(False for _ in range(0, N * M + 2, 1))

        # Начальные условия
        x[0] = x0
        v[0] = v0
        t[0] = t0

        index = 1

        # for i in range(1, N):
        #     v[i] = v[i - 1] + (-w0 ** 2 * x[i - 1] - y * v[i - 1]) * dt2
        #     x[i] = x[i - 1] + v[i] * dt2

        # Численное решение уравнения методом Эйлера
        for i in range(1, N + 1):
            for k in range(1, M + 1):
                if t[index - 1] + dt2 > t0 + dt1 * i:
                    t[index] = t0 + dt1 * i
                else:
                    t[index] = t[index - 1] + dt2

                if t[index] > tk:
                    t[index] = tk
                v[index] = v[index - 1] + (-w0 ** 2 * x[index - 1] - y * v[index - 1]) * dt2
                x[index] = x[index - 1] + v[index - 1] * dt2

                if t[index] == tk:
                    break

                index += 1

        if tk not in t:  # ТУТ ИЛИ НИЖЕ ОШИБКА
            while t[-1] is False:
                del t[-1]
                del v[-1]
                del x[-1]
            t.append(tk)
            v.append(v[-1] + (-w0 ** 2 * x[-1] - y * v[-1]) * dt2)
            x.append(x[-1] + v[-1] * dt2)
        else:  # ДВАЖДЫ tk
            flag = True
            count = t.count(tk)
            while t[-1] != tk or flag:
                if t[-1] == tk:
                    count -= 1

                del t[-1]
                del v[-1]
                del x[-1]

        # Проверка, существует ли директория "graph"
        if not os.path.exists("graph"):
            os.makedirs("graph")

        # Создание графика xvt
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        fig1.patch.set_facecolor((1, 1, 1, 0))  # Устанавливаем прозрачный фон для холста

        # Построение графика x(t) - синяя линия
        ax1.plot(t, x, label="x(t) - Положение", color="blue")

        # Построение графика v(t) - розовая линия
        ax1.plot(t, v, label="v(t) - Скорость", color="pink")

        # Установка заголовка и меток осей
        ax1.set_title("Колебания линейного гармонического осциллятора с учётом трения")
        ax1.set_xlabel("t - Время")
        ax1.set_ylabel("x - Положение; v - Скорость")

        # Включение сетки и легенды
        ax1.grid(True)
        ax1.legend()

        # Сохранение графика xvt в файл с прозрачным фоном
        graph_path_1 = Path("graph/oscillator_graph_xvt.png")
        plt.savefig(graph_path_1, transparent=True)

        # Создание Excel-файла для графика xvt
        excel_file_path_1 = Path("graph/oscillator_data_xvt.xlsx")
        data = {"t": t, "x": x, "v": v}
        df = pd.DataFrame(data)
        df.to_excel(excel_file_path_1, index=False)

        # Создание графика xt
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        fig2.patch.set_facecolor((1, 1, 1, 0))  # Устанавливаем прозрачный фон для холста

        # Построение графика x(t) - синяя линия
        ax2.plot(t, x, label="x(t) - Положение", color="blue")

        ax2.set_title("Колебания линейного гармонического осциллятора с учётом трения")
        ax2.set_xlabel("t - Время")
        ax2.set_ylabel("x - Положение")
        ax2.grid(True)
        ax2.legend()

        # Сохранение графика xt в файл с прозрачным фоном
        graph_path_2 = Path("graph/oscillator_graph_xt.png")
        plt.savefig(graph_path_2, transparent=True)

        # Создание Excel-файла
        excel_file_path_2 = Path("graph/oscillator_data_xt.xlsx")
        data = {"t": t, "x": x}
        df = pd.DataFrame(data)
        df.to_excel(excel_file_path_2, index=False)

        # Создание графика vt
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        fig3.patch.set_facecolor((1, 1, 1, 0))  # Устанавливаем прозрачный фон для холста

        # Построение графика v(t) - розовая линия
        ax3.plot(t, v, label="v(t) - Скорость", color="pink")

        ax3.set_title("Колебания линейного гармонического осциллятора с учётом трения")
        ax3.set_xlabel("t - Время")
        ax3.set_ylabel("v - Скорость")
        ax3.grid(True)
        ax3.legend()

        # Сохранение графика vt в файл с прозрачным фоном
        graph_path_3 = Path("graph/oscillator_graph_vt.png")
        plt.savefig(graph_path_3, transparent=True)

        # Создание Excel-файла для графика xvt
        excel_file_path_3 = Path("graph/oscillator_data_vt.xlsx")
        data = {"t": t, "v": v}
        df = pd.DataFrame(data)
        df.to_excel(excel_file_path_3, index=False)

        # Сохранение путей к графикам и файлам в список
        self.graph_paths = [graph_path_1, graph_path_2, graph_path_3]
        self.excel_paths = [excel_file_path_1, excel_file_path_2, excel_file_path_3]

        # Установка начального изображения
        self.graph_counter = 0
        self.update_graph()

        # Делаем видимыми стрелочки переключения
        self.ui.pushButton.setHidden(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setHidden(False)

        # Блокировка кнопки "Сгенерировать", разблокировка кнопок "Сброс", "Печать", "Excel"
        self.ui.button_reset.setEnabled(True)
        self.ui.button_print.setEnabled(True)
        self.ui.button_excel.setEnabled(True)
        self.ui.button_start.setEnabled(False)

    def show_next_graph(self):
        # Переключение на следующий график
        if self.graph_counter < len(self.graph_paths) - 1:
            self.graph_counter += 1
            self.update_graph()

        # Если мы достигли последнего графика, отключаем кнопку "Вперед"
        if self.graph_counter == len(self.graph_paths) - 1:
            self.ui.pushButton_2.setEnabled(False)

        # Всегда включаем кнопку "Назад", если это не первый график
        if self.graph_counter > 0:
            self.ui.pushButton.setEnabled(True)

    def show_previous_graph(self):
        # Переключение на предыдущий график
        if self.graph_counter > 0:
            self.graph_counter -= 1
            self.update_graph()

        # Если мы достигли первого графика, отключаем кнопку "Назад"
        if self.graph_counter == 0:
            self.ui.pushButton.setEnabled(False)

        # Всегда включаем кнопку "Вперед", если это не последний график
        if self.graph_counter < len(self.graph_paths) - 1:
            self.ui.pushButton_2.setEnabled(True)

    def update_graph(self):
        # Обновляем QPixmap текущего графика и отображаем его
        self.pixmap = QPixmap(self.graph_paths[self.graph_counter])

        # Масштабируем изображение, сохраняя пропорции
        scaled_pixmap = self.pixmap.scaled(self.ui.label_graph.width(), self.ui.label_graph.height(),
                                           Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Устанавливаем масштабированное изображение в QLabel
        self.ui.label_graph.setPixmap(scaled_pixmap)

    def restart_graph(self):
        # Очистка полей ввода и графика
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

        # Блокировка кнопок "Печать", "Excel", разблокировка кнопки "Сгенерировать", скрытие стрелок переключения
        self.ui.button_print.setEnabled(False)
        self.ui.button_excel.setEnabled(False)
        self.ui.button_start.setEnabled(True)
        self.ui.pushButton.setHidden(True)
        self.ui.pushButton_2.setHidden(True)

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

    def open_excel(self):
        # Открытие Excel файла, связанного с текущим графиком
        excel_file_path = self.excel_paths[self.graph_counter]
        if os.path.exists(excel_file_path):
            os.startfile(excel_file_path)
        else:
            self.error_incorrect_input_message("Ошибка при открытии файла", "Файл не найден в директории.")

    def upload_excel(self):
        # Открытие проводника для выбора Excel-файла
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите Excel-файл", "",
                                                   "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_name:
            try:
                # Чтение данных из Excel-файла
                df = pd.read_excel(file_name)

                # Предполагается, что файл Excel содержит следующие столбцы:
                # 't0', 'tk', 'dt1', 'dt2', 'x0', 'v0', 'w0', 'y'

                # Заполнение полей ввода данными из Excel
                self.ui.entry_t0.setText(str(df["t0"].iloc[0]))
                self.ui.entry_tk.setText(str(df["tk"].iloc[0]))
                self.ui.entry_dt1.setText(str(df["dt1"].iloc[0]))
                self.ui.entry_dt2.setText(str(df["dt2"].iloc[0]))
                self.ui.entry_x0.setText(str(df["x0"].iloc[0]))
                self.ui.entry_v0.setText(str(df["v0"].iloc[0]))
                self.ui.entry_w0.setText(str(df["w0"].iloc[0]))
                self.ui.entry_y.setText(str(df["y"].iloc[0]))

                # Проверка полей ввода и активация кнопки сброса
                self.check_input_fields()

            except Exception as e:
                self.error_incorrect_input_message("Ошибка при чтении файла", f"Проверьте корректность "
                                                                              f"формата ввода данных в файле.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
