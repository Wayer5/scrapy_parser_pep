import csv
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = {}

    def process_item(self, item, spider):
        status = item.get('status')
        if status in self.status_count:
            self.status_count[status] += 1
        else:
            self.status_count[status] = 1
        return item

    def close_spider(self, spider):
        # Генерация имени файлов с текущей датой и временем.
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

        # Создание файла с результатами по статусам
        path = BASE_DIR / f'results/status_summary_{now}.csv'
        with open(path, mode='w', encoding='utf-8') as summary_file:
            writer = csv.writer(summary_file)
            writer.writerow(['Статус', 'Количество'])
            total_count = 0
            for status, count in self.status_count.items():
                writer.writerow([status, count])
                total_count += count
            writer.writerow(['Total', total_count])
