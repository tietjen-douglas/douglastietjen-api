from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()
router.register('basic-viewset', views.BasicViewSet, basename="basic-viewset")
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('basic-api-view/', views.BasicApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]