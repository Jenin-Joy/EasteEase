from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
path('',views.index,name='index'),
path('Login/',views.Login,name='Login'),
path('registration/',views.registration,name='registration'),
path('Ajaxplace/',views.Ajaxplace,name='Ajaxplace'),
path('Ownerregistration/',views.Ownerregistration,name='Ownerregistration'),
]