from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: redirect("dashboard:home")),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("hostels/", include("apps.hostels.urls")),
    path("residents/", include("apps.residents.urls")),
    path("verification/", include("apps.verification.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("search/", include("apps.search.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
