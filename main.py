from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel("Нажата кнопка мыши")
        self.label2 = QLabel("Отпущена кнопка мыши")
        self.label3 = QLabel("Колесо прокручено")
        self.label4 = QLabel("Мышь перемещается")
        self.label5 = QLabel()
        self.label6 = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.widget3 = QWidget()

        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Событие 1"))
        self.widget1.setLayout(layout1)

        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Событие 2"))
        self.widget2.setLayout(layout2)

        layout3 = QVBoxLayout()
        layout3.addWidget(QLabel("Событие 3"))
        self.widget3.setLayout(layout3)

    def mousePressEvent(self, event):
        self.widget1.setStyleSheet("background-color: yellow;")
        self.widget2.setStyleSheet("")
        self.widget3.setStyleSheet("")
        self.label1.setText(f"Нажата кнопка мыши: {event.button()}")

    def mouseReleaseEvent(self, event):
        self.label2.setText(f"Отпущена кнопка мыши: {event.button()}")

        self.widget1.setStyleSheet("")
        self.widget2.setStyleSheet("background-color: black;")
        self.widget3.setStyleSheet("")
        self.label2.setText(f"Отпущена кнопка мыши: {event.button()}")

    def wheelEvent(self, event):
        self.widget1.setStyleSheet("")
        self.widget2.setStyleSheet("")
        self.widget3.setStyleSheet("background-color: purple;")
        self.label3.setText(f"Колесо прокручено: {event.angleDelta().y()}")

    def mouseMoveEvent(self, event):
        self.label4.setText("Мышь перемещается")
        self.label5.setText(f"x: {event.pos().x()}, y: {event.pos().y()}")
        self.label6.move(event.globalPosition().x(), event.globalPosition().y())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()

    layout = QVBoxLayout()
    layout.addWidget(window.widget1)
    layout.addWidget(window.widget2)
    layout.addWidget(window.widget3)

    widget = QWidget()
    widget.setLayout(layout)
    window.setCentralWidget(widget)

    app.exec()
