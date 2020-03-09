from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate

from core.forms import RegistrationForm


class HomePage(View):
    def get(self, request):
        tables = [1, 2,
                  3, 4,
                  5, 6]
        return render(request, 'core/index.html', context={'tables': tables})


class Table(View):
    def get(self, request, table_id):
        return render(request, 'core/table.html', context={'table_id': table_id})


class MyRegisterFormView(FormView):
    template_name = "registration/register.html"

    def post(self, request, *args, **kwargs):
        context = {}
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('homePage')
        else:
            context['form'] = form
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        context = {}
        form = RegistrationForm()
        context['form'] = form
        return render(request, self.template_name, context)


class PageNotFound(View):
    def get(self, request):
        return render(request, 'core/not_found.html', context={})
