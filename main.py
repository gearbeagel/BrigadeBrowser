import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.showMaximized()
        self.setWindowIcon(QIcon('icons/icon.ico'))

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ccc;
                top: -1px;
            }
            QTabBar::tab {
                background: #f8f9fa;
                border: 1px solid #ddd;
                border-bottom: none;
                padding: 5px 10px;
                min-width: 100px;
                font-family: Roboto, sans-serif;
            }
            QTabBar::tab:selected {
                background: #ffffff;
                border-bottom: 1px solid #ffffff;
            }
            QTabBar::tab:hover {
                background: #e9ecef;
            }
        """)
        layout.addWidget(self.tabs)

        # Toolbar
        self.navbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.navbar)
        self.navbar.setStyleSheet("""
            QToolBar {
                background-color: #f8f9fa;
                spacing: 10px;
                font-family: Roboto, sans-serif;
                border: none;
            }
            QToolButton {
                background-color: #f8f9fa;
                border: none;
                padding: 5px;
                margin: 5px;
            }
            QToolButton:hover {
                background-color: #e9ecef;
            }
        """)

        # Toolbar buttons
        back_btn = QAction(QIcon('icons/arrow-left.svg'), 'Back', self)
        back_btn.triggered.connect(self.navigate_back)
        self.navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('icons/arrow-right.svg'), 'Forward', self)
        forward_btn.triggered.connect(self.navigate_forward)
        self.navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('icons/arrow-clockwise.svg'), 'Reload', self)
        reload_btn.triggered.connect(self.reload_page)
        self.navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('icons/house.svg'), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        self.navbar.addAction(home_btn)

        new_tab_btn = QAction(QIcon('icons/plus-circle.svg'), 'New Tab', self)
        new_tab_btn.triggered.connect(
            lambda: self.add_new_tab(QUrl.fromLocalFile(QDir.current().filePath('homepage.html')), "Homepage"))
        self.navbar.addAction(new_tab_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                padding: 5px;
                border-radius: 5px;
                margin: 5px;
            }
        """)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.url_bar)

        # Tab change event
        self.tabs.currentChanged.connect(self.update_url_bar)

        # Add initial tab with homepage
        self.add_new_tab(QUrl.fromLocalFile(QDir.current().filePath('homepage.html')), "Homepage")

    def add_new_tab(self, qurl=QUrl.fromLocalFile(QDir.current().filePath('homepage.html')), label="Homepage"):
        if not isinstance(qurl, QUrl):
            print(f"Error: Expected QUrl, got {type(qurl)}")
            return

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(self.update_url_bar)

    def close_current_tab(self, index):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(index)

    def navigate_home(self):
        homepage_path = QDir.current().filePath('homepage.html')
        self.tabs.currentWidget().setUrl(QUrl.fromLocalFile(homepage_path))

    def navigate_to_url(self):
        qurl = QUrl(self.url_bar.text())
        if not qurl.isValid():
            qurl = QUrl("http://" + self.url_bar.text())
        self.tabs.currentWidget().setUrl(qurl)

    def navigate_back(self):
        self.tabs.currentWidget().back()

    def navigate_forward(self):
        self.tabs.currentWidget().forward()

    def reload_page(self):
        self.tabs.currentWidget().reload()

    def update_url_bar(self, q):
        current_url = self.tabs.currentWidget().url()
        url_string = current_url.toString()
        homepage_url = QUrl.fromLocalFile(QDir.current().filePath('homepage.html')).toString()
        if url_string == homepage_url:
            self.url_bar.clear()
        else:
            self.url_bar.setText(url_string)
        self.url_bar.setCursorPosition(0)


app = QApplication(sys.argv)
QApplication.setApplicationName('Brigade Browser')
window = MainWindow()
window.show()
app.exec_()
