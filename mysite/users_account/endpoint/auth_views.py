from django.shortcuts import render


def google_login(request):
    return render(request, 'auth/google_auth.html')