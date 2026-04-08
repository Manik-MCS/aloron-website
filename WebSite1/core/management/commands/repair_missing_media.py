from django.core.management.base import BaseCommand

from core.models import Advisor, Donation, Member, PresidentMessage, Project, VicePresidentMessage


class Command(BaseCommand):
    help = "Clear broken media file references that no longer exist in storage."

    model_configs = (
        (PresidentMessage, "photo"),
        (VicePresidentMessage, "photo"),
        (Advisor, "photo"),
        (Member, "photo"),
        (Project, "screenshot"),
        (Donation, "photo"),
    )

    def handle(self, *args, **options):
        repaired = 0

        for model, field_name in self.model_configs:
            for obj in model.objects.all():
                file_field = getattr(obj, field_name, None)
                if not file_field or not getattr(file_field, "name", ""):
                    continue

                try:
                    exists = file_field.storage.exists(file_field.name)
                except Exception:
                    exists = False

                if exists:
                    continue

                setattr(obj, field_name, "")
                obj.save(update_fields=[field_name])
                repaired += 1
                self.stdout.write(
                    f"Cleared missing file for {model.__name__}#{obj.pk}: {field_name}"
                )

        self.stdout.write(self.style.SUCCESS(f"Repaired {repaired} missing media reference(s)."))
