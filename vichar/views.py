from django.shortcuts import render
from .models import Vichar


# Create your views here.
def vichar(request):
    vichar = Vichar.objects.all()
    context = {
        'vichar': vichar
    }
    return render(request, 'vichar.html', context)
