from django.db.models.query import NamedValuesListIterable
from sampleapp.models import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

import random
global email_user ,name_user,password_user
        
#from .models import Destingnation
#def index(request):
   # return HttpResponse("Hello World")
def handle_not_found(request,exception):
    return render(request, "notfound.html")
def index(request):
    return render(request, "index.html",{})
def indexlog(request):
    return render(request,"indexlog.html",{})
def contact(request):
    return render(request, "contact.html",{})
def contactlog(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['email']
        Message=request.POST['message']
        str4="Email : "+Email+"\n Message :"+Message
        send_mail('Queries From Mr.K & Co Fund ', str4, 'god3vishnu420@gmail.com', ['god6vishnu420@gmail.com'],fail_silently=False)
        return redirect('indexlog')
    return render(request, "contactlog.html")
def donate(request):
    users=CampaignDetail.objects.all()
    imgs=Images.objects.all()
    pdetail=UserDetail.objects.all()
    return render(request, "donate.html",{'users':users,'imgs':imgs,'pdetail':pdetail})
def FAQ(request):
    return render(request, "FAQ.html",{})
def FAQlog(request):
    return render(request, "FAQlog.html",{'username':name123})
def mission(request):
    '''dest1=Destingnation()
    dest1.name='Karupannan'
    dest1.sub='the great founder'
    dest1.desc='asddhdhjdhsh sgvys sudf'

    dest2=Destingnation()
    dest2.name='Karupannan2'
    dest2.sub='the great founder2'
    dest2.desc='asddhdhjdhsh sgvys sudf'

    dest3=Destingnation()
    dest3.name='Karupannan3'
    dest3.sub='the great founde3r'
    dest3.desc='asddhdhjdhsh sgvys sudf'

    dests=[dest1, dest2,dest3, dest1, dest2, dest3, dest1, dest2, dest3]'''

    return render(request, "mission.html",{})#'dests':dests})
def missionlog(request):
   
    '''a=user.Amount_Wanted
    b=user.Amount_Reached
    if b!=0:
        c=(int(a)/int(b))*100
    elif b==0:
        c=0'''
    #a = (int(user.Amount_Reached)/int(user.Amount_Wanted))*100
    
   
    return render(request, "missionlog.html")#'dests':dests})
def services(request):
    return render(request, "services.html",{})
def serviceslog(request):
    return render(request, "serviceslog.html",{'username':name123})    
'''def register(request):
    if request.method == 'POST':
        username = request.POST['Fullname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1==pass2:
            user=User.objects.create_user(username=username, email=email,password=pass1)
            user.save();
            print('user created')
            return redirect('/')
    else:    
        print('user created not')
    return render(request, "sign.html",{})'''

def sign(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        print(name)
        global name123,status,reg1,name_user
        name123 = name
        name_user = name
        if Register.objects.filter(Name=name).exists():
            reg1=Register.objects.get(Name=name)
            status=reg1.status
            print(reg1.password)
            print(password)
            if reg1.password==password:
                #return render(request,'indexlog.html',{'username':name123})
                return redirect('indexlog')
            else:
                messages.info(request, 'password is mismatch')   
                return redirect('sign')    
        else:
            messages.info(request, 'Invalid username')
            return redirect('sign')    
    else:
        return render(request,'sign.html')
    '''print("from post")
    if request.method == 'POST':
        print("from post")
        Fullname = request.POST['Fullname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print("name %s email %s pass1 %s pass2 %s",Fullname,email, pass1, pass2)
        if pass1==pass2:
            user=Register(Name=Fullname, Email=email,password=pass1)
            user.save();
            print('user created')
            return redirect('/')
        else:
            print('user not created')    
    else:    
        print('user created not')'''
        
       
    return render(request, "sign.html",{})

def register(request):
    if request.method == 'POST':
        print('get post')
        #first_name=request.POST['first_name']
        #last_name=request.POST['last_name']
        '''form = UserCreationForm(request.POST)
        
        if form.is_valid():
            print('get post to form')
            form.save()
            return redirect('/')'''
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        global email_user,name_user,password_user
        email_user = email
        name_user = username
        password_user = password1
        if password1==password2:
            if Register.objects.filter(Name=username).exists():
                messages.warning(request,'Username is Already in use')
                return redirect('register')
            elif Register.objects.filter(Email=email).exists():
                #messages.success(request,'You created account succesfully!!')
                messages.warning(request,'This email is Already in use')
                return redirect('register')
            else:  
                global n
                n=random.randint(10005000,99999999)  
                str1="The OTP from Mr.K & Co is "
                str2=" . If you not tried to register in Mr.K & Co Funds Leave it."
                str3=str1+str(n)+str2
                send_mail('OTP From Mr.K & Co Fund ', str3, 'god3vishnu420@gmail.com', [email_user],fail_silently=False)
                
                #user=User(username=username,password=password1,email=email,)
                #user.save();
                #reg=Register(Name=username, Email=email, password=password1)
                #reg.save();
                #print('user created')
                #messages.success(request,'You created account succesfully!!')
                return redirect('otp')
        else:
            print("not pass matching")
            return render(request, "register.html")   
        return redirect('/')    
    else:
        
        print('not fount')
    return render(request, "register.html",{})
def otp(request):
    print(str(n))
    
    print(int(n))
    if request.method=='POST':
        otp=request.POST['otp']
        print(otp)
        print(n)
        if int(otp)==int(n):
            print(otp)
            print(n)
            
            print('user created')
            return redirect('person')
        else:
            return render(request, "otp.html")   
    else:
        return render(request, "otp.html")    
def logout(request):
    
    return redirect ('indexlog') 
def campaign(request):
    user=CampaignDetail.objects.filter(Name=reg1.Name)
    users=CampaignDetail.objects.all()
    img=Images.objects.get(Name=reg1.Name)
    imgs=Images.objects.all()
    pdetail=UserDetail.objects.all()
    
    global Title,SubTitle,Description,Amoount_Wanted
    if request.method=='POST':
        Title=request.POST['Title']
        SubTitle=request.POST['SubTitle']
        Description=request.POST['Desc']
        Amount_Wanted=request.POST['Amount_Wanted']
        Categoary=request.POST['Categoary']
        campaigncreate=CampaignDetail(Name=reg1.Name,Categoary=Categoary,Title=Title,SubTitle=SubTitle,Description=Description,Amount_Wanted=Amount_Wanted)
        campaigncreate.save()
        return redirect('upCampaignFiles')
    else:
        return render(request,"startasfund.html",{'user':user,'users':users,'img':img,'imgs':imgs,'pdetail':pdetail})    
def updateperson(request):
    if request.method=='POST':
        '''MyCampaignForm=CampaignForm(request.POST, request.FILES)
        if MyCampaignForm.is_valid():
            campaign=Campaign()
            campaign.Image_1=MyCampaignForm.cleaned_data["Image_1"]
            campaign.Name="vishnu"
            campaign.Address=MyCampaignForm.Address
            campaign.Permanent_Address=MyCampaignForm.Permanent_Address
            campaign.Date_Of_Birth=MyCampaignForm.Date_Of_Birth
            campaign.Title=MyCampaignForm.Title
            campaign.Sub_Title=MyCampaignForm.Sub_Title
            campaign.Description=MyCampaignForm.Description
            campaign.Country=MyCampaignForm.Country
            campaign.Country_code=MyCampaignForm.Country_code
            campaign.State=MyCampaignForm.State
            campaign.Gender=MyCampaignForm.Gender
            campaign.Pin_Code=MyCampaignForm.Pin_Code
            campaign.Phone_Number=MyCampaignForm.Phone_Number
            campaign.Image_2=MyCampaignForm.cleaned_data["Image_2"]
            campaign.Document_per1=MyCampaignForm.cleaned_data["Document_per1"]
            campaign.Document_per2=MyCampaignForm.cleaned_data["Document_per2"]
            campaign.Document_ver1=MyCampaignForm.cleaned_data["Document_ver1"]
            campaign.Document_ver2=MyCampaignForm.cleaned_data["Document_ver2"]
            campaign.save()'''
        print('post')
        Address=request.POST['Address']
        Permanent_Address=request.POST['PermanentAddress']
        State=request.POST['State']
        Gender=request.POST['Gender']
        Pin_Code=request.POST['PinCode']
        Country_Code=request.POST['CountryCode']
        Phone_Number=request.POST['PhoneNo']
        #Image2=request.FILES.getlist('image_campaign2')
        Description=request.POST['Desc']
        #files=request.FILES.getlist('files')
        #images=request.FILES.getlist('images')
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        Country=request.POST['Country']
        #Categoary=request.POST['Categoary']
        #Image1=request.FILES.getlist('image_campaign1')
        #Document_per1=request.FILES.getlist('Document_User1')
        #Document_per2=request.FILES.getlist('Document_User2')
        #Document_ver1=request.FILES.getlist('Document_Campaign1')
        #Document_ver2=request.FILES.getlist('Document_Campaign2')
        Date=request.POST['DOB']
        #Amount=request.POST['Amount_Wanted']
        #Currency_Name=request.POST['Currency_Name']
        #Currency_Symbol=request.POST['Currency_Symbol']
        #Image_1="pics/"+Image1
        delcamp=UserDetail.objects.get(Name=reg1.Name)
        delcamp.delete()
        print(Country)
        Camp=UserDetail(Name=name_user ,Address=Address,Permanent_Address=Permanent_Address,Date_Of_Birth=Date,FirstName=FirstName,LastName=LastName,Description=Description,Country=Country,State=State,Gender=Gender,Pin_Code=Pin_Code,Country_code=Country_Code,Phone_Number=Phone_Number)#,Image=images,File=files)#Image_1=Image_1,Image_2=Image2,Document_per1=Document_per1,Document_per2=Document_per2,Document_ver1=Document_ver1,Document_ver2=Document_ver2,
        Camp.save()
        return redirect('indexlog')

    else:   
        return render(request, "images/person.html")
def person(request):
    print('arrived')
    if request.method=='POST':
        '''MyCampaignForm=CampaignForm(request.POST, request.FILES)
        if MyCampaignForm.is_valid():
            campaign=Campaign()
            campaign.Image_1=MyCampaignForm.cleaned_data["Image_1"]
            campaign.Name="vishnu"
            campaign.Address=MyCampaignForm.Address
            campaign.Permanent_Address=MyCampaignForm.Permanent_Address
            campaign.Date_Of_Birth=MyCampaignForm.Date_Of_Birth
            campaign.Title=MyCampaignForm.Title
            campaign.Sub_Title=MyCampaignForm.Sub_Title
            campaign.Description=MyCampaignForm.Description
            campaign.Country=MyCampaignForm.Country
            campaign.Country_code=MyCampaignForm.Country_code
            campaign.State=MyCampaignForm.State
            campaign.Gender=MyCampaignForm.Gender
            campaign.Pin_Code=MyCampaignForm.Pin_Code
            campaign.Phone_Number=MyCampaignForm.Phone_Number
            campaign.Image_2=MyCampaignForm.cleaned_data["Image_2"]
            campaign.Document_per1=MyCampaignForm.cleaned_data["Document_per1"]
            campaign.Document_per2=MyCampaignForm.cleaned_data["Document_per2"]
            campaign.Document_ver1=MyCampaignForm.cleaned_data["Document_ver1"]
            campaign.Document_ver2=MyCampaignForm.cleaned_data["Document_ver2"]
            campaign.save()'''
        print('post')
        Address=request.POST['Address']
        Permanent_Address=request.POST['PermanentAddress']
        State=request.POST['State']
        Gender=request.POST['Gender']
        Pin_Code=request.POST['PinCode']
        Country_Code=request.POST['CountryCode']
        Phone_Number=request.POST['PhoneNo']
        #Image2=request.FILES.getlist('image_campaign2')
        Description=request.POST['Desc']
        #files=request.FILES.getlist('files')
        #images=request.FILES.getlist('images')
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        Country=request.POST['Country']
        #Categoary=request.POST['Categoary']
        #Image1=request.FILES.getlist('image_campaign1')
        #Document_per1=request.FILES.getlist('Document_User1')
        #Document_per2=request.FILES.getlist('Document_User2')
        #Document_ver1=request.FILES.getlist('Document_Campaign1')
        #Document_ver2=request.FILES.getlist('Document_Campaign2')
        Date=request.POST['DOB']
        #Amount=request.POST['Amount_Wanted']
        #Currency_Name=request.POST['Currency_Name']
        #Currency_Symbol=request.POST['Currency_Symbol']
        #Image_1="pics/"+Image1
        
        print(Country)
        Camp=UserDetail(Name=name_user ,Address=Address,Permanent_Address=Permanent_Address,Date_Of_Birth=Date,FirstName=FirstName,LastName=LastName,Description=Description,Country=Country,State=State,Gender=Gender,Pin_Code=Pin_Code,Country_code=Country_Code,Phone_Number=Phone_Number)#,Image=images,File=files)#Image_1=Image_1,Image_2=Image2,Document_per1=Document_per1,Document_per2=Document_per2,Document_ver1=Document_ver1,Document_ver2=Document_ver2,
        Camp.save()
        return redirect('upImages')

    else:   
        return render(request, "images/person.html",{})
def index1(request):
    '''if request.method == 'POST':
        images1=request.FILES.getlist('Images')
        
        for k in images1:
            print("for")
            img=Images(Name="vishnu",images=k)
            img.save()
            print("save")
            return redirect('upFiles')
    return render(request,"upImages.html") '''
    if request.method == "POST":
        images=request.FILES.getlist('images')
        
        for i in images:
            carinfo=Images(Name='rols',images=i)
            carinfo.save()
            print("hello")
        return HttpResponse('Images added')
    return render(request, "images/index.html")
def updateimg(request):
    if request.method == "POST":
        global images
        images=request.FILES.getlist('images')
          
        imgdel=Images.objects.get(Name=name_user)
        imgdel.delete()
        
        for i in images:
            carinfo=Images(Name=name_user,images=i)
            carinfo.save()
            print("hello")
        return redirect('indexlog')
        
    return render(request, "userImages/index.html",{'name_user':reg1.Name})

def upImages(request):
    if request.method == "POST":
        global images
        images=request.FILES.getlist('images')
         
        
        for i in images:
            carinfo=Images(Name=name_user,images=i)
            carinfo.save()
            print("hello")
        return redirect('upFiles')
        
    return render(request, "userImages/index.html",{'name_user':name_user})
    '''if request.method == "POST":
        images1=request.FILES.getlist('images')
        print("img")
        
        for k in images1:
            print("for")
            img=Images(Name="vishnu",images=k)
            img.save()
            print("save")
            return HttpResponse('Images added')
        #return redirect('upFiles')
    return render(request,"images/upImages.html") '''
def updatefiles(request):
    if request.method == "POST":
        images=request.FILES.getlist('files')
        
        fildel=Documents.objects.filter(Name=name_user)
        fildel.delete()
        
        for i in images:
            carinfo=Documents(Name=name_user,Documents=i)
            carinfo.save()
            print("hello")
   
        return redirect('indexlog')
    return render(request,"images/UpFiles.html",{'name_user':reg1.Name}) 

def upFiles(request):
    if request.method == "POST":
        images=request.FILES.getlist('files')
        
        
        for i in images:
            carinfo=Documents(Name=name_user,Documents=i)
            carinfo.save()
            print("hello")

        reg=Register(Name=name_user, Email=email_user, password=password_user)
        reg.save()    
        return redirect('sign')
    return render(request,"images/UpFiles.html",{'name_user':name_user}) 
def updatecampfiles(request):
    if request.method == "POST":
        images=request.FILES.getlist('files')
        title=request.POST['title']

        fildelc=CampaignDocuments.objects.filter(Name=reg1.Name)
        aaa=fildelc.filter(Title=title)
        aaa.delete()
        for i in images:
            carinfo=CampaignDocuments(Name=reg1.Name,Title=title,Documents=i)
            carinfo.save()
            print("hello")
   
        return redirect('indexlog')
    return render(request,"images/UpCampupdate.html",{'name_user':reg1.Name}) 
def upCampaignFiles(request):
    if request.method == "POST":
        images=request.FILES.getlist('files')
        
        for i in images:
            carinfo=CampaignDocuments(Name=reg1.Name,Title=Title,Documents=i)
            carinfo.save()
            print("hello")
   
        return redirect('indexlog')
    return render(request,"images/UpCampaignFiles.html",{'name_user':reg1.Name}) 