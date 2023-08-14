from django.urls import path

from . import views

urlpatterns = [
    #API routes

    path("freights", views.new_freight, name="new_freight"),
    path("freights/<int:freight_id>", views.freight_by_id, name="freight_by_id"),
    path("freights/all", views.all_freights, name="all_freights"),
    path("freights/generate-pdf/<str:content_disposition>", views.generate_pdf, name="generate-pdf")
]
