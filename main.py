"""Small description of the project.

This project aims to record the keyboard keys
using the pynput library as well as pyqt5.
Most of the functions are defined in snake_case (Python)
contrary to PyQt5 which uses CamelCase (C++).

No copyright.
"""

__author__ = '{Armanta}'
__copyright__ = 'Copyright {2020}, {NoCopyright}'
__credits__ = ['{Armanta}']
__license__ = '{NoLicense}'
__version__ = '{0}.{0}.{1}'
__maintainer__ = '{Armanta}'
__email__ = '{antoine.chauvin@live.fr}'


#Lib
from settings import *
from PyQt5 import QtCore, QtGui, QtWidgets
from time import monotonic
from pynput import keyboard
from math import trunc


class Ui_Label_Fade(QtWidgets.QLabel):
    def __init__(self):
        QtWidgets.QLabel.__init__(self)


    def fade(self, duration : int, start_value : int, end_value : int) -> None:
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(FADE_DURATION * 1000)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.start()


class Ui_GridLayout(QtWidgets.QGridLayout):
    def __init__(self, *args):
        QtWidgets.QGridLayout.__init__(self, *args)
    

    def clear(self) -> None:
        for i in reversed(range(self.count())):
                layout = self.itemAt(i)
                for _ in range(2):
                    layout.itemAt(0).widget().setParent(None)
                layout.setParent(None)
    

    def find_empty_position(self, col_span : int, max_row : int, max_col : int) -> None:
        for row in range(self.rowCount()):
            for column in range(self.columnCount() + 1):
                if col_span + column <= max_col and not self.itemAtPosition(row,column) and not self.itemAtPosition(row + 1,0):
                    return [row, column]
        return [self.rowCount(), 0]


class Listener(keyboard.Listener, QtCore.QObject):
    released = QtCore.pyqtSignal(str,float)

    def __init__(self):
        keyboard.Listener.__init__(self, on_press = self.on_press, on_release = self.on_release)
        QtCore.QObject.__init__(self)
        self.active_key = []
        self.time_started = None
        self.time_finished = None


    def code_to_string(self, code : keyboard._win32.KeyCode) -> str:
        try:
            code = code.char
        except AttributeError:
            code = KEYS[code]
        finally:
            return code


    def on_press(self, code : keyboard._win32.KeyCode) -> None:
        key = self.code_to_string(code)
        if not key in self.active_key:
            self.time_started = monotonic()
            self.active_key.append(key)


    def on_release(self, code : keyboard._win32.KeyCode) -> None:
        key = self.code_to_string(code)
        self.time_finished = monotonic()
        elapsed_time = round(self.time_finished - self.time_started, 3)
        try:
            self.active_key.remove(key)
            self.released.emit(key, elapsed_time)
        except ValueError:
            pass


