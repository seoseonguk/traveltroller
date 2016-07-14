from django.shortcuts import render

def main(request):
    context = {

    }
    return render(request, "main/home.html", context)