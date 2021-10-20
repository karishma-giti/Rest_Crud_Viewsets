from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_app import views
from drf_app.views import StudentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'studentapi', views.StudentViewSet, basename='studentapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
    
]

