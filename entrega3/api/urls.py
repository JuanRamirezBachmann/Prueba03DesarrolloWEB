from django.conf.urls import url
from django.urls import path, include
from .views import(
    Entrega3DetailApiView,
    Entrega3ListApiView,
)

urlpatterns = [
    path('', Entrega3ListApiView.as_view()),
    path('<int:clienteID>/', Entrega3DetailApiView.as_view()),
    ]