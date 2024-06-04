from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.db import IntegrityError
import json


from django.http import HttpResponseRedirect, JsonResponse
from .models import *
# Create your views here.

@csrf_exempt
@login_required
def main(request):
    # user = User()
    if request.method == "POST":
        print(request.body)

        data  = json.loads(request.body)
  
        history = History(date=data['date'], start=data['start'], amount=data['amount'], user=request.user, end=data['end'])
        history.save()
        return render(request, 'time_management/main.html')

    else:
        return render(request, 'time_management/main.html')
        

def history(request):
    day = 0
    hour = 0
    min = 0 
    sec = 0 
    money = 0 
    archive = History.objects.filter(user=request.user)
    total_time = History.objects.values_list("amount")
    for time_length in total_time:
        measurement = str(time_length)
        unit = measurement[2:10].split(':')
        hour += int(unit[0])
        min += int(unit[1])
        sec += int(unit[2])
        if min > 59 or sec > 59:
            hour += min // 60
            money = hour * 300
            day += hour // 24
            min += sec // 60
            hour = hour % 24
            min = min % 60
            sec = sec % 60
    total_time = f"{day} д. | {hour} час | {min} мин | {sec} сек"
    return render(request, 'time_management/history.html', {"archive":archive, "total_time": total_time, "money": money})

def logout_fun(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

# Яркость
# def light(request):
#     light = Light()
#     print("i")
#     data = json.loads(request.body)
#     if data.get("light") is not None:
#         light.light = data["light"]
#     else:
#         light.light = data["light"]
#     light.save()

def login_fun(request):
    if request.method == 'POST':
        username = request.POST['name']
        print(request.POST['name'])
        password = request.POST['password']
        employee = authenticate(request, username=username, password=password)
        
        if employee != None:
            login(request, employee)
            return HttpResponseRedirect(reverse("main"))
        else:
            return render(request, 'time_management/login.html', {"problem":"Неправильный логин или пороль. Повторите попытку.."})
    else:
        return render(request, 'time_management/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        password_check = request.POST["password_check"]
        if password == password_check:
            try:
                employee = User.objects.create_user(username, email, password)
                # user = User.objects.create_user(username, email, password)

                employee.save()
            except IntegrityError:
                return render(request, 'time_management/register.html', {"problem": "Вы уже зарегистрироавны..."})

            login(request, employee)
            return HttpResponseRedirect(reverse("main"))
        else:
            return render(request, 'time_management/register.html', {"problem": "Пароли не совпадают. Повтортите попытку.."})
        
    # else:
    return render(request, 'time_management/register.html')