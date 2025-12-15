from django.shortcuts import render

def home(request):
    return render(request,'main/index.html')
def whisper(request):
    return render(request,'main/whisper.html')
def animals(request):
    return render(request, 'main/animals.html')
def birds(request):
    return render(request, 'main/birds.html')
def insects(request):
    return render(request, 'main/insects.html')



