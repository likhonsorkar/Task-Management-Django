from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
   return  render(request, "dashboard/manager-dash.html")
def userdash(request):
   return render(request,"dashboard/userdash.html")

def test(request):
   return render(request, "test.html")