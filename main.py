import sys

from matplotlib.patches import FancyArrow
import validators
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))

        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        navbar.setMovable(False)
        navbar.addSeparator()
        self.addToolBar(navbar)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        next_btn = QAction('Next', self)
        next_btn.triggered.connect(self.browser.forward)
        navbar.addAction(next_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        
        if not url.startswith('https://') or url.startswith('http://'):
            url = f'https://{url}'

        if not validators.url(url):
            url = url.replace(' ', '+')
            url = url.replace('https://', '')
            url = f'https://google.com/search?q={url}'

        self.browser.setUrl(QUrl(url))
        self.url_bar.clearFocus()

    def update_url(self, changed_url):
        self.url_bar.setText(changed_url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('LightWeight Browser')

window = MainWindow()
app.exec_()