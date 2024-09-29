from django.urls import path
from .views import curt_summary

urlpatterns=[
    path('',curt_summary,name="cart"),
    # path('add',views.cart_summary,name="cart_add"),
    # path('delete/',views.cart_summary,name="cart_delete"),
    # path('update/',views.cart_summary,name="cart_update"),
]