from django.db import models

# Create your models here.
class Bio(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()

class Register(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    password = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    
class UserDetail(models.Model):
    Name=models.CharField(max_length=30)
    Address=models.CharField(max_length=200)
    Permanent_Address=models.CharField(max_length=200)
    Date_Of_Birth=models.CharField(max_length=20)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=200)
    Description=models.CharField(max_length=500)
    Country=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Gender=models.CharField(max_length=20)
    Pin_Code=models.IntegerField(null=True)
    Country_code=models.IntegerField(null=True)
    Phone_Number=models.IntegerField(null=True)
    #Image=models.FileField(upload_to='pics',blank=True)
    #Image_2=models.FileField(upload_to='pics',blank=True)
    #File=models.FileField(upload_to='files_db',blank=True)
    '''Document_per2=models.FileField(upload_to='files_db',blank=True)
    Document_ver1=models.FileField(upload_to='files_db',blank=True)
    Document_ver2=models.FileField(upload_to='files_db',blank=True)'''
    Verified=models.BooleanField(default=False)
    #Percentage=(int(Amount_Reached)/int(Amount_Wanted))*100

class Cars(models.Model):
    name=models.CharField(max_length=54)
    images=models.FileField(upload_to='pics',blank=True)

class Images(models.Model):
    Name=models.CharField(max_length=50) 
    images=models.FileField(upload_to='pics',blank=True)

class Documents(models.Model):
    Name=models.CharField(max_length=54)
    Documents=models.FileField(upload_to='files_db',blank=True)

class CampaignDocuments(models.Model):
    Name=models.CharField(max_length=54)
    Title=models.CharField(max_length=54)
    Documents=models.FileField(upload_to='files_db',blank=True)

class CampaignDetail(models.Model):
    Name=models.CharField(max_length=54)
    Title=models.CharField(max_length=54,null=True)
    SubTitle=models.CharField(max_length=54,null=True)
    Description=models.CharField(max_length=2000,null=True)
    Amount_Wanted=models.IntegerField(null=True)
    Amount_Reached=models.IntegerField(null=True)
    Verified=models.BooleanField(default=False)
    Categoary=models.CharField(max_length=100,null=True)
'''class Fundraiser(models.Model):
    
    Name=models.CharField(max_length=30)
    Email=models.EmailField()'''
