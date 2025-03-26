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
                messages.success(request, "Password Changed Successfully.")
                return redirect('dashboard:profile')
            else:
                messages.error(request, "Passwords do not Match.")
                return redirect('dashboard:change_password', user_id=user_id)
        else:
            messages.error(request, "Incorrect Password.")
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
    messages.success(request, "Lead Deleted Successfully!!!")
    return redirect('dashboard:leads')

# USERS TABLE
# =============================================================== #

@login_required
def users(request):
    users = User.objects.all()
    context = { 'users': users}
    return render(request, 'users.html', context)

@login_required
def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_superuser = request.POST.get('is_superuser')
        is_active = request.POST.get('is_active')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    is_superuser = is_superuser,
                    is_active = is_active,
                    password = password1)
                user.save()
                messages.success(request, "User Created Successfully!!!")
                return redirect('dashboard:users')
            except:
                messages.error(request, "User Exists, Try Again!!!")
                return redirect('dashboard:users')
        else:
            messages.error(request, "Passwords do not Match")
            return redirect('dashboard:users')

    return render(request, 'users.html')


@login_required
def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_superuser = request.POST.get('is_superuser')
        is_active = request.POST.get('is_active')

        if username and email and first_name and last_name:
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name

            if is_superuser:
                user.is_superuser = is_superuser
            if is_active:
                user.is_active = is_active
        user.save()
        messages.success(request, "User Updated Sucessfully!!!")
        return redirect('dashboard:users')

    return render(request, 'users.html')

@login_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.error(request, "User Deleted Successfully!!!")
    return redirect('dashboard:users')


@login_required
def change_password_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request, "Password Changed Successfully.")
            return redirect('dashboard:users')
        else:
            messages.error(request, "Passwords do not Match.")
            return redirect('dashboard:users')
    else:
        messages.error(request, "All Fields are Required")
        return redirect('dashboard:users')
    
# ANALYTICS TABLE
# =============================================================== #

@login_required
def analytics(request):
    return render(request, 'analytics.html')


# CONFIG
# =============================================================== #

@login_required
def config_profile(request):
    return render(request, 'config.html')