from django.urls import path
from core import views


urlpatterns = [
    path('dashboard/', views.index, name="dashboard.index"),
    path('case-listed-today/', views.case_list, name="case_list"),
    path('<str:caseno>/case-details/', views.case_details, name="case_details"),
    path('<str:caseno>/bdiary/', views.view_bdiary, name="view_bdiary"),
    path('<str:caseno>/obdiary/', views.view_oldbdiary, name="view_oldbdiary"),
    path('<str:caseno>/<str:srno>/diary/', views.view_diary, name="view_diary"),
    path('<str:caseno>/<str:srno>/old-diary/', views.view_odiary, name="view_old_diary")
]