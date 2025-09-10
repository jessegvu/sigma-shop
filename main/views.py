from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495496',
        'name': 'Jessevan Gerard Vito Uisan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
