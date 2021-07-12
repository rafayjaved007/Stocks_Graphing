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
    interval = 0
    labels = []
    while interval <= 5400:
        labels.append('')
        interval += 5

    s_interval = 0
    m_interval = 0
    while s_interval <= 1081:
        labels[s_interval] = m_interval
        s_interval += 60
        m_interval += 5
    # labels = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80',
    #           '85', '90']
    chartLabel = "Delta"
    stocks = Stocks.objects.all()
    if len(stocks) >= 1080:
        stocks = stocks[len(stocks) - 1080:]

    # stocks.reverse()

    delta = []
    interval = 0
    while interval <= 1080:
        try:
            delta.append(stocks[interval].us_tech_100 - stocks[interval].us_500)
            interval += 1
        except IndexError:
            break

    if len(delta) < 1080:
        dummy = 0
        d_list = []
        while dummy < 1080-len(delta):
            d_list.append(0)
            dummy += 1

        delta = d_list + delta

    data = {
        "v1": stocks[len(stocks)-1].us_tech_100,
        "v2": stocks[len(stocks)-1].us_500,
        "delta": stocks[len(stocks)-1].us_tech_100 - stocks[len(stocks)-1].us_500,
        "labels": labels[::-1],
        "chartLabel": chartLabel,
        "chartdata": delta,
    }

    return JsonResponse(data) # http response


class SecondGraph(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, time=0):
        intervals = 0
        labels = []
        while intervals <= 5400:
            labels.append('')
            intervals += 5

        s_interval = 0
        m_interval = 0
        while s_interval <= 1081:
            labels[s_interval] = m_interval
            s_interval += 60
            m_interval += 5

        chartLabel = "m Delta"
        stocks = Stocks.objects.all()
        if len(stocks) >= 1080:
            stocks = stocks[len(stocks) - 1080:]

        stocks.reverse()
        delta = []
        interval = 0
        while interval <= 1080:
            try:
                # delta.append(stocks[interval].us_tech_100 - stocks[interval].us_500)
                delta_now = stocks[interval].us_tech_100 - stocks[interval].us_500
                delta_ago = stocks[int(time / 5)].us_tech_100 - stocks[int(time / 5)].us_500
                slope = (delta_now - delta_ago) / time
                delta.append(slope)
                interval += 1
            except IndexError:
                break

        if len(delta) < 1080:
            dummy = 0
            d_list = []
            while dummy < 1080 - len(delta):
                d_list.append(0)
                dummy += 1

            delta = d_list + delta

        data = {
            "mdelta": stocks[int(time / 5)].us_tech_100 - stocks[int(time / 5)].us_500,
            "labels": labels[::-1],
            "chartLabel": chartLabel,
            "chartdata": delta,
        }
        return Response(data)
