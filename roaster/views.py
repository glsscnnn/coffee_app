from django.shortcuts import render

# test view
def index(request):
   return render(request, 'roaster/index.html', None)