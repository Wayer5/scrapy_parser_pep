# scrapy_parser_pep
Парсер PEP с использованием Scrapy
Этот проект демонстрирует, как скрапить данные с веб-сайта Python Enhancement Proposals (PEP) с помощью фреймворка Scrapy.

Установка
Склонируйте репозиторий:

bash
Копировать код
git clone https://github.com/ваше_имя_пользователя/pep_parser.git
cd pep_parser
Создайте и активируйте виртуальное окружение (опционально, но рекомендуется):

bash
Копировать код
python -m venv venv
# На Windows
venv\Scripts\activate
# На macOS/Linux
source venv/bin/activate
Установите зависимости:

bash
Копировать код
pip install -r requirements.txt
Использование
Запуск паука
Для запуска паука и скрапинга данных с сайта PEP выполните:

bash
Копировать код
scrapy crawl pep
Вывод
Скрапленные данные будут сохранены в CSV файлы в директории results:

results/pep_<timestamp>.csv: Содержит детальную информацию о каждом PEP.
results/status_summary_<timestamp>.csv: Содержит сводную информацию о статусе PEP.
Структура проекта
pep_parse/: Основной код проекта.
spiders/: Содержит пауки Scrapy для скрапинга данных PEP.
items.py: Определяет элементы Scrapy для данных PEP.
pipelines.py: Определяет конвейеры Scrapy для обработки скрапленных данных.
settings.py: Содержит настройки Scrapy, включая конфигурацию экспорта данных.
results/: Директория для сохранения скрапленных данных в виде CSV файлов.
tests/: Директория для скриптов тестирования.