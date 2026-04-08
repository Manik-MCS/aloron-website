import logging

from django.db.utils import OperationalError, ProgrammingError
from django.http import HttpResponse
from django.shortcuts import render

from .models import Advisor, Donation, Member, PresidentMessage, Project, VicePresidentMessage

logger = logging.getLogger(__name__)


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
    try:
        return render(request, "core/home.html", context)
    except Exception:
        logger.exception("Homepage rendering failed")
        return HttpResponse(
            """
            <html>
                <head><title>Aloron</title></head>
                <body style="font-family: Arial, sans-serif; padding: 32px;">
                    <h1>Aloron</h1>
                    <p>Website is updating now. Please refresh again in a moment.</p>
                </body>
            </html>
            """,
            status=200,
        )
