# # # # from PySide6.QtWidgets import (
# # # #     QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit,
# # # #     QListWidget, QSplitter
# # # # )
# # # # from PySide6.QtCore import Qt
# # # # import sys

# # # # class MainWindow(QMainWindow):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #         self.setWindowTitle("Resizable Sidebar Example")
# # # #         self.resize(800, 600)

# # # #         # Main layout
# # # #         main_widget = QWidget()
# # # #         main_layout = QVBoxLayout(main_widget)

# # # #         # Create a horizontal splitter
# # # #         splitter = QSplitter(Qt.Horizontal)

# # # #         # Sidebar (e.g., navigation)
# # # #         sidebar = QListWidget()
# # # #         sidebar.addItems(["Home", "Settings", "About"])

# # # #         # Main content
# # # #         content = QTextEdit()
# # # #         content.setPlainText("Main content area")

# # # #         # Add widgets to splitter
# # # #         splitter.addWidget(sidebar)
# # # #         splitter.addWidget(content)

# # # #         # Optionally set initial sizes
# # # #         splitter.setSizes([200, 600])

# # # #         main_layout.addWidget(splitter)
# # # #         self.setCentralWidget(main_widget)

# # # # if __name__ == "__main__":
# # # #     app = QApplication(sys.argv)
# # # #     window = MainWindow()
# # # #     window.show()
# # # #     sys.exit(app.exec())



# # # from PySide6.QtWidgets import (
# # #     QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QLabel
# # # )
# # # from PySide6.QtCore import (
# # #     QPropertyAnimation, QEasingCurve, QRect, QParallelAnimationGroup, Qt
# # # )

# # # class SlideStack(QStackedWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.animation_duration = 400
# # #         self._anim_group = None

# # #     def slide_to_index(self, next_index):
# # #         if next_index == self.currentIndex():
# # #             return

# # #         current_index = self.currentIndex()
# # #         current_widget = self.currentWidget()
# # #         next_widget = self.widget(next_index)

# # #         width = self.frameRect().width()
# # #         height = self.frameRect().height()

# # #         # Устанавливаем начальное положение следующего виджета
# # #         next_widget.setGeometry(width, 0, width, height)
# # #         next_widget.show()

# # #         # Анимация текущего виджета — уходит влево
# # #         anim_current = QPropertyAnimation(current_widget, b"geometry")
# # #         anim_current.setDuration(self.animation_duration)
# # #         anim_current.setStartValue(QRect(0, 0, width, height))
# # #         anim_current.setEndValue(QRect(-width, 0, width, height))
# # #         anim_current.setEasingCurve(QEasingCurve.InOutQuad)

# # #         # Анимация следующего виджета — заходит справа
# # #         anim_next = QPropertyAnimation(next_widget, b"geometry")
# # #         anim_next.setDuration(self.animation_duration)
# # #         anim_next.setStartValue(QRect(width, 0, width, height))
# # #         anim_next.setEndValue(QRect(0, 0, width, height))
# # #         anim_next.setEasingCurve(QEasingCurve.InOutQuad)

# # #         # Группируем анимации
# # #         self._anim_group = QParallelAnimationGroup()
# # #         self._anim_group.addAnimation(anim_current)
# # #         self._anim_group.addAnimation(anim_next)

# # #         # После завершения — переключаем экран и сбрасываем геометрию
# # #         def on_finished():
# # #             self.setCurrentIndex(next_index)
# # #             current_widget.setGeometry(0, 0, width, height)
# # #             next_widget.setGeometry(0, 0, width, height)

# # #         self._anim_group.finished.connect(on_finished)
# # #         self._anim_group.start()

# # # class Screen(QWidget):
# # #     def __init__(self, name, go_next=None):
# # #         super().__init__()
# # #         layout = QVBoxLayout()
# # #         label = QLabel(name)
# # #         label.setAlignment(Qt.AlignCenter)
# # #         label.setStyleSheet("font-size: 24px;")
# # #         layout.addWidget(label)
# # #         if go_next:
# # #             btn = QPushButton("Перейти")
# # #             btn.clicked.connect(go_next)
# # #             layout.addWidget(btn)
# # #         self.setLayout(layout)

# # # if __name__ == "__main__":
# # #     app = QApplication([])

# # #     stack = SlideStack()

# # #     screen1 = Screen("Экран 1", lambda: stack.slide_to_index(1))
# # #     screen2 = Screen("Экран 2", lambda: stack.slide_to_index(0))

# # #     stack.addWidget(screen1)
# # #     stack.addWidget(screen2)

# # #     stack.resize(400, 300)
# # #     stack.show()

# # #     app.exec()


