from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.addFreight, name="addFreight"),
    path("edit<int:freight_id>", views.editFreight, name="editFreight"),
    path("remove<int:freight_id>", views.removeFreight, name="removeFreight"),
]