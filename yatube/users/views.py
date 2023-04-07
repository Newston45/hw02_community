from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ContactForm


# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:profile')
    template_name = 'users/signup.html'


def logout_view(request):
    logout(request)
    return redirect('/logout/')


def user_contact(request):
    # Создаём объект формы
    form = ContactForm()

    # И в словаре контекста передаём эту форму в HTML-шаблон
    return render(request, 'users/contact.html', {'form': form})
