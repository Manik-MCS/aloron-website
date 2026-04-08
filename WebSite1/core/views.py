from django.db.utils import OperationalError, ProgrammingError
from django.shortcuts import render

from .models import Advisor, Donation, Member, PresidentMessage, Project, VicePresidentMessage


def home(request):
    try:
        context = {
            "president": PresidentMessage.objects.filter(is_active=True).first(),
            "vice_president": VicePresidentMessage.objects.filter(is_active=True).first(),
            "advisors": Advisor.objects.filter(is_active=True),
            "members": Member.objects.all(),
            "projects": Project.objects.all(),
            "donations": Donation.objects.all(),
        }
    except (OperationalError, ProgrammingError):
        # Keep the homepage available even if the production database is not ready yet.
        context = {
            "president": None,
            "vice_president": None,
            "advisors": [],
            "members": [],
            "projects": [],
            "donations": [],
        }
    return render(request, "core/home.html", context)
