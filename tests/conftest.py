"""Конфигурация тестов и фикстуры."""
import logging
import pytest
import os
import sys
from faker import Faker

# Добавляем корневую директорию проекта в PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(project_root, "src"))

from utils.api_client import APIClient

# Настройка логирования
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def api_client():
    """Фикстура для создания экземпляра API клиента."""
    return APIClient()

@pytest.fixture
def random_post_data():
    """Фикстура с случайными данными для поста."""
    fake = Faker()
    return {
        "title": fake.sentence(),
        "body": fake.text(),
        "userId": fake.random_int(min=1, max=10)
    }

@pytest.fixture
def new_post_data():
    """Фикстура с тестовыми данными для создания поста."""
    return {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    } 