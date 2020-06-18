from django.shortcuts import render


# Create your views here.
def home_page_index(request):
    return render(request, 'home_page/home_page.html')