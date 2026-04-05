#  Инструкция по запуску автотестов

Данный проект содержит автоматизированные тесты на Python с использованием **Selenium 4.41.0** и **Pytest**.

## Требования
* **Python 3.10** или выше.
* Браузер **Google Chrome** (актуальной версии).

* На моём устройстве тестируемый сайт открывался только при запуске vpn

## Настройка окружения

### 1. Клонирование проекта
Скачайте проект на локальный компьютер:
```bash
git clone https://github.com/Ivarum/avito_test_task
cd <локальный путь>\avito_test_task
```
### 2. Создание виртуального окружения (Venv)
Это изолирует зависимости проекта от системного Python:

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```
macOS / Linux:
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Установка зависимостей
Установите все необходимые библиотеки одной командой:
```bash
pip install -r requirements.txt
```
### 4. Запуск тестов

* Команда для тестов обычного браузера, главная страница:
```
pytest -v --tb=line -m desktop_ver .\test_main_page.py
```
* Команда для тестов мобильного браузера, главная страница:
```
pytest -v --tb=line --on_mobile=on -m mobile .\test_main_page_mobile.py
```
* Команда для тестов обычного браузера, страница статистики:
```
pytest -v --tb=line .\test_stat_page.py
```