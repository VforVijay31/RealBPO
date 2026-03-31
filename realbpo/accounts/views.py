from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Profile   # import your Profile model
from home.models import Project   # import Project for employee dashboard
from django.contrib.auth.decorators import login_required

# Owner login
def owner_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.profile.role == "owner":
            login(request, user)
            return redirect('dashboard')  # Owner dashboard
        else:
            messages.error(request, "Invalid credentials or not an owner")
            return redirect('owner_login')
    return render(request, 'authentication/owner_login.html')


# Employee login
def employee_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if profile exists before accessing
            if hasattr(user, "profile") and user.profile.role == "employee":
                login(request, user)
                return redirect("employee_dashboard")
            else:
                messages.error(request, "This account is not registered as an employee.")
                return redirect("employee_login")  # redirect back to register page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("employee_login")  # redirect back to login page

    return render(request, "authentication/employee_login.html")



# Logout
def logout_user(request):
    # Accept only POST requests for security
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        # If someone tries GET, just redirect safely
        return redirect('home')



def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('register_user')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register_user')

        user = User.objects.create_user(username=username, password=password)

        # Ensure profile exists
        profile, created = Profile.objects.get_or_create(user=user)
        profile.role = "owner"
        profile.save()

        messages.success(request, "Owner account created successfully! You can now log in.")
        return redirect('owner_login')

    return render(request, 'authentication/register_user.html')

# Employee dashboard
@login_required
def employee_dashboard(request):
    if request.user.profile.role != "employee":
        return redirect("dashboard")  # Owners go to their own dashboard

    owner = request.user.profile.owner
    projects = Project.objects.filter(owner=owner)
    return render(request, "homepage/employee_dashboard.html", {"projects": projects})

@login_required
def create_employee(request):
    # Only owners can create employees
    if request.user.profile.role != "owner":
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Basic validation
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("create_employee")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return redirect("create_employee")

        # Create the employee user
        user = User.objects.create_user(username=username, password=password)

        # Update the auto-created profile
        profile = user.profile
        profile.role = "employee"
        profile.owner = request.user   # link employee to current owner
        profile.save()

        messages.success(request, f"Employee '{username}' created successfully!")
        return redirect("dashboard")

    return render(request, "authentication/create_employee.html")




@login_required
def employee_dashboard(request):
    if request.user.profile.role != "employee":
        return redirect("dashboard")

    # Get the owner linked to this employee
    owner = request.user.profile.owner

    # Fetch projects created by that owner
    projects = Project.objects.filter(owner=owner)

    return render(
        request,
        "homepage/employee_dashboard.html",
        {"projects": projects, "owner": owner}
    )
