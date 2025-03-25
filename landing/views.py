from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def thankyou_page(request):
    return render(request, 'thankyou_page.html')