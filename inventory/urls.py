
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.create_item),
    path('items/<int:item_id>/', views.get_item),
    path('items/<int:item_id>/update/', views.update_item),
    path('items/<int)item_id>/delete/', views.delete_item),
]
    