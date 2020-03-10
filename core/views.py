from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate

from core.forms import RegistrationForm, AccountUpdateForm


class HomePage(View):
    template_name = 'core/index.html'

    def get(self, request):
        tables = [1, 2,
                  3, 4,
                  5, 6]
        return render(request, self.template_name, context={'tables': tables})


class Table(View):
    template_name = 'core/table.html'

    def get(self, request, table_id):
        return render(request, self.template_name, context={'table_id': table_id})


class MyRegisterFormView(FormView):
    template_name = 'registration/register.html'

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


class AccountView(FormView):
    template_name = 'core/account.html'

    def post(self, request, *args, **kwargs):
        context = {}
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('homePage')
        else:
            context['account_form'] = form
            return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        context = {}
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

        context['account_form'] = form
        return render(request, self.template_name, context)


class PageNotFound(View):
    template_name = 'core/not_found.html'

    def get(self, request):
        return render(request, self.template_name, context={})
