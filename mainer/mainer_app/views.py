from django.shortcuts import render, HttpResponse

# Create your views here.
def mainer_view(request):
    return render(request, 'main.html')