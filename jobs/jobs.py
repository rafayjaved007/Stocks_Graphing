from django.utils import timezone
from lxml import html
from django.conf import settings
import requests
from main.models import Stocks


def scrape_schedule():
    try:
        res = requests.get('https://www.investing.com/indices/indices-futures')
        source = html.fromstring(res.content)

        us_500 = source.xpath('//tbody[1]/tr[2]/td[8]/text()')[0].replace('%', '')
        us_tech_100 = source.xpath('//tbody[1]/tr[3]/td[8]/text()')[0].replace('%', '')

        stock = Stocks.objects.create(us_500=float(us_500), us_tech_100=float(us_tech_100))
        stock.save()

        # Deleting stocks older than 60 minutes
        ninety_minutes_ago = timezone.now() - timezone.timedelta(minutes=100)
        expired_stocks = Stocks.objects.filter(
            timestamp__lte=ninety_minutes_ago
        )
        expired_stocks.delete()

    except Exception as e:
        print(f'Error : {e}')
