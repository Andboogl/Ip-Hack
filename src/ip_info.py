"""Module for obtaining IP information"""


import requests


def get_info_about_ip(ip: str) -> dict:
    """Get IP information"""
    # Checking for valid data
    if not isinstance(ip, str) or not ip.strip():
        raise ValueError('IP must be a string and could not be empty')

    # Making request to server
    responce: dict = requests.get(
        url=f'http://www.ip-api.com/json/{ip}').json()

    return responce
