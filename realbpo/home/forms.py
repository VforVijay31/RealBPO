from django import forms
from .models import Project, OutsourcedService

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "status"]


class OutsourcedServiceForm(forms.ModelForm):
    class Meta:
        model = OutsourcedService
        fields = [
            "service_name",
            "provider_name",
            "status",
            "completion_percentage",
            "contact_no",
            "contact_mail",
        ]

class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["status"]  # only status field

