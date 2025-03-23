# Nordclan Test Automation Framework

## Описание
Автоматизированный фреймворк для тестирования веб-сайта Nordclan. Фреймворк построен на Python с использованием современных инструментов и практик тестирования.

## Технологии
- Python 3.9+
- Pytest
- Selene (UI тестирование)
- Allure Reports
- Selenium WebDriver
- Poetry (управление зависимостями)

## Структура проекта
```
nordclan_test/
├── pages/                    # Page Objects
│   ├── __init__.py
│   ├── main_page.py         # Главная страница
│   └── vacancies_page.py    # Страница вакансий
├── tests/                   # Тесты
│   ├── __init__.py
│   ├── conftest.py         # Конфигурация pytest
│   └── ui/                 # UI тесты
│       ├── __init__.py
│       └── test_main_page.py
├── utils/                  # Утилиты
│   ├── __init__.py
│   └── attach.py          # Функции для Allure
├── .env                   # Переменные окружения
├── pyproject.toml         # Зависимости проекта
└── pytest.ini            # Конфигурация pytest
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/YarikSec/nordclan-test.git
cd nordclan-test
```

2. Установите Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Установите зависимости:
```bash
poetry install
```

4. Создайте файл `.env` и добавьте необходимые переменные окружения:
```env
LOGIN=your_login
PASSWORD=your_password
BASE_URL=https://nordclan.com
```

## Запуск тестов

### Запуск всех тестов
```bash
poetry run pytest
```

### Запуск конкретного теста
```bash
poetry run pytest tests/ui/test_main_page.py -v
```

### Запуск тестов с генерацией Allure отчета
```bash
poetry run pytest --alluredir=./allure-results
poetry run allure serve ./allure-results
```

## Тест-кейсы

### Главная страница
- [x] Проверка основных элементов страницы
- [x] Проверка формы обратной связи
- [x] Проверка ссылки на вакансии
- [x] Проверка логотипа
- [x] Проверка навигации по логотипу

### Страница вакансий
- [x] Проверка основных элементов страницы
- [ ] Проверка фильтрации вакансий
- [ ] Проверка поиска вакансий
- [ ] Проверка пагинации

## Особенности фреймворка

### Page Object Pattern
- Использование паттерна Page Object для инкапсуляции селекторов и действий
- Методы для проверки видимости элементов
- Методы для взаимодействия с элементами

### Allure Reporting
- Подробные шаги тестов
- Скриншоты при падении тестов
- Логи браузера
- HTML-снапшоты страниц
- Видео выполнения тестов

### Конфигурация
- Поддержка разных окружений через переменные окружения
- Настройка браузера через Selenoid
- Возможность запуска в headless режиме

## Разработка

### Добавление нового теста
1. Создайте Page Object для новой страницы в директории `pages/`
2. Добавьте селекторы и методы в Page Object
3. Создайте тест в директории `tests/ui/`
4. Используйте фикстуры из `conftest.py`