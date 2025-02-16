from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def profile(request):
    user_data = get_object_or_404(User, login=request.user.username)

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
def edit_profile(request):
    user_data = get_object_or_404(User, login=request.user.username)

    if request.method == "POST":
        user_data.name = request.POST.get("name", user_data.name)
        user_data.email = request.POST.get("email", user_data.email)
        user_data.city = request.POST.get("city", user_data.city)
        user_data.login = request.POST.get("login", user_data.login)
        user_data.about_oneself = request.POST.get("bio", user_data.about_oneself)
        user_data.save()
        return redirect("Profile")

    context = {
        "page_title": "Редактирование профиля",
        "user_name": user_data.name,
        "user_email": user_data.email,
        "user_city": user_data.city,
        "user_login": user_data.login,
        "user_about_oneself": user_data.about_oneself,
    }
    return render(request, "my_profile/edit_profile.html", context)


def profile_history(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | int] = {
        "page_title": "История голосов"
        }
    return render(request, "my_profile/profile_history.html", context)
