#  Инструкция по запуску автотестов

Данный проект содержит автоматизированные тесты на Python с использованием **Selenium 4.41.0** и **Pytest**.

## 📋 Требования
* **Python 3.10** или выше.
* Браузер **Google Chrome** (актуальной версии).

## 🛠 Настройка окружения

### 1. Клонирование проекта
Скачайте проект на локальный компьютер:
```bash
git clone <ссылка_на_ваш_репозиторий>
cd <название_папки_проекта>

### 2. Создание виртуального окружения (Venv)
Это изолирует зависимости проекта от системного Python:

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate

### 3. Установка зависимостей
Установите все необходимые библиотеки одной командой:
```bash
pip install -r requirements.txt

### 4. Запуск тестов

*Команда для тестов обычного браузера, главная страница:
pytest -v --tb=line -m desktop_ver .\test_main_page.py
*Команда для тестов мобильного браузера, главная страница:
pytest -v --tb=line --on_mobile=on -m mobile .\test_main_page_mobile.py
*Команда для тестов обычного браузера, страница статистики:
pytest -v --tb=line .\test_stat_page.py