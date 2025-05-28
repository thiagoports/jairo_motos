from django.shortcuts import render # vai renderizar o html

def motos(request):
    return render(
        request,
        'motos_styles/index.html'
    )