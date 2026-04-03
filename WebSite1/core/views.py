from django.shortcuts import render

from .models import Advisor, Donation, Member, PresidentMessage, Project, VicePresidentMessage


def home(request):
    context = {
        "president": PresidentMessage.objects.filter(is_active=True).first(),
        "vice_president": VicePresidentMessage.objects.filter(is_active=True).first(),
        "advisors": Advisor.objects.filter(is_active=True),
        "members": Member.objects.all(),
        "projects": Project.objects.all(),
        "donations": Donation.objects.all(),
    }
    return render(request, "core/home.html", context)
