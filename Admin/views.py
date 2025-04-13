from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import*
from User.models import *

# Create your views here.
def add(request):
   
    if request.method=="POST":
        a=int(request.POST.get("Number1"))
        b=int(request.POST.get("Number2"))
        c=a+b
        return render(request,"Admin/Add.html",{'result':c})
    else:
        return render(request,"Admin/Add.html")

def largest(request):
     if request.method=="POST":
        a=int(request.POST.get("Number1"))
        b=int(request.POST.get("Number2"))
        if(a>b):
          c=a
        else:
          c=b  
        return render(request,"Admin/Largest.html",{'result':c})
     else:
        return render(request,'Admin/Largest.html')

def calculator(request):
    if request.method=="POST":
        a=int(request.POST.get("Number1"))
        b=int(request.POST.get("Number2"))
        btn=request.POST.get("add")
        if(btn=='+'):
            c=a+b 
        elif(btn=='-'):
            c=a-b 
        elif(btn=='*'): 
            c=a*b 
        else:
            c=a/b
        return render(request,"Admin/calculator.html",{'result':c})
    else:
        return render(request,'Admin/calculator.html')  

def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")

def district(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    dist=tbl_district.objects.all()
    if request.method=="POST":
        district=(request.POST.get("District"))
        tbl_district.objects.create(district_name=district)

        return render(request,"Admin/District.html",{'result':dist})
    else:
        return render(request,"Admin/District.html",{'result':dist}) 


def deldis(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")                    


def viewcomplaint(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    complaint=tbl_complaint.objects.filter(complaint_status=0)
    replied=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{"complaint":complaint,'replied':replied})

def reply(request,id):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    complaint=tbl_complaint.objects.get(id=id)
    if request.method == "POST":
        complaint.complaint_reply=request.POST.get("reply")
        complaint.complaint_status=1
        complaint.save()
        return redirect("Admin:viewcomplaint")
    else:
        return render(request,"Admin:Reply.html")

        
    


def category(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    cat=tbl_category.objects.all()
    if request.method=="POST":
        category=(request.POST.get("Category"))
        tbl_category.objects.create(category_name=category)

        return render(request,"Admin/Category.html",{'result':cat})
    else:
        return render(request,"Admin/Category.html",{'result':cat}) 
        
def delcat(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")                                    

def adminreg(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    admin=tbl_adminreg.objects.all()  
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        tbl_adminreg.objects.create(adminreg_name=name,adminreg_email=email,adminreg_password=password)

        return render(request,"Admin/Adminreg.html",{'result':admin})
    else:
        return render(request,"Admin/Adminreg.html",{'result':admin})                     
 
def deladmin (request,id):
    tbl_adminreg.objects.get(id=id).delete()
    return redirect("Admin:adminreg")                    


def place(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("sel_dist"))
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
        return redirect("Admin:place")
    else:
         return render(request,'Admin/place.html',{'result':district,'place':place})

def brand(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    bnd=tbl_brand.objects.all()
    if request.method=="POST":
        brand=(request.POST.get("Brand"))
        tbl_brand.objects.create(brand_name=brand)

        return render(request,"Admin/Brand.html",{'result':bnd})
    else:
        return render(request,"Admin/Brand.html",{'result':bnd})              

def editdis(request,id):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    district= tbl_district.objects.get(id=id)
    district1=tbl_district.objects.all()
    if request.method=="POST":
        district.district_name=request.POST.get("District")
        district.save()                    
        return redirect("Admin:district")                    
    else:
        return render(request,"Admin/District.html",{'results':district,'result':district1})

def delplace(request,id):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")         
         
def Ownerverification(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    pending=tbl_owner.objects.filter(owner_status=0)
    accepted=tbl_owner.objects.filter(owner_status=1)
    rejected=tbl_owner.objects.filter(owner_status=2)
    return render(request,'Admin/Ownerverification.html',{'pending':pending,'accepted':accepted,'rejected':rejected})  
         
def Accept(request,id):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    own=tbl_owner.objects.get(id=id)
    own.owner_status=1
    own.save()
    return redirect("Admin:Ownerverification") 

def Reject(request,id):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    own=tbl_owner.objects.get(id=id)
    own.owner_status=2
    own.save()
    return redirect("Admin:Ownerverification") 
                           
def Homepage(request):  
    if "aid" not in request.session:
        return redirect("Guest:Login")
    return render(request,'Admin/Homepage.html')
     


                                    