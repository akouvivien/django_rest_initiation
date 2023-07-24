from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from crudProjet_api.views import AuthorViewSet,BookViewSet,RegisterView,ChangePasswordView,UpdateProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#pour le swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="REST APIs",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
        # Include DRF-Swagger URLs
    path('api/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/register/', RegisterView.as_view(), name='auth_register'),
    path('api/v1/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('api/v1/update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile')
]

# python manage.py createsuperuser creer un super utilisateur
# python manage.py runserver demarre le serveur
# python manage.py flush --noinput   supprimer le shema de la base de donnée sans interaction utilisateur 