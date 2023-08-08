from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_freight, name="add_freight"),
    path("edit<int:freight_id>", views.edit_freight, name="edit_freight"),
    path("remove<int:freight_id>", views.removef_reight, name="removef_reight"),
    path("generate-pdf/", views.generate_pdf, name="generate_pdf"),
]
