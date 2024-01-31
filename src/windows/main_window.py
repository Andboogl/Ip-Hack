"""Application main window"""


from PyQt6.QtWidgets import QMainWindow, QMessageBox
from design import MainWindowDesign
from ip_info import get_info_about_ip
from .ip_info_window import IpInfoWindow


def show_message(window: QMainWindow, text: str, details: str = None) -> None:
    """Show message"""
    msg = QMessageBox(window)
    msg.setText(text)

    if details:
        msg.setDetailedText(details)

    msg.exec()


class MainWindow(QMainWindow):
    """Application main window"""
    def __init__(self, parent: None = None) -> None:
        super().__init__(parent)

        # Loading design
        self.design = MainWindowDesign()
        self.design.setupUi(self)

        self.design.get_info.clicked.connect(self.get_info)

    def get_info(self) -> None:
        """Get info about ip"""
        user_ip = self.design.ip.text().strip()

        try:
            data = get_info_about_ip(user_ip)
            self.__ip_info_window = IpInfoWindow(data)
            self.__ip_info_window.show()

        except ValueError:
            show_message(self, 'Enter all data')

        except Exception as error:
            show_message(
                self,
                'Error when retrieving IP data. '\
                'Maybe the server is unavailable or you '\
                'are not connected to the Internet', str(error))
