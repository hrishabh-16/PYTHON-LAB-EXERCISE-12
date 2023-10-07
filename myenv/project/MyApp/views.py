from django.shortcuts import render

def election_registration(request):
    return render(request, 'MyApp/home.html')
