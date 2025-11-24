from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from gui.character_card import CharacterTab
from gui.game_widget import GameTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Каталог та Гра")
        self.setGeometry(100, 100, 800, 600)
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        self.character_tab = CharacterTab()
        self.game_tab = GameTab()
        
        self.tabs.addTab(self.character_tab, "Каталог персонажів")
        self.tabs.addTab(self.game_tab, "Текстова гра")
