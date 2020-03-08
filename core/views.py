from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


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
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "../../"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class PageNotFound(View):
    def get(self, request):
        return render(request, 'core/not_found.html', context={})