class Ui_MainWindow(object):
    def __init__(self):
        self.listener = Listener()
        self.listener.released.connect(self.add_key)
        self.listener.start()


    def setupUi(self, MainWindow :  QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(".QMainWindow{"
"background-color: rgb(11, 6, 39);"
"}")
        MainWindow.setFixedSize(QtCore.QSize(539, 312))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 151, 311))
        self.frame_menu.setAutoFillBackground(False)
        self.frame_menu.setStyleSheet(".QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_menu.setObjectName("frame_menu")
        self.text_home = QtWidgets.QLabel(self.frame_menu)
        self.text_home.setGeometry(QtCore.QRect(0, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(22)
        self.text_home.setFont(font)
        self.text_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_home.setAutoFillBackground(False)
        self.text_home.setAlignment(QtCore.Qt.AlignCenter)
        self.text_home.setObjectName("text_home")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(152, 0, 381, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setContentsMargins(0, 0, 0, 0)
        self.layout_log = Ui_GridLayout(self.gridLayoutWidget)
        self.layout_log.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layout_log.setVerticalSpacing(VERTICAL_SPACING)
        self.layout_log.setHorizontalSpacing(HORIZONTAL_SPACING)
        self.layout_log.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_log.setContentsMargins(0, 0, 0, 0)
        self.layout_log.setObjectName("layout_log")
        self.init_grid()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def init_grid(self) -> None:
        self.max_row = trunc(self.gridLayoutWidget.size().height()/BOX_HEIGHT)
        self.max_column = trunc(self.gridLayoutWidget.size().width()/BOX_WIDTH)
        self.layout_log.setDefaultPositioning(self.max_column, QtCore.Qt.Horizontal)
    

    def set_font_size(self, label : QtWidgets.QLabel) -> None:
        if FONT_SIZE:
            font_measure = QtGui.QFontMetrics(QtGui.QFont(label.fontInfo().family(), FONT_SIZE))
            if font_measure.width(label.text()) > BOX_WIDTH:
                error = QtWidgets.QMessageBox()
                error.setIcon(QtWidgets.QMessageBox.Critical)
                error.setText("Too high font")
                error.setWindowTitle("Error")
                sys.exit(error.exec_())
            else:
                font_family = label.fontInfo().family()
                label.setFont(QtGui.QFont(font_family, FONT_SIZE))
        else:
            font_measure = QtGui.QFontMetrics(QtGui.QFont(label.fontInfo().family(), label.fontInfo().pointSize()))
            while font_measure.width(label.text()) < BOX_WIDTH:
                font_family = label.fontInfo().family()
                font_size = label.fontInfo().pointSize()
                label.setFont(QtGui.QFont(font_family, font_size + 1))
                font_measure = QtGui.QFontMetrics(label.font())
            while font_measure.width(label.text()) > BOX_WIDTH:
                font_family = label.fontInfo().family()
                font_size = label.fontInfo().pointSize()
                label.setFont(QtGui.QFont(font_family, font_size - 1))
                font_measure = QtGui.QFontMetrics(label.font())

    
    def add_key(self, key : str, key_duration : int) -> None: 
        box_v = QtWidgets.QVBoxLayout()
        box_v.setSpacing(BOTH_SPACING)
        box_v.setContentsMargins(0, 0, 0, 0)
        img_obj = QtGui.QPixmap(f"{PATH}\\{key}.png")
        key_span = trunc(img_obj.width()/img_obj.height())
        if self.layout_log.itemAtPosition(self.max_row -1 , self.max_column - key_span):
            self.layout_log.clear()
        img_label = Ui_Label_Fade()
        txt_label = Ui_Label_Fade()
        box_v.setAlignment(QtCore.Qt.AlignCenter)
        img_label.setAlignment(QtCore.Qt.AlignCenter)
        txt_label.setAlignment(QtCore.Qt.AlignCenter)
        txt_label.setStyleSheet('color: white')
        txt_label.setText(f"Time:{key_duration}")
        txt_label.setFixedWidth(BOX_WIDTH * key_span)
        row, column = self.layout_log.find_empty_position(key_span, self.max_row, self.max_column)
        self.set_font_size(txt_label)
        font_measure = QtGui.QFontMetrics(txt_label.font())   
        scale_w = round(BOX_WIDTH * key_span)
        scale_h = round(BOX_HEIGHT - (font_measure.height() + BOTH_SPACING))
        img_obj = img_obj.scaled(scale_w, scale_h, QtCore.Qt.KeepAspectRatio)
        img_label.setPixmap(img_obj)
        box_v.addWidget(img_label)
        box_v.addWidget(txt_label)            
        self.layout_log.addLayout(box_v, row, column, 1, key_span, QtCore.Qt.AlignCenter)            
        txt_label.fade(2, 0, 1)
        img_label.fade(2, 0, 1)


    def retranslateUi(self, MainWindow :  QtWidgets.QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_home.setText(_translate("MainWindow", "HOME"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
