# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from find.forms import RegistrationForm, LoginForm
import json
from find.models import UserKey


@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            request_data = json.loads(request.body)
        except ValueError:
            message = "Malformed JSON"
            return JsonResponse({'status': 0, 'message': message})

        try:
            form = RegistrationForm(data=request_data)
            if form.is_valid():
                form.save()
                return JsonResponse({"status": 1})
            else:
                return JsonResponse({"status": 0, "errors": form.errors})
        except:
            return JsonResponse({"status":0, "fail": "Kayıt işlemi sırasında bir hata oluştu."})

    return JsonResponse({"status": 0, "message": "Request rejected"})

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            request_data = json.loads(request.body)
        except ValueError:
            message = "Malformed JSON"
            return JsonResponse({'status': 0, 'message': message})

        try:
            form = LoginForm(data=request_data)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                username = cleaned_data["username"]
                password = cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        key = UserKey.objects.create(user=user)
                        return JsonResponse({"status": 1, "key": key.key})
            else:
                return JsonResponse({"status": 0, "errors": form.errors})
        except:
            return JsonResponse({"status":0, "fail": "Giriş işlemi sırasında bir hata oluştu."})

    return JsonResponse({"status": 0, "message": "Request rejected"})