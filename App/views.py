from django.http import HttpResponse
from django.shortcuts import render
from App import models

# Create your views here.
def home(request):
    urser1 = models.User(username='谢一', passwrod=123456, info='喜爱书法', hobby='泡妞')
    urser1.save()
    uu = models.User.objects.all()
    return render(request, 'index.html',locals())