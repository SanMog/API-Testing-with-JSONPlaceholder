"""Клиент для работы с API."""
import logging
from typing import Dict, Any, Optional

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
        """Выполняет HTTP-запрос и обрабатывает исключения."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                timeout=self.timeout,
                **kwargs
            )
            logger.info(f"Request: {method} {url}")
            logger.info(f"Response status: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            logger.error(f"Timeout error for {url}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def get_posts(self) -> Response:
        """Получает список всех постов."""
        return self._make_request("GET", "/posts")

    def get_post(self, post_id: int) -> Response:
        """Получает пост по ID."""
        return self._make_request("GET", f"/posts/{post_id}")

    def create_post(self, data: Dict[str, Any]) -> Response:
        """Создает новый пост."""
        return self._make_request("POST", "/posts", json=data) 