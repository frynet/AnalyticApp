import os
from PyQt5.QtWidgets import QMessageBox

if __name__ == '__main__':
    try:
        os.system("python main.py")
    except Exception as e:
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.setWindowTitle("Возникла ошибка:")
        error_dialog.setText(e.args[0])

        error_dialog.show()
        error_dialog.exec_()
