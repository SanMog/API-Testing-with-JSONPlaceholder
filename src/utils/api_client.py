"""Клиент для работы с API."""
import logging
from typing import Dict, Any
import requests
from requests import Response
from config.config import Config

logger = logging.getLogger(__name__)

class APIClient:
    """Класс для работы с API."""

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS
        self.timeout = Config.TIMEOUT

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Response:
        """Базовый метод для выполнения HTTP-запросов."""
        url = f"{self.base_url}{endpoint}"
        try:
            logger.info(f"Отправка {method} запроса к {url}")
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                timeout=self.timeout,
                **kwargs
            )
            logger.info(f"Получен ответ, статус: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            logger.error(f"Таймаут при запросе к {url}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе к {url}: {str(e)}")
            raise

    def get_posts(self) -> Response:
        """Получение списка всех постов."""
        return self._make_request("GET", "/posts")

    def get_post(self, post_id: int) -> Response:
        """Получение поста по ID."""
        return self._make_request("GET", f"/posts/{post_id}")

    def create_post(self, data: Dict[str, Any]) -> Response:
        """Создание нового поста."""
        return self._make_request("POST", "/posts", json=data)

    def update_post(self, post_id: int, data: Dict[str, Any]) -> Response:
        """Обновление существующего поста."""
        return self._make_request("PUT", f"/posts/{post_id}", json=data)

    def delete_post(self, post_id: int) -> Response:
        """Удаление поста."""
        return self._make_request("DELETE", f"/posts/{post_id}") 