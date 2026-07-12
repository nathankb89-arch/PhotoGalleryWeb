from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileUpdateForm, RegisterForm
from .models import Photo


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created successfully.")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})


def home(request):
    tag = request.GET.get("tag", "")
    photos = Photo.objects.all().order_by("-created_at")

    if tag:
        photos = photos.filter(tags__icontains=tag)

    return render(request, "home.html", {"photos": photos, "tag": tag})


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "like":
            photo.likes += 1
            photo.save()
            messages.success(request, "You liked this photo.")
        elif action == "dislike":
            photo.dislikes += 1
            photo.save()
            messages.success(request, "You disliked this photo.")

        return redirect("photo_detail", photo_id=photo.id)

    return render(request, "photo_detail.html", {"photo": photo})


@login_required
def profile_view(request):
    return render(request, "profile.html", {"user": request.user})


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "profile_edit.html", {"form": form})