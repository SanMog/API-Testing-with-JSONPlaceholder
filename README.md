# API Testing Framework

## Описание проекта
Фреймворк для автоматизированного тестирования REST API с использованием Python и pytest. 
Демонстрирует современные практики тестирования на примере публичного API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## Стек технологий
- Python 3.8+
- pytest (фреймворк тестирования)
- requests (HTTP-клиент)
- jsonschema (валидация JSON-схем)
- pytest-html (генерация HTML-отчетов)
- pytest-cov (анализ покрытия кода)
- Faker (генерация тестовых данных)

## Структура проекта
api_testing_project/
├── src/ # Исходный код
│ ├── utils/
│ │ ├── api_client.py # API клиент
│ │ ├── schemas.py # Схемы валидации
│ ├── config/
│ │ ├── config.py # Конфигурация
├── tests/
│ ├── test_posts_api.py # Тесты API
├── requirements.txt
├── setup.py


## Установка и настройка

1. Клонировать репозиторий:
bash
git clone <repository-url>
cd api-testing-project

2. Создать виртуальное окружение:
bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3. Установить зависимости:
bash
pip install -e .


## Запуск тестов

### Запуск всех тестов:
bash
pytest tests/ -v

### Запуск с генерацией HTML-отчета:
bash
pytest tests/ -v --html=report.html

### Запуск с отчетом о покрытии:
bash
pytest tests/ -v --cov=src --cov-report=html


## Функциональность тестов

### Позитивные сценарии:
- Получение списка всех постов
- Получение конкретного поста по ID
- Создание нового поста
- Валидация схемы ответа

### Негативные сценарии:
- Обработка невалидных ID
- Проверка граничных значений

## Отчетность
- HTML-отчеты о прохождении тестов
- Отчеты о покрытии кода
- Подробное логирование запросов и ответов

## Лучшие практики
- Модульная структура
- Паттерн Page Object для API
- Валидация схем ответов
- Параметризованные тесты
- Обработка исключений
- Подробное логирование

## Поддержка
При возникновении вопросов или проблем создавайте issue в репозитории проекта.