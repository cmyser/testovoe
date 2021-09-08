from django.shortcuts import render
from .models import *



def index(request):
    users = User.objects.all()
    
    print(request)       
 
    data = { "user": users}
    return render(request, "show.html", context=data)



    

