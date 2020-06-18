from django.shortcuts import render

# Create your views here.
def git_tutorials(request):
    return render(request, 'git_class/git_class.html')
