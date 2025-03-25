from django.shortcuts import redirect, render
from dashboard.models import Lead
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def thankyou_page(request):
    return render(request, 'thankyou_page.html')

def capture_lead(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        plan = request.POST['plan']

        if fullname and email and phone and plan:
            lead = Lead(fullname=fullname, email=email, phone=phone, plan=plan)
            lead.save()
            return redirect('landing:thankyou_page')
        else:
            messages.error(request, "Please fill all the fields.")
            return redirect('landing:home')
    return render(request, 'home.html')