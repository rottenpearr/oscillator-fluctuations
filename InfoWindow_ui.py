# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoWindow.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources

class Ui_info_win(object):
    def setupUi(self, info_win):
        if not info_win.objectName():
            info_win.setObjectName(u"info_win")
        info_win.setEnabled(True)
        info_win.resize(600, 800)
        info_win.setMinimumSize(QSize(600, 800))
        info_win.setMaximumSize(QSize(600, 800))
        info_win.setBaseSize(QSize(1000, 850))
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
        info_win.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(14)
        info_win.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/help icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        info_win.setWindowIcon(icon)
        info_win.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0446\u0432\u0435\u0442\u0430 */\n"
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
"}\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:vertical {\n"
"        border: none;\n"
"        background-color: rgb(244, 249, 252); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        width: 14px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    }\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(info_win)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_8)

        self.label = QLabel(info_win)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_6)

        self.textEdit = QTextEdit(info_win)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: rgba(136, 194, 206, 90);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"")
        self.textEdit.setLineWrapColumnOrWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(info_win)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_7)

        self.textEdit_2 = QTextEdit(info_win)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"background-color: rgba(136, 194, 206, 90);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(info_win)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setBaseSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 6px;\n"
"font-size: 16pt;")
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(7, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(info_win)

        QMetaObject.connectSlotsByName(info_win)
    # setupUi

    def retranslateUi(self, info_win):
        info_win.setWindowTitle(QCoreApplication.translate("info_win", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("info_win", u"<html><head/><body><p><span style=\" font-size:22pt;\">\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("info_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto Medium'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0443\u0435\u0442 \u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u044f \u0433\u0430\u0440\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043e"
                        "\u0441\u0446\u0438\u043b\u043b\u044f\u0442\u043e\u0440\u0430.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0427\u0442\u043e\u0431\u044b \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 \u043d\u0443\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0432 \u043c\u0435\u043d\u044e \u0432\u0432\u043e\u0434\u0430 \u0438\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u0431 \u043e\u0441\u0446\u0438\u043b\u043b\u044f\u0442\u043e\u0440\u0435:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">t<span"
                        " style=\" vertical-align:sub;\">0</span>, t<span style=\" vertical-align:sub;\">k</span> \u2013 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439 \u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 (\u0441); </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">x<span style=\" vertical-align:sub;\">0</span> \u2013 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0433\u0440\u0443\u0437\u0430 (\u043c); </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">v<span style=\" vertical-align:sub;\">0</span> \u2013 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c (\u043c/c); </p>\n"
"<p style=\" margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">k \u2013 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0436\u0451\u0441\u0442\u043a\u043e\u0441\u0442\u0438 \u043f\u0440\u0443\u0436\u0438\u043d\u044b (\u041d/\u043c); </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">m - \u043c\u0430\u0441\u0441\u0430 \u0433\u0440\u0443\u0437\u0430 (\u043a\u0433);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">y \u2013 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0442\u0440\u0435\u043d\u0438\u044f;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dt<span style=\" vertical-align:sub;\">1</span> \u2013 \u043f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 (\u0442. \u0435. \u0438"
                        "\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u0447\u0435\u0440\u0435\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u0442\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445) (\u0441); </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dt<span style=\" vertical-align:sub;\">2</span> (\u0394t) \u2013 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u0438 (\u0441).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0430\u043a\u0436\u0435"
                        " \u0434\u0430\u043d\u043d\u044b\u0435 \u043c\u043e\u0436\u043d\u043e \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 \u0432\u0438\u0434\u0435 excel-\u0444\u0430\u0439\u043b\u0430 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043d\u043e\u043f\u043a\u0438 &quot;\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c&quot;. \u0414\u043b\u044f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f \u0432 \u0444\u0430\u0439\u043b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u044c\u0441\u044f \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0441 \u0438\u043c\u0435\u043d\u0430\u043c\u0438 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445, \u0430 \u0432 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0439 \u044f\u0447\u0435\u0439\u043a\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 - \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439.</p>\n"
"<p style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 &quot;\u0421\u0413\u0415\u041d\u0415\u0420\u0418\u0420\u041e\u0412\u0410\u0422\u042c&quot; \u043d\u0430 \u044d\u043a\u0440\u0430\u043d\u0435 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0433\u0440\u0430\u0444\u0438\u043a \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u043c \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u043c.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0441\u0435\u0433\u043e \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442\u0441\u044f 3 \u0442\u0438\u043f\u0430 \u0433\u0440\u0430\u0444"
                        "\u0438\u043a\u0430:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 \u0442\u0438\u043f - \u0433\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 x, v, t;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 \u0442\u0438\u043f - \u0433\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 x, t;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 \u0442\u0438\u043f - \u0433\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 v, t.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043c\u0435\u0436"
                        "\u0434\u0443 \u043d\u0438\u043c\u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0441\u0442\u0440\u0435\u043b\u043e\u043a &quot;&lt;&quot; \u0438 &quot;&gt;&quot;.<br /><br />\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a \u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043d\u043e\u043f\u043a\u0438 &quot;\u041f\u0415\u0427\u0410\u0422\u042c&quot; \u0438\u043b\u0438 \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c excel-\u0444\u0430\u0439\u043b \u0441 \u0442\u0430\u0431\u043b\u0438\u0446\u0435\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;EXCEL&quot;.<br /><br />\u0415\u0441\u043b\u0438 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 \u0437\u0430\u043d\u0443\u043b\u0438\u0442\u044c"
                        " \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0442\u0440\u0435\u043d\u0438\u044f, \u0442\u043e \u0432 excel-\u0444\u0430\u0439\u043b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 x, v, t \u043f\u043e\u044f\u0432\u044f\u0442\u0441\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0438 &quot;\u041f\u043e\u043b\u043d\u0430\u044f \u044d\u043d\u0435\u0440\u0433\u0438\u044f Ei&quot;, &quot;\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0439 \u044d\u043d\u0435\u0440\u0433\u0438\u0438 Esr&quot;, &quot;\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c \u043f\u043e \u044d\u043d\u0435\u0440\u0433\u0438\u0438 di&quot; \u0438 &quot;\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0442\u043d"
                        "\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c dsr&quot; \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0437\u0430\u043a\u043e\u043d\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u044d\u043d\u0435\u0440\u0433\u0438\u0438 \u0432 \u043f\u043e\u043b\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u0435. \u0420\u0430\u0441\u0447\u0451\u0442\u044b \u043f\u043e \u0444\u043e\u0440\u043c\u0443\u043b\u0430\u043c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u043d\u0430 \u043a\u0430\u0436\u0434\u043e\u043c \u0440\u0430\u0441\u0447\u0451\u0442\u043d\u043e\u043c \u0448\u0430\u0433\u0435.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("info_win", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("info_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto Medium'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0430 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u043b\u0435\u0442\u043d\u0435\u0439 \u0443\u0447\u0435\u0431\u043d\u043e\u0439 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0438 \u043d\u0430 2 \u043a\u0443\u0440\u0441\u0435 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f 09.03.02 \u0418"
                        "\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438 \u0423\u0440\u0430\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u0424\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0430 \u0438\u043c\u0435\u043d\u0438 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0440\u0435\u0437\u0438\u0434\u0435\u043d\u0442\u0430 \u0420\u043e\u0441\u0441\u0438\u0438 \u0411.\u041d. \u0415\u043b\u044c\u0446\u0438\u043d\u0430.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a:</span"
                        "> \u041c\u0430\u0440\u043a\u043e\u0432\u0430 \u0410\u043b\u0451\u043d\u0430 \u0414\u0435\u043d\u0438\u0441\u043e\u0432\u043d\u0430</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0438:</span> \u041a\u0438\u0431\u0430\u0440\u0434\u0438\u043d \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("info_win", u"\u041e\u041a", None))
    # retranslateUi

