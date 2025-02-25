"""Тесты для API постов."""
import pytest
import requests
import time
from jsonschema import validate
from utils.schemas import POSTS_SCHEMA, POST_SCHEMA

class TestPostsAPI:
    """Тесты для эндпоинтов /posts."""

    def test_get_posts_returns_200(self, api_client):
        """Проверка получения списка постов."""
        response = api_client.get_posts()
        assert response.status_code == 200

    def test_get_posts_validates_schema(self, api_client):
        """Проверка схемы ответа для списка постов."""
        response = api_client.get_posts()
        posts = response.json()
        validate(instance=posts, schema=POSTS_SCHEMA)

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_single_post(self, api_client, post_id):
        """Проверка получения отдельного поста."""
        response = api_client.get_post(post_id)
        post = response.json()
        validate(instance=post, schema=POST_SCHEMA)
        assert post["id"] == post_id

    def test_create_post(self, api_client, random_post_data):
        """Проверка создания поста."""
        response = api_client.create_post(random_post_data)
        created_post = response.json()
        assert response.status_code == 201
        validate(instance=created_post, schema=POST_SCHEMA)
        for key, value in random_post_data.items():
            assert created_post[key] == value

    def test_update_post(self, api_client, random_post_data):
        """Проверка обновления поста."""
        response = api_client.update_post(1, random_post_data)
        assert response.status_code == 200
        updated_post = response.json()
        validate(instance=updated_post, schema=POST_SCHEMA)

    def test_delete_post(self, api_client):
        """Проверка удаления поста."""
        response = api_client.delete_post(1)
        assert response.status_code == 200

    def test_api_response_time(self, api_client):
        """Проверка времени ответа API."""
        start_time = time.time()
        api_client.get_posts()
        response_time = time.time() - start_time
        assert response_time < 1.0, f"Время ответа превышает 1 секунду: {response_time}"

    @pytest.mark.parametrize("invalid_id", [-1, 0, 999999])
    def test_get_post_invalid_id(self, api_client, invalid_id):
        """Проверка обработки невалидных ID."""
        with pytest.raises(requests.exceptions.HTTPError):
            api_client.get_post(invalid_id) 