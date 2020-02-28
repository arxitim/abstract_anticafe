from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomePage(View):
    def get(self, request):
        return render(request, 'core/index.html', context={'tables': ['table_1', 'table_2',
                                                                      'table_3', 'table_4',
                                                                      'table_5', 'table_6']})


class PageNotFound(View):
    def get(self, request):
        return render(request, 'core/not_found.html', context={})
