import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

if __name__ == '__main__':
    try:
        os.system("python main.py")
    except Exception as e:
        qt_app = QApplication(sys.argv)

        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.setWindowTitle("Возникла ошибка:")
        error_dialog.setText(e.args[0])

        error_dialog.show()

        sys.exit(error_dialog.exec_())
