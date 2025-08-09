# PySide6 Cheatsheet

A compact overview of **PySide6** with the most important widgets, layouts, signals/slots, dialogues, styling, events and more. Experimenting with PySide6 and creating a modern UI This project is a personal exploration of PySide6 (Qt for Python) to build clean, modern, and responsive desktop applications.

## Basic window
```python
from PySide6 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QMainWindow()
    win.setWindowTitle("App")
    win.resize(800, 600)
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

## Important Namespaces
-QtWidgets: UI-Widgets (Button, Label, Layouts, Dialoge, MainWindow …)
-QtCore: Basistypen (QObject, QTimer, QThread, Signals/Slots, Datentypen)
-QtGui: Malen, Fonts, Icons, Farben, QPainter, Aktionen, Shortcuts

## Layouts/Widgets, Button, Edit
```python
layout = QtWidgets.QVBoxLayout()  # Vertikal
btn = QtWidgets.QPushButton("OK")
edit = QtWidgets.QLineEdit()
layout.addWidget(edit)
layout.addWidget(btn)
```

## Button pressed handle
```python
btn.clicked.connect(lambda: print("Klick"))
edit.textChanged.connect(lambda s: print("Text:", s))
```

## Menu, Toolbar & Shortcuts
```python
act = QtGui.QAction("Öffnen", parent)
act.setShortcut("Ctrl+O")
menu = parent.menuBar().addMenu("Datei")
menu.addAction(act)
```

## Styling example
```python
widget.setStyleSheet("""
    QPushButton { padding: 8px; border-radius: 5px; }
""")
```

## Ressources, Icons, Pictures
```python
pix = QtGui.QPixmap("bild.png")
label.setPixmap(pix)
```

## Drag & Drop
```python
edit.setAcceptDrops(True)
```