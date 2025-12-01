from django.shortcuts import render

def home(request):
    return render(request,'map_image.html')

def mount(request):
    return render(request,'Mount.html')

def flight(request):
    return render(request,'Flight.html')

def shop(request):
    return render(request,'Shop.html')

def church(request):
    return render(request,'Church.html')

def beach(request):
    return render(request,'Beach.html')


