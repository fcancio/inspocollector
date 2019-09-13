from django.shortcuts import render
from .models import Inspiration

# Create home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def inspirations_index(request):
    inspirations = Inspiration.objects.all()
    return render(request, 'inspirations/index.html', {'inspirations': inspirations })

def inspirations_detail(request, inspiration_id):
    inspiration = Inspiration.objects.get(id=inspiration_id)
    return render(request, 'inspirations/detail.html', { 'inspiration': inspiration })
    