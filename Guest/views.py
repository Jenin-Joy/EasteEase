from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*

# Create your views here.
def index(request):
   return render(request,'Guest/index.html')


def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place,})
def registration(request):
    dist=tbl_district.objects.all()
    a=tbl_user.objects.all()
    if request.method=="POST":
        tbl_user.objects.create(user_name=request.POST.get("user_name"),user_email=request.POST.get("user_email"),user_contact=request.POST.get("user_contact"),user_password=request.POST.get("user_password"),user_address=request.POST.get("user_address"),user_place=tbl_place.objects.get(id=request.POST.get("sel_place")),user_photo=request.FILES.get("txt_file"))
        return render(request,'Guest/Registration.html',{'result':dist,'r':a})
    else:
        return render(request,'Guest/Registration.html',{'result':dist,'r':a})

def Login(request):  
    if request.method=="POST":
        email=(request.POST.get("email"))
        password=(request.POST.get("password"))
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        ownercount=tbl_owner.objects.filter(owner_email=email,owner_password=password).count()
        adminregcount=tbl_adminreg.objects.filter(adminreg_email=email,adminreg_password=password).count()
        if usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            return redirect("User:Homepage")
        elif ownercount>0:
            owner=tbl_owner.objects.get(owner_email=email,owner_password=password)
            request.session["oid"]=owner.id
            return redirect("Owner:Homepage")
        elif adminregcount>0:
            adminreg=tbl_adminreg.objects.get(adminreg_email=email,adminreg_password=password)
            request.session["aid"]=adminreg.id
            return redirect("Admin:Homepage")    
        else:
            return render(request,'Guest/Login.html')
    else:
            return render(request,'Guest/Login.html')        
    
def Ownerregistration(request):
    dist=tbl_district.objects.all()
    
    if request.method=="POST":
        tbl_owner.objects.create(owner_name=request.POST.get("owner_name"),
                                 owner_email=request.POST.get("owner_email"),
                                 owner_contact=request.POST.get("owner_contact"),
                                 owner_password=request.POST.get("owner_password"),
                                 owner_address=request.POST.get("owner_address"),
                                 owner_place=tbl_place.objects.get(id=request.POST.get("sel_place")))
        return render(request,'Guest/Ownerregistration.html',{'result':dist})
    else:
        return render(request,'Guest/Ownerregistration.html',{'result':dist})
               

               