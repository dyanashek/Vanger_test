from django.shortcuts import render
from .models import Slider

def index(request):
    template = 'sliders/index.html'
    images = Slider.objects.filter(shown=True).all()
    slides_to_show = len(images)
    if slides_to_show > 5:
        slides_to_show = 5

    context = {
        'images' : images,
        'slides' : slides_to_show
    }
    
    return render(request, template, context)
