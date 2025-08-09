# Message Box: QtWidgets.QMessageBox.information(window, "Hi")
# Button: QtWidgets.QPushButton("OK")   & btn.clicked.connect(on_click)  
# Input Feld: QtWidgets.QLineEdit()
# Label: QtWidgets.QLabel("Hier steht was")
# Layout edit: QtWidgets.QHBoxLayout(window)  &  layout.addWidget(obj)
# Fenster Größe: window.resize(480, 280)
# Datei Eingabefeld: QtWidgets.QLineEdit()
# Platzhalter Text: setPlaceholderText()
# Checkbox: QtWidgets.QCheckBox("Option 1"); QtWidgets.QCheckBox("Option 2") &   if isChecked():
# choose option a or option b: QtWidgets.QRadioButton("manually"); QtWidgets.QRadioButton("automatically"); manually.setChecked(True)

# add to layout: layout.addWidget(btn)


from PySide6 import QtWidgets, QtCore, QtGui
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Modern UI")
    layout = QtWidgets.QVBoxLayout(window)

    """actual code"""
    youtube_link = QtWidgets.QLineEdit()
    btn = QtWidgets.QPushButton("OK")
    manually = QtWidgets.QRadioButton("manually")
    automatically = QtWidgets.QRadioButton("automatically")

    layout.addWidget(youtube_link)
    layout.addWidget(manually)
    layout.addWidget(automatically)
    layout.addWidget(btn)
    """actual code"""

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
