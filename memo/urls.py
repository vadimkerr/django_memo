from django.urls import path
from . import views


app_name = "memo"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.CreateMemoView.as_view(), name="create"),
    path('list/', views.ListMemoView.as_view(), name="list"),
    path('detail/<int:pk>', views.DetailMemoView.as_view(), name="detail"),
    path('delete/<int:pk>', views.DeleteMemoView.as_view(), name="delete"),
    path('update/<int:pk>', views.UpdateMemoView.as_view(), name="update"),
]
