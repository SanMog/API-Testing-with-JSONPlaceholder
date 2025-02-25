"""Схемы для валидации ответов API."""
from typing import TypedDict

class Post(TypedDict):
    """Типизированный словарь для структуры поста."""
    id: int
    title: str
    body: str
    userId: int

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"}
    },
    "required": ["id", "title", "body", "userId"]
}

POSTS_SCHEMA = {
    "type": "array",
    "items": POST_SCHEMA
} 