from django.urls import path, re_path
from api import views, schema
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
   openapi.Info(
       title="Fundraising API",
       default_version='v1',
       description="For demo",
       url="https://www.craking-enigma.com/api/swagger/",
   ),
   public=True,
   generator_class=schema.OnlyHttpsSchemaGenerator,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('category-list/', views.ListCategory.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('project/', views.ListProject.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    ### JWT token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ### drf-yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
