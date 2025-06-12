from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),

]