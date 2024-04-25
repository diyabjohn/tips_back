
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL view
    path('tips/', views.TipListCreateAPIView.as_view(), name='tip-list-create'),
    path('tips/<int:pk>/', views.TipRetrieveUpdateDestroyAPIView.as_view(), name='tip-detail'),
    path('tip_form/', views.tip_form, name='tip-form'),
    path('tip_detail/<int:pk>/', views.tip_detail, name='tip-detail'),
]


