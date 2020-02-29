from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomePage(View):
    def get(self, request):
        tables = [1, 2,
                  3, 4,
                  5, 6]
        return render(request, 'core/index.html', context={'tables': tables})


class Table(View):
    def get(self, request, table_id):
        return render(request, 'core/table.html', context={'table_id': table_id})


class PageNotFound(View):
    def get(self, request):
        return render(request, 'core/not_found.html', context={})
