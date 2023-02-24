from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>First Django Project</h1>')
