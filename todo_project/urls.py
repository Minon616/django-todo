# todo_project/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # All URLs from the todo_app (HTML + API routes)
    path('', include('todo_app.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
