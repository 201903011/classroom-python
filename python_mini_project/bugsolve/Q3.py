# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Q3(object):
    def setupUi(self, Q3):
        Q3.setObjectName("Q3")
        Q3.resize(400, 300)

        self.retranslateUi(Q3)
        QtCore.QMetaObject.connectSlotsByName(Q3)

    def retranslateUi(self, Q3):
        _translate = QtCore.QCoreApplication.translate
        Q3.setWindowTitle(_translate("Q3", "Frame"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Q3 = QtWidgets.QFrame()
    ui = Ui_Q3()
    ui.setupUi(Q3)
    Q3.show()
    sys.exit(app.exec_())
