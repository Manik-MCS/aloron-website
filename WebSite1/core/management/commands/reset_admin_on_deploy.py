import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update an admin user when explicitly enabled by env vars."

    def handle(self, *args, **options):
        enabled = os.getenv("RESET_ADMIN_ON_DEPLOY", "").lower() == "true"
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "")

        if not enabled:
            self.stdout.write("Admin reset is disabled.")
            return

        if not username or not password:
            self.stdout.write(
                self.style.ERROR(
                    "RESET_ADMIN_ON_DEPLOY is true, but username/password env vars are missing."
                )
            )
            raise SystemExit(1)

        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )

        if email:
            user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        action = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{action} admin user '{username}'"))
