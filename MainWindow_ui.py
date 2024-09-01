# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 900)
        MainWindow.setMinimumSize(QSize(800, 600))
        palette = QPalette()
        brush = QBrush(QColor(16, 16, 15, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(244, 249, 252, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(136, 194, 206, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Accent, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush3)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/icons/win icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0446\u0432\u0435\u0442\u0430 */\n"
"QWidget {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(244, 249, 252); \n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    background-color: rgb(136, 194, 206);\n"
"    color: rgb(16, 16, 15);\n"
"    border: 1px solid rgb(105, 88, 79);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(147, 208, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110, 158, 167);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(214, 223, 232);\n"
"}\n"
"\n"
"/* \u0422\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0435 \u043f\u043e\u043b\u044f */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(16, 16, 15);\n"
"    border: 1px solid rgb(141, 118, 105);\n"
"}\n"
"\n"
"/* \u041b\u0435\u0439\u0431\u043b\u044b */\n"
"QLabel {\n"
"    color: rgb(16, 16, 15);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.centralwidget.setStyleSheet(u"font-family: Roboto Medium;")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.data_input_groupBox = QGroupBox(self.centralwidget)
        self.data_input_groupBox.setObjectName(u"data_input_groupBox")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        brush5 = QBrush(QColor(136, 194, 206, 90))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.data_input_groupBox.setPalette(palette2)
        self.data_input_groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.data_input_groupBox.setAutoFillBackground(False)
        self.data_input_groupBox.setStyleSheet(u"background-color: rgba(136, 194, 206, 90);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"")
        self.verticalLayout = QVBoxLayout(self.data_input_groupBox)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setContentsMargins(1, 1, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_23)

        self.layout_input_data = QHBoxLayout()
        self.layout_input_data.setSpacing(6)
        self.layout_input_data.setObjectName(u"layout_input_data")
        self.layout_input_data.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.layout_input_data.setContentsMargins(0, 1, -1, -1)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_input_data.addItem(self.horizontalSpacer_24)

        self.label = QLabel(self.data_input_groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 40))
        self.label.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_input_data.addWidget(self.label)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_input_data.addItem(self.horizontalSpacer_25)

        self.layout_input_data.setStretch(1, 15)

        self.verticalLayout.addLayout(self.layout_input_data)

        self.horizontalSpacer_26 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_26)

        self.layout_t0 = QHBoxLayout()
        self.layout_t0.setObjectName(u"layout_t0")
        self.horizontalSpacer_22 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_t0.addItem(self.horizontalSpacer_22)

        self.label_t0 = QLabel(self.data_input_groupBox)
        self.label_t0.setObjectName(u"label_t0")
        self.label_t0.setMinimumSize(QSize(50, 40))
        self.label_t0.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_t0.setTextFormat(Qt.TextFormat.AutoText)
        self.label_t0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_t0.setWordWrap(False)
        self.label_t0.setOpenExternalLinks(False)

        self.layout_t0.addWidget(self.label_t0)

        self.entry_t0 = QLineEdit(self.data_input_groupBox)
        self.entry_t0.setObjectName(u"entry_t0")
        self.entry_t0.setMinimumSize(QSize(0, 30))
        self.entry_t0.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;\n"
"")
        self.entry_t0.setFrame(True)
        self.entry_t0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_t0.addWidget(self.entry_t0)

        self.horizontalSpacer_18 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_t0.addItem(self.horizontalSpacer_18)

        self.layout_t0.setStretch(1, 2)
        self.layout_t0.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_t0)

        self.layout_tk = QHBoxLayout()
        self.layout_tk.setObjectName(u"layout_tk")
        self.horizontalSpacer_21 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_tk.addItem(self.horizontalSpacer_21)

        self.label_tk = QLabel(self.data_input_groupBox)
        self.label_tk.setObjectName(u"label_tk")
        self.label_tk.setMinimumSize(QSize(50, 40))
        self.label_tk.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_tk.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_tk.addWidget(self.label_tk)

        self.entry_tk = QLineEdit(self.data_input_groupBox)
        self.entry_tk.setObjectName(u"entry_tk")
        self.entry_tk.setMinimumSize(QSize(0, 30))
        self.entry_tk.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")

        self.layout_tk.addWidget(self.entry_tk)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_tk.addItem(self.horizontalSpacer_17)

        self.layout_tk.setStretch(1, 2)
        self.layout_tk.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_tk)

        self.layout_dt1 = QHBoxLayout()
        self.layout_dt1.setObjectName(u"layout_dt1")
        self.horizontalSpacer_20 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_dt1.addItem(self.horizontalSpacer_20)

        self.label_dt1 = QLabel(self.data_input_groupBox)
        self.label_dt1.setObjectName(u"label_dt1")
        self.label_dt1.setMinimumSize(QSize(50, 40))
        self.label_dt1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_dt1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_dt1.addWidget(self.label_dt1)

        self.entry_dt1 = QLineEdit(self.data_input_groupBox)
        self.entry_dt1.setObjectName(u"entry_dt1")
        self.entry_dt1.setMinimumSize(QSize(0, 30))
        self.entry_dt1.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")

        self.layout_dt1.addWidget(self.entry_dt1)

        self.horizontalSpacer_16 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_dt1.addItem(self.horizontalSpacer_16)

        self.layout_dt1.setStretch(1, 2)
        self.layout_dt1.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_dt1)

        self.layout_dt2 = QHBoxLayout()
        self.layout_dt2.setObjectName(u"layout_dt2")
        self.horizontalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_dt2.addItem(self.horizontalSpacer_14)

        self.label_dt2 = QLabel(self.data_input_groupBox)
        self.label_dt2.setObjectName(u"label_dt2")
        self.label_dt2.setMinimumSize(QSize(50, 40))
        self.label_dt2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_dt2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_dt2.addWidget(self.label_dt2)

        self.entry_dt2 = QLineEdit(self.data_input_groupBox)
        self.entry_dt2.setObjectName(u"entry_dt2")
        self.entry_dt2.setMinimumSize(QSize(0, 30))
        self.entry_dt2.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        self.entry_dt2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_dt2.addWidget(self.entry_dt2)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_dt2.addItem(self.horizontalSpacer_15)

        self.layout_dt2.setStretch(1, 2)
        self.layout_dt2.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_dt2)

        self.layout_x0 = QHBoxLayout()
        self.layout_x0.setObjectName(u"layout_x0")
        self.horizontalSpacer_12 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_x0.addItem(self.horizontalSpacer_12)

        self.label_x0 = QLabel(self.data_input_groupBox)
        self.label_x0.setObjectName(u"label_x0")
        self.label_x0.setMinimumSize(QSize(50, 40))
        self.label_x0.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_x0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_x0.addWidget(self.label_x0)

        self.entry_x0 = QLineEdit(self.data_input_groupBox)
        self.entry_x0.setObjectName(u"entry_x0")
        self.entry_x0.setMinimumSize(QSize(0, 30))
        self.entry_x0.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        self.entry_x0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_x0.addWidget(self.entry_x0)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_x0.addItem(self.horizontalSpacer_13)

        self.layout_x0.setStretch(1, 2)
        self.layout_x0.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_x0)

        self.layout_v0 = QHBoxLayout()
        self.layout_v0.setObjectName(u"layout_v0")
        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_v0.addItem(self.horizontalSpacer_11)

        self.label_v0 = QLabel(self.data_input_groupBox)
        self.label_v0.setObjectName(u"label_v0")
        self.label_v0.setMinimumSize(QSize(50, 40))
        self.label_v0.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_v0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_v0.addWidget(self.label_v0)

        self.entry_v0 = QLineEdit(self.data_input_groupBox)
        self.entry_v0.setObjectName(u"entry_v0")
        self.entry_v0.setMinimumSize(QSize(0, 30))
        self.entry_v0.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")

        self.layout_v0.addWidget(self.entry_v0)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_v0.addItem(self.horizontalSpacer_10)

        self.layout_v0.setStretch(1, 2)
        self.layout_v0.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_v0)

        self.layout_w0 = QHBoxLayout()
        self.layout_w0.setObjectName(u"layout_w0")
        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_w0.addItem(self.horizontalSpacer_6)

        self.label_w0 = QLabel(self.data_input_groupBox)
        self.label_w0.setObjectName(u"label_w0")
        self.label_w0.setMinimumSize(QSize(50, 40))
        self.label_w0.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_w0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_w0.addWidget(self.label_w0)

        self.entry_w0 = QLineEdit(self.data_input_groupBox)
        self.entry_w0.setObjectName(u"entry_w0")
        self.entry_w0.setMinimumSize(QSize(0, 30))
        self.entry_w0.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")

        self.layout_w0.addWidget(self.entry_w0)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_w0.addItem(self.horizontalSpacer_9)

        self.layout_w0.setStretch(1, 2)
        self.layout_w0.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_w0)

        self.layout_y = QHBoxLayout()
        self.layout_y.setObjectName(u"layout_y")
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_y.addItem(self.horizontalSpacer_5)

        self.label_y = QLabel(self.data_input_groupBox)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setMinimumSize(QSize(50, 40))
        self.label_y.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"border-radius: none;")
        self.label_y.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_y.addWidget(self.label_y)

        self.entry_y = QLineEdit(self.data_input_groupBox)
        self.entry_y.setObjectName(u"entry_y")
        self.entry_y.setMinimumSize(QSize(0, 30))
        self.entry_y.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")

        self.layout_y.addWidget(self.entry_y)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_y.addItem(self.horizontalSpacer_8)

        self.layout_y.setStretch(1, 2)
        self.layout_y.setStretch(2, 15)

        self.verticalLayout.addLayout(self.layout_y)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_32)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_31 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_31)

        self.button_upload = QPushButton(self.data_input_groupBox)
        self.button_upload.setObjectName(u"button_upload")
        self.button_upload.setMinimumSize(QSize(100, 50))
        self.button_upload.setBaseSize(QSize(100, 100))
        self.button_upload.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;\n"
