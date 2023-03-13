from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # giving route to access fingerprint in main project
    path('fingerprint/', include('fingerprint.urls')),
    # path('')
]
