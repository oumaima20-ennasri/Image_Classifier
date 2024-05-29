# views.py
from django.shortcuts import render
from .form import UploadImageForm


def prediction(request):
    return render(request, 'prediction.html')

def home(request):
    if request.method == 'POST':

        form = UploadImageForm(request.POST, request.FILES)            
        form = UploadImageForm()
    return render(request, 'prediction.html', {'form': form})
