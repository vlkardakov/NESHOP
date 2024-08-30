from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:id>", views.view_product, name="view_product"),
    path("payment/<int:id>", views.payment, name='payment'),
    path("success", views.success, name='success')
]