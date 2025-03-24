import scrapy
from scrapy.exporters import CsvItemExporter

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
            # Получаем название модели
            pre_name = divan.css('span.d-product-information__prename::text').get(default='').strip()
            model_name = divan.xpath('.//span[@class="d-product-information__prename"]/following-sibling::text()').get(default='').strip()

            # Получаем цвет
            color = divan.css('div.tovs__item__colors::text').get(default='').strip()

            # Получаем цену (убираем ₽ и пробелы)
            price = divan.css('div.d-product-information__price.information__price__disc::text').get(default='').strip()
            price = ''.join(filter(str.isdigit, price))  # Убираем всё, кроме цифр

            # Полное название: если model_name пустой, используем pre_name
            full_name = model_name if model_name else pre_name

            yield {
                'name': full_name,
                'color': color,
                'price': price
            }

