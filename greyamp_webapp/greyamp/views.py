from django.shortcuts import render
from .models import GreyampData
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, "home_page.html", context=None)


# class CheckAssignments():
#     p = GreyampData(name='Shakeel', assginment=1)
#     p.save()


from django.views.generic.edit import CreateView
from .models import GreyampData

class AuthorCreate(CreateView):
    model = GreyampData
    fields = ['name', 1]