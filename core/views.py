from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomePage(View):
    def get(self, request):
        return render(request, 'core/index.html', context={})


class PageNotFound(View):
    def get(self, request):
        return render(request, 'core/not_found.html', context={})
