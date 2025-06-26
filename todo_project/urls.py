from django.contrib import admin
from django.urls import path, include

from django.conf import settings                # ✅ for media settings
from django.conf.urls.static import static     # ✅ for serving media in dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),  # ✅ main app routes
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
