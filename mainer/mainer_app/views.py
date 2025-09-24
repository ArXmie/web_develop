from django.shortcuts import render, HttpResponse

# Create your views here.
def mainer_view(request):
    text = "ладно"
    values = ["lo", "rem", "pe"]
    return render(request, 'main.html', {'my_note': text, 'is_draw_note': True, 'values': values})