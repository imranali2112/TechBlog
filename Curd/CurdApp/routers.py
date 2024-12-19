from rest_framework.routers import DefaultRouter
from .viewsets import AboutViewSet, UserViewSet, BlogViewSets, StudentsViewSet, EmployeeViewSet, JobViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'user', UserViewSet)
router.register(r'blog', BlogViewSets)
router.register(r'student', StudentsViewSet)
router.register(r'employe',EmployeeViewSet)
router.register(r'job',JobViewSet)