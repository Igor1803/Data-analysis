import scrapy
import pandas as pd
import matplotlib.pyplot as plt

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divanchik.ru"]
    start_urls = ["https://divanchik.ru/category/pryamye-divany/"]

    # Настройки для красивого экспорта в CSV
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'divan_data.csv',
        'FEED_EXPORT_FIELDS': ['name', 'color', 'price'],  # Порядок колонок
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        divans = response.css('div.product__item')

        for divan in divans:
            pre_name = divan.css('span.d-product-information__prename::text').get(default='').strip()
            model_name = divan.xpath('.//span[@class="d-product-information__prename"]/following-sibling::text()').get(default='').strip()
            color = divan.css('div.tovs__item__colors::text').get(default='').strip()
            price = divan.css('div.d-product-information__price.information__price__disc::text').get(default='').strip()
            price = ''.join(filter(str.isdigit, price))  # Оставляем только цифры

            full_name = model_name if model_name else pre_name

            yield {
                'name': full_name,
                'color': color,
                'price': price
            }

    def closed(self, reason):
        """Вызывается после завершения парсинга. Анализирует цены и строит график."""
        try:
            df = pd.read_csv('divan_data.csv')

            # Преобразуем цены в числа
            df['price'] = pd.to_numeric(df['price'], errors='coerce')

            # Убираем пустые значения
            df = df.dropna(subset=['price'])

            # Считаем среднюю цену
            avg_price = df['price'].mean()
            print(f"📊 Средняя цена дивана: {int(avg_price)} ₽")

            # Строим гистограмму цен
            plt.figure(figsize=(10, 5))
            plt.hist(df['price'], bins=10, color='skyblue', edgecolor='black')
            plt.xlabel("Цена (₽)")
            plt.ylabel("Количество диванов")
            plt.title("Распределение цен на диваны")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.savefig("price_histogram.png")  # Сохраняем гистограмму
            plt.show()

        except Exception as e:
            print(f"⚠️ Ошибка анализа данных: {e}")


