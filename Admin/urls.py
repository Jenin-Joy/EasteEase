from django.urls import path,include
from Admin import views

app_name="Admin"


urlpatterns = [
  path('add/',views.add,name='add'), 
  path('largest/',views.largest,name='largest'), 
  path('calculator/',views.calculator,name='calculator'), 
  path('district/',views.district,name='district'), 
  path('category/',views.category,name='category'), 
  path('adminreg/',views.adminreg,name='adminreg'),
  path('deladmin/<int:id>',views.deladmin,name='deladmin'),
  path('deldis/<int:id>',views.deldis,name='deldis'),
  path('delcat/<int:id>',views.delcat,name='delcat'),
  path('place/',views.place,name='place'),
  path('brand/',views.brand,name='brand'), 
  path('editdis/<int:id>',views.editdis,name='editdis'),
  path('delplace/<int:id>',views.delplace,name='delplace'),
  path('Ownerverification/',views.Ownerverification,name='Ownerverification'),
  path('Accept/<int:id>',views.Accept,name='Accept'),
  path('Reject/<int:id>',views.Reject,name='Reject'),
  path('Homepage/',views.Homepage,name='Homepage'),
  path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
  path('logout/',views.logout,name='logout'),
  path('reply/<int:id>',views.reply,name='reply'),
]






