from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
import os
import json

class GameTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        self.layout.addWidget(self.text_output)

        self.load_button = QPushButton("Завантажити гру")
        self.save_button = QPushButton("Зберегти гру")
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.save_button)

        self.load_button.clicked.connect(self.load_game)
        self.save_button.clicked.connect(self.save_game)

    def load_game(self):
        file_path = os.path.join("data", "saves.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                saves = json.load(f)
            self.text_output.append("Гру завантажено")
        else:
            self.text_output.append("Файл збережень не знайдено")

    def save_game(self):
        file_path = os.path.join("data", "saves.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({"status": "example"}, f, ensure_ascii=False, indent=4)
        self.text_output.append("Гру збережено")
