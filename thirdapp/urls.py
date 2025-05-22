
from django.urls import path
from thirdapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_pro',views.add_pro, name='add_pro'),
    path('display',views.display,name='display'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('pro_edit/<int:id>',views.pro_edit,name='pro_edit'),
    path('pro_delt/<int:id>',views.pro_del,name='pro_del'),
]
