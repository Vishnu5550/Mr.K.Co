from django import forms

class CampaignForm(forms.Form):
    Name=forms.CharField(max_length=30)
    Address=forms.CharField(max_length=200)
    Permanent_Address=forms.CharField(max_length=200)
    Date_Of_Birth=forms.CharField(max_length=20)
    Title=forms.CharField(max_length=50)
    Sub_Title=forms.CharField(max_length=200)
    Description=forms.CharField(max_length=500)
    Country=forms.CharField(max_length=100)
    State=forms.CharField(max_length=100)
    Gender=forms.CharField(max_length=20)
    Pin_Code=forms.IntegerField()
    Country_code=forms.IntegerField()
    Phone_Number=forms.IntegerField()
    #Image_1=forms.ImageField()
    #Image_2=forms.ImageField()
    #Document_per1=forms.FileField()
    #Document_per2=forms.FileField()
    #Document_ver1=forms.FileField()
    #Document_ver2=forms.FileField()
    Verified=forms.BooleanField()
    Amount_Wanted=forms.IntegerField()
    Amount_Reached=forms.IntegerField()
    Currency_Name=forms.CharField(max_length=100)
    Currency_Symbol=forms.CharField(max_length=100)

'''class Images(forms.Form):
    Name=forms.CharField(max_length=50) 
    images=forms.FileField(upload_to='pics',blank=True)

class Documents(forms.Form):
    Name=forms.CharField(max_length=54)
    Documents=forms.FileField(upload_to='files_db',blank=True)'''
