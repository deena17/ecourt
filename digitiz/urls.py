from django.urls import path
from digitiz import views

urlpatterns = [
    path('list-document', views.list_index, name="list-document"),
    path('add-document', views.add_documents, name="add-document")
]