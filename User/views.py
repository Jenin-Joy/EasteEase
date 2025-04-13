from django.shortcuts import render,redirect
from Guest.models import*
from Owner.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def logout(request):
    del request.session["uid"]
    return redirect("Guest:Login")

def Homepage(request):  
    if "uid" not in request.session:
        return redirect("Guest:Login")
    return render(request,'User/Homepage.html')

def Myprofile(request): 
    if "uid" not in request.session:
        return redirect("Guest:Login")
    user=tbl_user.objects.get(id=request.session["uid"])
    return render(request,'User/Myprofile.html',{'user':user})

def Editprofile(request):
     if "uid" not in request.session:
        return redirect("Guest:Login")
     b=tbl_user.objects.get(id=request.session["uid"])
     if request.method=="POST":
        b.user_name=request.POST.get("user_name")
        b.user_email=request.POST.get("user_email")
        b.user_contact=request.POST.get("user_contact")
        b.user_address=request.POST.get("user_address")
        b.save()
        return redirect("User:Myprofile")
     else:
         return render(request,"User/Editprofile.html",{'user':b})
def Changepassword(request):
     if "uid" not in request.session:
        return redirect("Guest:Login")
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_user.objects.get(id=request.session['uid'])
     olda=b.user_password
     oldb= new=request.POST.get("user_old_pasword")
     new=request.POST.get("user_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.user_password=request.POST.get("re_type_password")
                b.save()
                return redirect("User:Myprofile")
            else:
                return render(request,"User/Changepassword.html",{'error1':error1})
        else:
            return render(request,"User/Changepassword.html",{'error2':error2})
     else:
         return render(request,"User/Changepassword.html")
def Viewrentproperty(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    rent=tbl_rentproperty.objects.all()
    return render(request,'User/Viewrentproperty.html',{'rent':rent})   

def Viewsellproperty(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    sell=tbl_sellproperty.objects.all()
    return render(request,'User/Viewsellproperty.html',{'sell':sell}) 

def Bookproperty(request,id):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    count = tbl_bookproperty.objects.filter(bookproperty_sellproperty_id=id,bookpropertyuser_id=request.session['uid']).count()
    if count > 0:
        return render(request,"User/Viewsellproperty.html",{"msg":"Your Already Requested To this Property  Thank you...."})
    else:
        tbl_bookproperty.objects.create(
            bookproperty_sellproperty_id=tbl_sellproperty.objects.get(id=id),
            bookpropertyuser_id=tbl_user.objects.get(id=request.session['uid'])
        )
        return redirect("User:Viewbooking")

def Viewbooking(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    book = tbl_bookproperty.objects.filter(bookpropertyuser_id=request.session['uid'])
    return render(request,'User/Viewbooking.html',{'book':book})     

def Viewrentbooking(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    book = tbl_rentbooking.objects.filter(user=request.session['uid'])
    return render(request,'User/Viewrentbooking.html',{'book':book})          


def Rentbook(request,id):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    count = tbl_rentbooking.objects.filter(rentproperty=id,user=request.session['uid']).count()
    if count > 0:
        return render(request,"User/Viewrentproperty.html",{"msg":"Your Already Requested To this Property  Thank you...."})
    else:
        rent = tbl_rentproperty.objects.get(id=id)
        amount = rent.rentproperty_price
        if request.method == "POST":
            tbl_rentbooking.objects.create(
                rentproperty=tbl_rentproperty.objects.get(id=id),
                user=tbl_user.objects.get(id=request.session['uid']),
                rentbooking_fdate=request.POST.get("Fromdate"),
                rentbooking_tdate=request.POST.get("Todate"),
                rentbooking_amount=request.POST.get("txt_amount"))
            return redirect("User:Viewrentbooking")
        else:
            return render(request,'User/Rentbook.html',{"amount":amount})   
        
def Complaint(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    comp=tbl_complaint.objects.all()
    if request.method=='POST':
        title=request.POST.get("txtcontent")
        user_id = tbl_user.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(complaint_title=title,user=user_id)       
        return render(request,'User/Complaint.html')
    else:
        return render(request,'User/Complaint.html')
        


def chatpage(request,id):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    owner  = tbl_owner.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":owner})

def ajaxchat(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_owner = tbl_owner.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,owner_to=to_owner,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(owner_from=tid) | Q(owner_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(owner_to=request.GET.get("tid")) | (Q(owner_from=request.GET.get("tid")) & Q(owner_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})