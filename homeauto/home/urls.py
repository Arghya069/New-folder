from django.urls import path
from . import views

urlpatterns = [
    path('home/<str:pk>',views.index,name='index'),
    path('A/<str:pk>',views.A),
    path('B/<str:pk>',views.a),
    path('C/<str:pk>',views.B),
    path('D/<str:pk>',views.b),
    path('E/<str:pk>',views.C),
    path('F/<str:pk>',views.c),
    path('datas/<str:pk>',views.Ldata)
]
