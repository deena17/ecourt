from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from core import views


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('dashboard'))),
    path('dashboard/', views.dasboard, name="dashboard"),
    path('case-list/', views.case_list, name="listed-today"),
    path('case-list/registered/', views.registered_list, name="registered-today"),
    path('case-list/undated/', views.undated_list, name="undated-today"),
    path('case-detail/<str:caseno>/', views.case_details, name="case-detail"),
    path('case-detail/<str:caseno>/bdiary/', views.view_bdiary, name="view-bdiary"),
    path('case-detail/<str:caseno>/oldbdiary/', views.view_oldbdiary, name="view-oldbdiary"),
    path('case-detail/<str:caseno>/<str:srno>/diary/', views.view_diary, name="view-diary"),
    path('case-detail/<str:caseno>/<str:srno>/olddiary/', views.view_odiary, name="view-olddiary"),
    path('case-detail/order-sheet', views.order_sheet, name="order-sheet")
]