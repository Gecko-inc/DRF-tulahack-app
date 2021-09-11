from django.urls import path
from .views import SectionDetailView, SectionListView

app_name = "section"

urlpatterns = [
    path("section/<int:section_id>/", SectionDetailView.as_view(), name="section_detail"),
    path("sections/", SectionListView.as_view(), name="section_list"),
]
