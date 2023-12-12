from django.urls import path 

from case import views

urlpatterns = [

    path('listed-today/', views.case_list, name="listed-today"),
    path('registered/', views.registered_list, name="registered-today"),
    path('undated/', views.undated_list, name="undated-today"),
    path('<str:caseno>/detail/', views.case_details, name="case-detail"),
    path('<str:caseno>/bdiary/', views.view_bdiary, name="view-bdiary"),
    path('<str:caseno>/oldbdiary/', views.view_oldbdiary, name="view-oldbdiary"),
    path('<str:caseno>-<str:srno>/diary/', views.view_diary, name="view-diary"),
    path('<str:caseno>-<str:srno>/olddiary/', views.view_odiary, name="view-olddiary"),
    path('order-sheet', views.order_sheet, name="order-sheet")
]