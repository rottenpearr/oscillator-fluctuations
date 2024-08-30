# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ErrorInputWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources


class Ui_Error_input_Window(object):
    def setupUi(self, Error_input_Window):
        if not Error_input_Window.objectName():
            Error_input_Window.setObjectName(u"Error_input_Window")
        Error_input_Window.resize(500, 350)
        Error_input_Window.setMinimumSize(QSize(500, 350))
        Error_input_Window.setMaximumSize(QSize(500, 350))
        Error_input_Window.setBaseSize(QSize(500, 250))
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
        Error_input_Window.setPalette(palette)
        Error_input_Window.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0446\u0432\u0435\u0442\u0430 */\n"
"QWidget {\n"
"    color: rgb(0, 0, 0); /* WindowText */\n"
"    background-color: rgb(244, 249, 252); /* Window */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    background-color: rgb(136, 194, 206); /* Button */\n"
"    color: rgb(16, 16, 15); /* ButtonText */\n"
"    border: 1px solid rgb(105, 88, 79);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(147, 208, 220);  /* Button */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110, 158, 167);  /* Button */\n"
"}\n"
"\n"
"/* \u0422\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0435 \u043f\u043e\u043b\u044f */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"    background-color: rgb(255, 255, 255); /* Base */\n"
"    color: rgb(16, 16, 15); /* Text */\n"
"    border: 1px solid rgb(141, 118, 105); /* Mid */\n"
"}\n"
"\n"
"/* \u041b\u0435\u0439\u0431\u043b\u044b */\n"
"QLabel {\n"
"    color: rgb(16, 16, 15"
                        "); /* WindowText */\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Error_input_Window)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Error_input_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(28, 28))
        self.label_2.setMaximumSize(QSize(28, 28))
        self.label_2.setBaseSize(QSize(28, 28))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(22)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setPixmap(QPixmap(u":/icons/images/error.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(0)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(Error_input_Window)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(22)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 10)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label = QLabel(Error_input_Window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 110))
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_error_ok = QPushButton(Error_input_Window)
        self.button_error_ok.setObjectName(u"button_error_ok")
        self.button_error_ok.setMinimumSize(QSize(150, 35))
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setStrikeOut(False)
        self.button_error_ok.setFont(font3)
        self.button_error_ok.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")

        self.horizontalLayout.addWidget(self.button_error_ok)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Error_input_Window)

        QMetaObject.connectSlotsByName(Error_input_Window)
    # setupUi

    def retranslateUi(self, Error_input_Window):
        Error_input_Window.setWindowTitle(QCoreApplication.translate("Error_input_Window", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0432\u0432\u043e\u0434\u0430", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Error_input_Window", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("Error_input_Window", u"<html><head/><body><p>\u0423\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c, \u0447\u0442\u043e \u0432\u0432\u0435\u0434\u0435\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0432\u0443\u044e\u0442 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u043c:</p><p>t<span style=\" vertical-align:sub;\">0</span> &lt; t<span style=\" vertical-align:sub;\">k</span>;</p><p>dt<span style=\" vertical-align:sub;\">1</span> &gt; 0; dt<span style=\" vertical-align:sub;\">2</span> &gt; 0; dt<span style=\" vertical-align:sub;\">1</span> &gt;= dt2;</p><p>\u03b3 &gt;= 0; \u03c9<span style=\" vertical-align:sub;\">0</span> &gt; 0.</p></body></html>", None))
        self.button_error_ok.setText(QCoreApplication.translate("Error_input_Window", u"\u041e\u041a", None))
    # retranslateUi

