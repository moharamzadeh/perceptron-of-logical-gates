from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
	def setupUi(self, window):
		window.setObjectName("window")
		window.resize(435, 240)
		window.setMinimumSize(QtCore.QSize(435, 240))
		window.setMaximumSize(QtCore.QSize(435, 240))

		font = QtGui.QFont()
		font.setPointSize(10)
		window.setFont(font)

		self.txtX = QtWidgets.QLineEdit(window)
		self.txtX.setGeometry(QtCore.QRect(30, 10, 31, 33))
		self.txtX.setObjectName("txtX")

		self.txtY = QtWidgets.QLineEdit(window)
		self.txtY.setGeometry(QtCore.QRect(100, 10, 31, 33))
		self.txtY.setObjectName("txtY")

		self.txtAlpha = QtWidgets.QLineEdit(window)
		self.txtAlpha.setGeometry(QtCore.QRect(100, 70, 41, 33))
		self.txtAlpha.setObjectName("txtAlpha")

		self.txtW1 = QtWidgets.QLineEdit(window)
		self.txtW1.setGeometry(QtCore.QRect(40, 160, 41, 33))
		self.txtW1.setObjectName("txtW1")

		self.txtW2 = QtWidgets.QLineEdit(window)
		self.txtW2.setGeometry(QtCore.QRect(40, 200, 41, 33))
		self.txtW2.setObjectName("txtW2")

		self.comboBox = QtWidgets.QComboBox(window)
		self.comboBox.setGeometry(QtCore.QRect(140, 160, 61, 33))
		self.comboBox.setObjectName("comboBox")

		self.btnMohasebeh = QtWidgets.QPushButton(window)
		self.btnMohasebeh.setGeometry(QtCore.QRect(140, 200, 61, 33))
		self.btnMohasebeh.setObjectName("btnMohasebeh")

		self.txtOutput = QtWidgets.QTextBrowser(window)
		self.txtOutput.setGeometry(QtCore.QRect(210, 10, 211, 221))

		font = QtGui.QFont()
		font.setPointSize(8)

		self.txtOutput.setFont(font)
		self.txtOutput.setObjectName("txtOutput")

		self.lblX = QtWidgets.QLabel(window)
		self.lblX.setGeometry(QtCore.QRect(10, 20, 21, 17))
		self.lblX.setObjectName("lblX")

		self.lblY = QtWidgets.QLabel(window)
		self.lblY.setGeometry(QtCore.QRect(80, 20, 21, 17))
		self.lblY.setObjectName("lblY")

		self.lblAlpha = QtWidgets.QLabel(window)
		self.lblAlpha.setGeometry(QtCore.QRect(10, 80, 71, 17))
		self.lblAlpha.setObjectName("lblAlpha")

		self.line = QtWidgets.QFrame(window)
		self.line.setGeometry(QtCore.QRect(10, 50, 151, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")

		self.line2 = QtWidgets.QFrame(window)
		self.line2.setGeometry(QtCore.QRect(10, 110, 151, 16))
		self.line2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line2.setObjectName("line2")

		self.lblW = QtWidgets.QLabel(window)
		self.lblW.setGeometry(QtCore.QRect(40, 130, 41, 17))
		self.lblW.setObjectName("lblW")

		self.btnClear = QtWidgets.QPushButton(window)
		self.btnClear.setGeometry(QtCore.QRect(170, 10, 31, 33))
		self.btnClear.setObjectName("btnClear")

		self.lblW1 = QtWidgets.QLabel(window)
		self.lblW1.setGeometry(QtCore.QRect(10, 170, 31, 17))
		self.lblW1.setObjectName("lblW1")

		self.lblW2 = QtWidgets.QLabel(window)
		self.lblW2.setGeometry(QtCore.QRect(10, 210, 31, 17))
		self.lblW2.setObjectName("lblW2")

		self.retranslateUi(window)
		QtCore.QMetaObject.connectSlotsByName(window)

		self.btnClear.clicked.connect(lambda: self.clickBtnClear())

	def clickBtnClear(self):
		self.__clearAllText()

	def __clearAllText(self):
		self.txtX.clear()
		self.txtY.clear()
		self.txtAlpha.clear()
		self.txtW1.clear()
		self.txtW2.clear()
		self.txtOutput.clear()
		self.txtX.setFocus()

	def retranslateUi(self, window):
		_translate = QtCore.QCoreApplication.translate
		window.setWindowTitle(_translate("window", "گیت‌های منطقی"))
		self.lblX.setText(_translate("window", "x:"))
		self.lblY.setText(_translate("window", "y:"))
		self.lblAlpha.setText(_translate("window", "نرخ یادگیری"))
		self.lblW.setText(_translate("window", "وزن‌ها"))
		self.btnClear.setText(_translate("window", "C"))
		self.lblW1.setText(_translate("window", "w1:"))
		self.lblW2.setText(_translate("window", "w2:"))
		self.btnMohasebeh.setText(_translate("window", "محاسبه"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QWidget()
	ui = Ui_window()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())

