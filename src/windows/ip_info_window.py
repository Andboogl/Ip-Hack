"""Ip info window"""


from PyQt6.QtWidgets import QMainWindow
from design import IpInfoWindowDesign


class IpInfoWindow(QMainWindow):
    """Ip info window"""
    def __init__(self, ip_info: dict) -> None:
        super().__init__(None)

        # Loading design
        self.design = IpInfoWindowDesign()
        self.design.setupUi(self)

        # Loading info about ip
        self.design.title.setText(f'Info for {ip_info['query']}')

        text = ''

        for key in ip_info.items():
            text += f'{key[0].capitalize()}: {key[1]}\n'

        self.design.info.setText(text)
