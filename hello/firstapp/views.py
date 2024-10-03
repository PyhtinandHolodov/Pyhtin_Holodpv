from .forms import UserForm
from django.shortcuts import render
def index(request):
 userform = UserForm()
 return render(request, "firstapp/index.html", {"form": userform})