from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Stocks


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


def get_data(request, *args, **kwargs):
    #
    # labels = []
    # while interval <= 5400:
    #     labels.append(interval)
    #     interval += 5
    labels = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80',
              '85', '90']
    chartLabel = "Delta"
    stocks = Stocks.objects.all()
    delta = []
    interval = 0
    while interval <= 1081:
        try:
            delta.append(stocks[interval].us_tech_100 - stocks[interval].us_500)
            interval += 60
        except IndexError:
            break



    data = {
        "labels": labels,
        "chartLabel": chartLabel,
        "chartdata": delta,
    }

    return JsonResponse(data) # http response


class SecondGraph(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, time=0):
        labels = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80',
                  '85', '90']
        # interval = 0
        # labels = []
        # while interval <= 5400:
        #     labels.append(interval)
        #     interval += 5

        chartLabel = "m Delta"
        stocks = Stocks.objects.all()
        delta = []
        interval = 0
        while interval <= 1081:
            try:
                delta.append(stocks[interval].us_tech_100 - stocks[interval].us_500)
                delta_now = stocks[interval].us_tech_100 - stocks[interval].us_500
                delta_ago = stocks[int(time / 5)].us_tech_100 - stocks[int(time / 5)].us_500
                slope = (delta_now - delta_ago) / time
                print(delta_now, delta_ago, slope)
                delta.append(slope)
                interval += 60
            except IndexError:
                break

        # for stock in stocks[len(stocks)-1081:]:
        #     delta_now = stock.us_tech_100 - stock.us_500
        #     delta_ago = stocks[int(time / 5)].us_tech_100 - stocks[int(time / 5)].us_500
        #     slope = (delta_now - delta_ago) / time
        #     print(delta_now, delta_ago, slope)
        #     delta.append(slope)

        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": delta,
        }
        return Response(data)
