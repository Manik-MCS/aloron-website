from django.db import models
from django.templatetags.static import static


class SafeImageURLMixin:
    fallback_image = "images/no-image.svg"

    def _safe_file_url(self, field_name):
        file_field = getattr(self, field_name, None)
        if not file_field or not getattr(file_field, "name", ""):
            return static(self.fallback_image)

        try:
            if file_field.storage.exists(file_field.name):
                return file_field.url
        except Exception:
            pass

        return static(self.fallback_image)


class PresidentMessage(SafeImageURLMixin, models.Model):
    name = models.CharField("নাম", max_length=150)
    designation = models.CharField("পদবি", max_length=150, default="সভাপতি")
    photo = models.ImageField("ছবি", upload_to="president/")
    message = models.TextField("বার্তা")
    is_active = models.BooleanField("সক্রিয়", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "President"
        verbose_name_plural = "President"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def display_image_url(self):
        return self._safe_file_url("photo")


class VicePresidentMessage(SafeImageURLMixin, models.Model):
    name = models.CharField("নাম", max_length=150)
    designation = models.CharField("পদবি", max_length=150, default="সহ-সভাপতি")
    photo = models.ImageField("ছবি", upload_to="vice-president/")
    message = models.TextField("বার্তা")
    is_active = models.BooleanField("সক্রিয়", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vice President"
        verbose_name_plural = "Vice President"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def display_image_url(self):
        return self._safe_file_url("photo")


class Advisor(SafeImageURLMixin, models.Model):
    name = models.CharField("নাম", max_length=150)
    designation = models.CharField("পদবি", max_length=150, default="উপদেষ্টা")
    photo = models.ImageField("ছবি", upload_to="advisors/")
    message = models.TextField("বার্তা", blank=True)
    is_active = models.BooleanField("সক্রিয়", default=True)
    ordering = models.PositiveIntegerField("সাজানোর ক্রম", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Advisor"
        verbose_name_plural = "Advisors"
        ordering = ["ordering", "-created_at", "name"]

    def __str__(self):
        return f"{self.name} - {self.designation}"

    @property
    def display_image_url(self):
        return self._safe_file_url("photo")


class Member(SafeImageURLMixin, models.Model):
    name = models.CharField("নাম", max_length=150)
    designation = models.CharField("পদবি", max_length=150)
    photo = models.ImageField("ছবি", upload_to="members/")
    bio = models.TextField("সংক্ষিপ্ত পরিচিতি", blank=True)
    facebook_url = models.URLField("Facebook link", blank=True)
    whatsapp_number = models.CharField("WhatsApp number", max_length=30, blank=True)
    linkedin_url = models.URLField("LinkedIn link", blank=True)
    ordering = models.PositiveIntegerField("সাজানোর ক্রম", default=0)

    class Meta:
        ordering = ["ordering", "name"]

    def __str__(self):
        return f"{self.name} - {self.designation}"

    @property
    def display_image_url(self):
        return self._safe_file_url("photo")


class Project(SafeImageURLMixin, models.Model):
    title = models.CharField("প্রজেক্টের নাম", max_length=200)
    description = models.TextField("বর্ণনা")
    screenshot = models.ImageField("স্ক্রিনশট", upload_to="projects/")
    project_date = models.DateField("তারিখ", blank=True, null=True)
    ordering = models.PositiveIntegerField("সাজানোর ক্রম", default=0)

    class Meta:
        ordering = ["ordering", "-project_date", "title"]

    def __str__(self):
        return self.title

    @property
    def display_image_url(self):
        return self._safe_file_url("screenshot")


class Donation(SafeImageURLMixin, models.Model):
    title = models.CharField("দানের শিরোনাম", max_length=200)
    description = models.TextField("বর্ণনা")
    photo = models.ImageField("ছবি", upload_to="donations/")
    donation_date = models.DateField("দানের তারিখ", blank=True, null=True)
    amount = models.CharField("পরিমাণ", max_length=100, blank=True)
    ordering = models.PositiveIntegerField("সাজানোর ক্রম", default=0)

    class Meta:
        ordering = ["ordering", "-donation_date", "title"]

    def __str__(self):
        return self.title

    @property
    def display_image_url(self):
        return self._safe_file_url("photo")
