from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from . import models, forms


class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'work_age/register.html'
    success_url = reverse_lazy('work_age:login')


class AuthloginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'work_age/login.html'

    def get_success_url(self):
        # Убедитесь, что этот маршрут правильный
        return reverse_lazy('work_age:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('work_age:login')


@method_decorator(cache_page(60 * 15), name='dispatch')  # Кэшируем на 15 минут
class UsersListView(ListView):
    template_name = 'work_age/user_list.html'
    context_object_name = 'person'
    model = models.CustomUser

    def get_queryset(self):
        # Этот запрос будет кэшироваться, но также следите за его актуальностью
        return models.CustomUser.objects.all()

