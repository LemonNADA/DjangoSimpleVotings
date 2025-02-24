from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import User
from my_project.my_site.forms import UserCreationForm

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    user_data = User.objects.filter(login = request.user.username).first()

    context = {
        "page_title": "Профиль пользователя",
        "user_name": user_data.name,
        "user_email": user_data.email,
        "user_city": user_data.city,
        "user_login": user_data.login,
        "user_about_oneself": user_data.about_oneself,
    }
    return render(request, "my_profile/profile.html", context)


@login_required
def edit_profile(request: HttpRequest) -> HttpResponse:
    user_data = User.objects.filter(login = request.user.username).first()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.login = request.POST.get("login", form.email)
            form.password = request.POST.get("password", form.password)

            form.save()

        user_data.name = request.POST.get("name", user_data.name)
        user_data.email = request.POST.get("email", user_data.email)
        user_data.city = request.POST.get("city", user_data.city)
        user_data.login = request.POST.get("login", user_data.login)
        user_data.password = request.POST.get("password", user_data.password)
        user_data.about_oneself = request.POST.get("bio", user_data.about_oneself)
        user_data.save()
        return redirect("Profile")

    context = {
        "page_title": "Редактирование профиля",
        "user_name": user_data.name,
        "user_email": user_data.email,
        "user_city": user_data.city,
        "user_login": user_data.login,
        "user_password": user_data.password,
        "user_about_oneself": user_data.about_oneself,
    }
    return render(request, "my_profile/edit_profile.html", context)
