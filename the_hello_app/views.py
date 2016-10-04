from django.shortcuts import render
from datetime import datetime


def say_hello(request):

    message = "Hello There!!"

    return render(request, "index.html", {'the_message': message})


def get_the_time(request):

    now = datetime.now()

    return render(request, "time.html", {'the_time': now})

