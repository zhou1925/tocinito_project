from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('api/v1/orders/', include('orders.urls')),
    # auth
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/verify/', TokenVerifyView.as_view()),
]
