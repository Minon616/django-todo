# todo_app/api_urls.py
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskDetailsViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'task-details', TaskDetailsViewSet)

urlpatterns = router.urls