"background-color: rgb(136, 194, 206); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(147, 208, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110, 158, 167);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/upload.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_upload.setIcon(icon1)
        self.button_upload.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.button_upload)

        self.horizontalSpacer_30 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_30)

        self.horizontalLayout.setStretch(1, 17)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_29)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_info.addItem(self.horizontalSpacer_4)

        self.button_info = QPushButton(self.data_input_groupBox)
        self.button_info.setObjectName(u"button_info")
        self.button_info.setMinimumSize(QSize(100, 50))
        self.button_info.setBaseSize(QSize(100, 100))
        self.button_info.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.button_info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_info.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;\n"
"background-color: rgb(136, 194, 206); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(147, 208, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110, 158, 167);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/help.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_info.setIcon(icon2)
        self.button_info.setIconSize(QSize(20, 20))
        self.button_info.setAutoRepeatDelay(300)
        self.button_info.setAutoDefault(False)
        self.button_info.setFlat(False)

        self.layout_info.addWidget(self.button_info)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_info.addItem(self.horizontalSpacer_3)

        self.layout_info.setStretch(1, 17)

        self.verticalLayout.addLayout(self.layout_info)

        self.horizontalSpacer_7 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_7)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 2)
        self.verticalLayout.setStretch(7, 2)
        self.verticalLayout.setStretch(8, 2)
        self.verticalLayout.setStretch(9, 2)
        self.verticalLayout.setStretch(10, 2)
        self.verticalLayout.setStretch(11, 1)
        self.verticalLayout.setStretch(12, 2)
        self.verticalLayout.setStretch(14, 2)
        self.verticalLayout.setStretch(15, 1)

        self.horizontalLayout_9.addWidget(self.data_input_groupBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalSpacer_2 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_graph = QLabel(self.centralwidget)
        self.label_graph.setObjectName(u"label_graph")
        self.label_graph.setMinimumSize(QSize(0, 0))
        self.label_graph.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_graph.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_graph)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setBaseSize(QSize(40, 30))
        self.pushButton.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_4)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setBaseSize(QSize(40, 30))
        self.pushButton_2.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_28)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_12.addItem(self.verticalSpacer_3)

        self.button_reset = QPushButton(self.centralwidget)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(50, 50))
        self.button_reset.setBaseSize(QSize(100, 100))
        self.button_reset.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/reset.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_reset.setIcon(icon5)
        self.button_reset.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.button_reset)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_12.addItem(self.verticalSpacer)

        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setMinimumSize(QSize(200, 50))
        self.button_start.setBaseSize(QSize(100, 100))
        self.button_start.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/start.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_start.setIcon(icon6)
        self.button_start.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.button_start)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_12.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 12)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(4, 1)

        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.button_print = QPushButton(self.centralwidget)
        self.button_print.setObjectName(u"button_print")
        self.button_print.setMinimumSize(QSize(110, 50))
        self.button_print.setBaseSize(QSize(100, 100))
        self.button_print.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/print.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_print.setIcon(icon7)
        self.button_print.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.button_print)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_27)

        self.button_excel = QPushButton(self.centralwidget)
        self.button_excel.setObjectName(u"button_excel")
        self.button_excel.setMinimumSize(QSize(110, 50))
        self.button_excel.setBaseSize(QSize(100, 100))
        self.button_excel.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/graph.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_excel.setIcon(icon8)
        self.button_excel.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.button_excel)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_19)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(4, 10)

        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 12)
        self.horizontalLayout_9.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_info.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u0439 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u0433\u0430\u0440\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043e\u0441\u0446\u0438\u043b\u043b\u044f\u0442\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445</span></p></body></html>", None))
        self.label_t0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">t</span><span style=\" font-size:22pt; vertical-align:sub;\">0</span></p></body></html>", None))
        self.label_tk.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">t</span><span style=\" font-size:22pt; vertical-align:sub;\">k</span></p></body></html>", None))
        self.label_dt1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">dt</span><span style=\" font-size:22pt; vertical-align:sub;\">1</span></p></body></html>", None))
        self.label_dt2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">dt</span><span style=\" font-size:22pt; vertical-align:sub;\">2</span></p></body></html>", None))
        self.label_x0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">x</span><span style=\" font-size:22pt; vertical-align:sub;\">0</span></p></body></html>", None))
        self.label_v0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">v</span><span style=\" font-size:22pt; vertical-align:sub;\">0</span></p></body></html>", None))
        self.label_w0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">\u03c9</span><span style=\" font-size:22pt; vertical-align:sub;\">0</span></p></body></html>", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">y</span></p></body></html>", None))
        self.button_upload.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c", None))
        self.button_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041d\u0424\u041e", None))
        self.label_graph.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.button_reset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0411\u0420\u041e\u0421", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0413\u0415\u041d\u0415\u0420\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.button_print.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0415\u0427\u0410\u0422\u042c", None))
        self.button_excel.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
    # retranslateUi

