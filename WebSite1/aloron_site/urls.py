"""
URL configuration for aloron_site project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]

# Serve uploaded media locally when Cloudinary is not configured.
# `django.conf.urls.static.static()` skips adding routes when DEBUG is False,
# so use an explicit route to keep media available in production deployments.
if not getattr(settings, "USE_CLOUDINARY_MEDIA", False):
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
