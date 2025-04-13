from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Editprofile/<int:id>',views.Editprofile,name='Editprofile'),
    path('Viewrentproperty/',views.Viewrentproperty,name='Viewrentproperty'),
    path('Viewsellproperty/',views.Viewsellproperty,name='Viewsellproperty'),
    path('Bookproperty/<int:id>',views.Bookproperty,name='Bookproperty'),
    path('Viewbooking/',views.Viewbooking,name='Viewbooking'),
    path('Viewrentbooking/',views.Viewrentbooking,name='Viewrentbooking'),
    path('Rentbook/<int:id>',views.Rentbook,name='Rentbook'),
    path('Complaint/<int:id>',views.Complaint,name='Complaint'),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('logout/',views.logout,name="logout"),
]


