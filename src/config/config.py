"""Конфигурационный файл с настройками проекта."""

class Config:
    """Класс с конфигурационными параметрами."""
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    TIMEOUT = 10  # секунды
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    } 