from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from crudProjet_api.views import AuthorViewSet,BookViewSet,RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/register/', RegisterView.as_view(), name='auth_register'),
]

# python manage.py createsuperuser creer un super utilisateur
# python manage.py runserver demarre le serveur