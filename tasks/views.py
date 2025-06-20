from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    html = """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Home Page</title>
</head>
<body>
    <h1> This is Home Page </h1>

</body>
</html>"""
    return HttpResponse(html)

def tasks(request):
    return HttpResponse("Task Home")
def showtasks(request):
    return HttpResponse("Show Tasks")
