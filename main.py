from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit,
    QListWidget, QSplitter
)
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resizable Sidebar Example")
        self.resize(800, 600)

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Create a horizontal splitter
        splitter = QSplitter(Qt.Horizontal)

        # Sidebar (e.g., navigation)
        sidebar = QListWidget()
        sidebar.addItems(["Home", "Settings", "About"])

        # Main content
        content = QTextEdit()
        content.setPlainText("Main content area")

        # Add widgets to splitter
        splitter.addWidget(sidebar)
        splitter.addWidget(content)

        # Optionally set initial sizes
        splitter.setSizes([200, 600])

        main_layout.addWidget(splitter)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
