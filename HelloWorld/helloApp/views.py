from django.shortcuts import render

# Create your views here.
def helloAppView(request):
    return render(request, 'hello.html')