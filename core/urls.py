from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from core import views


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('dashboard'))),
    path('dashboard/', views.dasboard, name="dashboard"),
    path('case-listed-today/', views.case_list, name="listed-today"),
    path('undated-today/', views.undated_list, name="undated-today"),
    path('<str:caseno>/case-details/', views.case_details, name="case-detail"),
    path('<str:caseno>/bdiary/', views.view_bdiary, name="view-bdiary"),
    path('<str:caseno>/oldbdiary/', views.view_oldbdiary, name="view-oldbdiary"),
    path('<str:caseno>/<str:srno>/diary/', views.view_diary, name="view-diary"),
    path('<str:caseno>/<str:srno>/olddiary/', views.view_odiary, name="view-olddiary"),
    path('case-order-sheet', views.order_sheet, name="order-sheet")
]