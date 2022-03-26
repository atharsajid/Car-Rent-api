from django.urls import path
from api import views

urlpatterns = [

    path("users", views.ListUserAPIView.as_view(), name="user_list"),
    path("create/", views.CreateUserAPIView.as_view(), name="user_create"),
    path("update/<int:pk>/", views.UpdateUserAPIView.as_view(), name="user_update"),
    path("delete/<int:pk>/", views.DeleteUserAPIView.as_view(), name="user_delete"),
    path("car/", views.ListCarAPIView.as_view(), name="car_list"),
    path("car/create/", views.CreateCarAPIView.as_view(), name="car_create"),
    path("car/update/<int:pk>/",
         views.UpdateCarAPIView.as_view(), name="car_update"),
    path("car/delete/<int:pk>/",

         views.DeleteCarAPIView.as_view(), name="car_delete"),

         views.DeleteUserAPIView.as_view(), name="car_delete"),
    path("users/",views.ListUserAPIView.as_view(),name="user_list"),
    path("create/", views.CreateUserAPIView.as_view(),name="user_create"),
    path("update/<int:pk>/",views.UpdateUserAPIView.as_view(),name="user_update"),
    path("delete/<int:pk>/",views.DeleteUserAPIView.as_view(),name="user_delete")

]
