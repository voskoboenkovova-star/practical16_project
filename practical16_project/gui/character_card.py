from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
import json
import os

class CharacterTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.load_characters()

    def load_characters(self):
        file_path = os.path.join("data", "characters.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                characters = json.load(f)
            for char in characters:
                item = QListWidgetItem(f"{char['name']} - {char.get('info', '')}")
                self.list_widget.addItem(item)
        else:
            self.list_widget.addItem("Поки немає персонажів")
