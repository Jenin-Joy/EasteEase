from django.urls import path,include
from Owner import views
app_name="Owner"

urlpatterns = [
path('Homepage/',views.Homepage,name='Homepage'),
path('Myprofile/',views.Myprofile,name='Myprofile'),
path('Editprofile/',views.Editprofile,name='Editprofile'),
path('Changepassword/',views.Changepassword,name='Changepassword'),    
path('Rentproperty/',views.Rentproperty,name='Rentproperty'),
path('Ajaxplace/',views.Ajaxplace,name='Ajaxplace'),
path('Sellproperty/',views.Sellproperty,name='Sellproperty'),
path('Viewsellbooking/',views.Viewsellbooking,name='Viewsellbooking'),
path('Viewrentbooking/',views.Viewrentbooking,name='Viewrentbooking'),
path('rentverification/<int:id>/<int:sts>',views.rentverification,name='rentverification'),
path('sellverification/<int:id>/<int:sts>',views.sellverification,name='sellverification'),

   path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('logout/',views.logout,name="logout"),
]