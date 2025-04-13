from django.shortcuts import render,redirect
from Guest.models import*
from Owner.models import*
from User.models import*
from django.db.models import *
from datetime import *
# Create your views here.
def logout(request):
    del request.session["oid"]
    return redirect('Guest:Login')

def Homepage(request):  
    if "oid" not in request.session:
        return redirect("Guest:Login")
    return render(request,'Owner/Homepage.html')

def Myprofile(request): 
    if "oid" not in request.session:
        return redirect("Guest:Login")
    owner=tbl_owner.objects.get(id=request.session["oid"])
    return render(request,'Owner/Myprofile.html',{'owner':owner})

def Editprofile(request):
     if "oid" not in request.session:
        return redirect("Guest:Login")
     c=tbl_owner.objects.get(id=request.session["oid"])
     if request.method=="POST":
        c.owner_name=request.POST.get("owner_name")
        c.owner_email=request.POST.get("owner_email")
        c.owner_contact=request.POST.get("owner_contact")
        c.owner_address=request.POST.get("owner_address")
        c.save()
        return redirect("Owner:Myprofile")
     else:
         return render(request,"Owner/Editprofile.html",{'owner':c})

def Changepassword(request):
     if "oid" not in request.session:
        return redirect("Guest:Login")
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_owner.objects.get(id=request.session['oid'])
     olda=b.owner_password
     oldb= request.POST.get("owner_old_pasword")
     new=request.POST.get("owner_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.owner_password=request.POST.get("re_type_password")
                b.save()
                return redirect("Owner:Myprofile")
            else:
                return render(request,"Owner/Changepassword.html",{'error1':error1})
        else:
            return render(request,"Owner/Changepassword.html",{'error2':error2})
     else:
         return render(request,"Owner/Changepassword.html")

def Rentproperty(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    dist=tbl_district.objects.all()
    cat=tbl_category.objects.all()
    rent=tbl_rentproperty.objects.all()
    if request.method=="POST":
        catid=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_rentproperty.objects.create(rentproperty_location=request.POST.get("rentproperty_location"),
                                        place=tbl_place.objects.get(id=request.POST.get("sel_place")),
                                        rentproperty_type=request.POST.get("rentproperty_type"),
                                        rentproperty_rentaltype=request.POST.get("rentproperty_rentaltype"),
                                        rentproperty_price=request.POST.get("rentproperty_price"),
                                        rentproperty_photo=request.FILES.get("file_photo"),
                                        category=catid,
                                        owner=tbl_owner.objects.get(id=request.session['oid']))

        return render(request,'Owner/Rentproperty.html',{'result':rent,'cat':cat,'dist':dist})
    else:
        return render(request,'Owner/Rentproperty.html',{'result':rent,'cat':cat,'dist':dist})    

def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place,})

def Sellproperty(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    dist=tbl_district.objects.all()
    cat=tbl_category.objects.all()
    sell=tbl_sellproperty.objects.all()
    if request.method=="POST":
        catid=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_sellproperty.objects.create(sellproperty_location=request.POST.get("sellproperty_location"),
                                        place=tbl_place.objects.get(id=request.POST.get("sel_place")),
                                        sellproperty_type=request.POST.get("sellproperty_type"),
                                        sellproperty_price=request.POST.get("sellproperty_price"),
                                        sellproperty_photo=request.FILES.get("file_photo"),
                                        category=catid,
                                        owner=tbl_owner.objects.get(id=request.session['oid']))

        return render(request,'Owner/Sellproperty.html',{'result':sell,'cat':cat,'dist':dist})
    else:
        return render(request,'Owner/Sellproperty.html',{'result':sell,'cat':cat,'dist':dist})            

def Viewsellbooking(request): 
    if "oid" not in request.session:
        return redirect("Guest:Login")
    sellbook=tbl_bookproperty.objects.filter()
    return render(request,'Owner/Viewsellbooking.html',{'sellbook':sellbook})

def Viewrentbooking(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    book = tbl_rentbooking.objects.filter(rentproperty__owner=request.session['oid'])
    return render(request,'Owner/Viewrentbooking.html',{'book':book})


def rentverification(request,id,sts):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    rentbk=tbl_rentbooking.objects.get(id=id)
    rentbk.rentbooking_status=sts
    rentbk.save()
    return redirect("Owner:Viewrentbooking")

def sellverification(request,id,sts):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    bkproperty=tbl_bookproperty.objects.get(id=id)
    bkproperty.bookproperty_status=sts
    bkproperty.save()
    return redirect("Owner:Viewsellbooking")



def chatpage(request,id):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    user  = tbl_user.objects.get(id=id)
    return render(request,"Owner/Chat.html",{"user":user})

def ajaxchat(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    from_owner = tbl_owner.objects.get(id=request.session["oid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),owner_from=from_owner,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Owner/Chat.html")

def ajaxchatview(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    tid = request.GET.get("tid")
    owner = tbl_owner.objects.get(id=request.session["oid"])
    chat_data = tbl_chat.objects.filter((Q(owner_from=owner) | Q(owner_to=owner)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Owner/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    if "oid" not in request.session:
        return redirect("Guest:Login")
    tbl_chat.objects.filter(Q(owner_from=request.session["uid"]) & Q(user_to=request.GET.get("tid")) | (Q(owner_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"Owner/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})