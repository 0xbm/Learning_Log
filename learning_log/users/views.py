from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Rejestracja nowego uzytkownika"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Zalogowanie usera i przekierowanie go na glowna strone
            login(request, new_user)
            return redirect("learning_logs:index")

    # Wyswietlenie pustego formularza
    context = {"form": form}
    return render(request, "registration/register.html", context)
