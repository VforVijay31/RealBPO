from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from home.models import Project,OutsourcedService
from home.models import Profile
from home.forms import ProjectForm,ProjectStatusForm
from home.forms import OutsourcedServiceForm,OutsourcedService
# Create your views here.
def index(request):
    return render(request,'homepage/index.html')
def about(request):
    return HttpResponse("this is about")

@login_required
def dashboard(request):
    if request.user.profile.role != "owner":
        return redirect("employee_dashboard")

    # Get employees linked to this owner
    employees = Profile.objects.filter(owner=request.user, role="employee")

    # Get projects owned by this owner
    projects = Project.objects.filter(owner=request.user)

    return render(
        request,
        "authentication/dashboard.html",
        {"projects": projects, "employees": employees}
    )



@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.owner = request.user
            project.save()
            # No need for save_m2m unless you add ManyToMany fields later
            return redirect("view_project", project_id=project.id)
    else:
        project_form = ProjectForm()

    return render(
        request,
        "homepage/create_project.html",
        {"project_form": project_form}
    )



@login_required
def project_list(request):
    if request.user.profile.role != "owner":
        return redirect("employee_dashboard")

    projects = Project.objects.filter(owner=request.user)
    return render(request, "homepage/project_list.html", {"projects": projects})

@login_required
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Owner can edit everything
    if request.user == project.owner:
        form_class = ProjectForm
    else:
        # Employees can only edit status
        form_class = ProjectStatusForm  # a restricted form with only 'status' field

    if request.method == "POST":
        project_form = form_class(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save()
            return redirect("view_project", project_id=project.id)
    else:
        project_form = form_class(instance=project)

    return render(
        request,
        "homepage/update_project.html",
        {"project_form": project_form, "project": project}
    )

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == "POST":
        project.delete()
        return redirect('project_list')
    return render(request, "homepage/delete_project.html", {"project": project})

@login_required
def view_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Restrict access: only owner or their employees can view
    if request.user.profile.role == "employee":
        if project.owner != request.user.profile.owner:
            return redirect("employee_dashboard")
    elif request.user.profile.role == "owner":
        if project.owner != request.user:
            return redirect("dashboard")

    return render(request, "homepage/view_project.html", {"project": project})

@login_required
def add_service(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Allow both owner and employees linked to owner
    if request.user.profile.role not in ["owner", "employee"]:
        return redirect("view_project", project_id=project.id)

    if request.method == "POST":
        form = OutsourcedServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.project = project
            service.save()
            return redirect("view_project", project_id=project.id)
    else:
        form = OutsourcedServiceForm()

    return render(request, "homepage/add_service.html", {"service_form": form, "project": project})



@login_required
def edit_service(request, service_id):
    service = get_object_or_404(OutsourcedService, id=service_id)

    # Allow both owner and employees linked to owner
    if request.user.profile.role not in ["owner", "employee"]:
        return redirect("view_project", project_id=service.project.id)

    if request.method == "POST":
        form = OutsourcedServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("view_project", project_id=service.project.id)
    else:
        form = OutsourcedServiceForm(instance=service)

    return render(request, "homepage/edit_service.html", {"form": form, "service": service})

