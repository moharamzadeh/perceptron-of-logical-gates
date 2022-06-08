from PyQt5 import QtCore, QtGui, QtWidgets
from main import *

class Ui_window(object):
	def setupUi(self, window):
		window.resize(435, 240)
		window.setMinimumSize(QtCore.QSize(435, 240))
		window.setMaximumSize(QtCore.QSize(435, 240))

		font = QtGui.QFont()
		font.setPointSize(10)
		window.setFont(font)

		self.txtAlpha = QtWidgets.QLineEdit(window)
		self.txtAlpha.setGeometry(QtCore.QRect(100, 10, 41, 33))

		self.txtW1 = QtWidgets.QLineEdit(window)
		self.txtW1.setGeometry(QtCore.QRect(40, 100, 41, 33))

		self.txtW2 = QtWidgets.QLineEdit(window)
		self.txtW2.setGeometry(QtCore.QRect(40, 140, 41, 33))

		self.comboBox = QtWidgets.QComboBox(window)
		self.comboBox.setGeometry(QtCore.QRect(115, 100, 85, 33))
		self.comboBox.addItems(['AND', 'OR', 'NOR', 'NAND'])

		self.btnMohasebeh = QtWidgets.QPushButton(window)
		self.btnMohasebeh.setGeometry(QtCore.QRect(115, 140, 85, 33))

		self.txtOutput = QtWidgets.QTextBrowser(window)
		self.txtOutput.setGeometry(QtCore.QRect(210, 10, 211, 221))

		font = QtGui.QFont()
		font.setPointSize(8)

		self.txtOutput.setFont(font)

		self.lblAlpha = QtWidgets.QLabel(window)
		self.lblAlpha.setGeometry(QtCore.QRect(10, 20, 71, 17))

		self.line2 = QtWidgets.QFrame(window)
		self.line2.setGeometry(QtCore.QRect(10, 50, 151, 16))
		self.line2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)

		self.lblW = QtWidgets.QLabel(window)
		self.lblW.setGeometry(QtCore.QRect(12, 70, 40, 17))

		self.btnClear = QtWidgets.QPushButton(window)
		self.btnClear.setGeometry(QtCore.QRect(170, 10, 31, 33))

		self.lblW1 = QtWidgets.QLabel(window)
		self.lblW1.setGeometry(QtCore.QRect(10, 110, 31, 17))

		self.lblW2 = QtWidgets.QLabel(window)
		self.lblW2.setGeometry(QtCore.QRect(10, 150, 31, 17))

		self.retranslateUi(window)
		QtCore.QMetaObject.connectSlotsByName(window)

		self.btnClear.clicked.connect(lambda: self.clickBtnClear())
		self.btnMohasebeh.clicked.connect(lambda: self.clickBtnMohasebeh())

	def clickBtnMohasebeh(self):
		answer = main(gate=self.comboBox.currentText(), alpha=float(self.txtAlpha.text()), w1=float(self.txtW1.text()), w2=float(self.txtW2.text()))
		matn = 'w1: ' + str(answer[0][0]) + '\n' + 'w2: ' + str(answer[0][1]) + '\n' + 'bias: ' + str(answer[1])
		print(matn)
		# print(answer)

	def clickBtnClear(self):
		self.__clearAllText()

	def __clearAllText(self):
		self.txtAlpha.clear()
		self.txtW1.clear()
		self.txtW2.clear()
		self.txtOutput.clear()
		self.txtAlpha.setFocus()

	def retranslateUi(self, window):
		_translate = QtCore.QCoreApplication.translate
		window.setWindowTitle(_translate("window", "گیت‌های منطقی"))
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