# # from PySide6.QtWidgets import (
# #     QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QLabel
# # )
# # from PySide6.QtCore import (
# #     QPropertyAnimation, QEasingCurve, QRect, QParallelAnimationGroup, Qt
# # )

# # class SlideStack(QStackedWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.animation_duration = 1000
# #         self._anim_group = None

# #     def slide_to_index(self, next_index, direction="left"):
# #         if next_index == self.currentIndex():
# #             return

# #         current_index = self.currentIndex()
# #         current_widget = self.currentWidget()
# #         next_widget = self.widget(next_index)

# #         width = self.frameRect().width()
# #         height = self.frameRect().height()

# #         # Определяем направления
# #         offset = width if direction == "left" else -width

# #         # Начальное положение следующего виджета
# #         next_widget.setGeometry(offset, 0, width, height)
# #         next_widget.show()

# #         # Анимация текущего виджета
# #         anim_current = QPropertyAnimation(current_widget, b"geometry")
# #         anim_current.setDuration(self.animation_duration)
# #         anim_current.setStartValue(QRect(0, 0, width, height))
# #         anim_current.setEndValue(QRect(-offset, 0, width, height))
# #         anim_current.setEasingCurve(QEasingCurve.OutInQuart)

# #         # Анимация следующего виджета
# #         anim_next = QPropertyAnimation(next_widget, b"geometry")
# #         anim_next.setDuration(self.animation_duration)
# #         anim_next.setStartValue(QRect(offset, 0, width, height))
# #         anim_next.setEndValue(QRect(0, 0, width, height))
# #         anim_next.setEasingCurve(QEasingCurve.InOutQuad)

# #         self._anim_group = QParallelAnimationGroup()
# #         self._anim_group.addAnimation(anim_current)
# #         self._anim_group.addAnimation(anim_next)

# #         def on_finished():
# #             self.setCurrentIndex(next_index)
# #             current_widget.setGeometry(0, 0, width, height)
# #             next_widget.setGeometry(0, 0, width, height)

# #         self._anim_group.finished.connect(on_finished)
# #         self._anim_group.start()

# # class Screen(QWidget):
# #     def __init__(self, name, go_next=None, go_back=None):
# #         super().__init__()
# #         layout = QVBoxLayout()
# #         label = QLabel(name)
# #         label.setAlignment(Qt.AlignCenter)
# #         label.setStyleSheet("font-size: 24px;")
# #         layout.addWidget(label)

# #         if go_next:
# #             btn_next = QPushButton("Перейти вперёд →")
# #             btn_next.clicked.connect(go_next)
# #             layout.addWidget(btn_next)

# #         if go_back:
# #             btn_back = QPushButton("← Назад")
# #             btn_back.clicked.connect(go_back)
# #             layout.addWidget(btn_back)

# #         self.setLayout(layout)

# # if __name__ == "__main__":
# #     app = QApplication([])

# #     stack = SlideStack()

# #     screen1 = Screen("Экран 1", go_next=lambda: stack.slide_to_index(1, direction="left"), )
# #     screen2 = Screen("Экран 2", go_back=lambda: stack.slide_to_index(0, direction="right"), go_next=lambda: stack.slide_to_index(2, direction="left"))
# #     screen3 = Screen("Экран 2", go_back=lambda: stack.slide_to_index(0, direction="right"))

# #     stack.addWidget(screen1)
# #     stack.addWidget(screen2)
# #     stack.addWidget(screen3)


# #     stack.resize(400, 300)
# #     stack.show()

# #     app.exec()



# import cv2

# # Загружаем фото (положи рядом с этим скриптом, например ronaldo.jpg)
# img = cv2.imread("ronaldo.jpg")

# # Уменьшаем размер (если нужно)
# img = cv2.resize(img, (600, 800))

# # Переводим в серый
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Инвертируем
# inverted = cv2.bitwise_not(gray)

# # Немного размываем
# blur = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)

# # Инвертируем снова
# inverted_blur = cv2.bitwise_not(blur)

# # Создаём эффект "карандаша"
# sketch = cv2.divide(gray, inverted_blur, scale=256.0)

# # Показываем
# cv2.imshow("Original", img)
# cv2.imshow("Sketch", sketch)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Замените на ваш токен доступа от Hugging Face
auth_token = "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"

# Инициализация пайплайна
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4").to("cuda" if torch.cuda.is_available() else "cpu")

# Текстовый запрос для генерации изображения
prompt = "A photorealistic image of a Portuguese male footballer with short light hair, athletic build, wearing a blue jersey with a white jersey, studio lighting, 4K resolution"

# Генерация изображения
image = pipe(prompt).images[0]

# Сохранение изображения
image.save("ronaldo_style_portrait.png")
