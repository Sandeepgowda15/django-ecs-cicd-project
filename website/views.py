from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "website/home.html")


def health(request):
    return JsonResponse(
        {
            "status": "healthy",
            "application": "django-ecs-cicd-project",
        }
    )
