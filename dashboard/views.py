from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Lead
from django.contrib import messages

# Create your views here.
@login_required
def dashboard(request):
    leads = Lead.objects.all().order_by('-id')
    context = { 'leads': leads }
    return render(request, 'index.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def change_password(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        password_check = request.POST['password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        password_check = user.check_password(password_check)

        if password_check:
            if password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, "Password changed successfully.")
                return redirect('dashboard:profile')
            else:
                messages.error(request, "Passwords do not match.")
                return redirect('dashboard:change_password', user_id=user_id)
        else:
            messages.error(request, "Incorrect password.")
            return redirect('dashboard:change_password', user_id=user_id)

    return render(request, 'profile.html', {'user': user})

# LEADS TABLE
# =============================================================== #
@login_required
def leads(request):
    leads = Lead.objects.all().order_by('-id')
    context = { 'leads': leads }
    return render(request, 'leads.html', context)


@login_required
def edit_lead(request, id):
    lead = get_object_or_404(Lead, id=id)
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        plan = request.POST.get('plan')

        if fullname and email and phone:
            lead.fullname = fullname
            lead.email = email
            lead.phone = phone

            if plan:
                lead.plan = plan

            lead.save()
            messages.success(request, "Lead Updated Successfully!!!")
            return redirect('dashboard:leads')
        else:
            messages.error(request, "All Fields are Required")
            return redirect('dashboard:leads')
    return render(request, 'leads,html')

@login_required
def delete_lead(request, id):
    lead = get_object_or_404(Lead, id=id)
    lead.delete()
    messages.success(request, "Lead deleted Successfully!!!")
    return redirect('dashboard:leads')