from django.shortcuts import render,redirect
from EmailApp2.models import DataEntry
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def addDetails(request):
    return render(request,'addDetails.html')

def data(request):
    if request.method=='POST':
        UName=request.POST['User_Name']
        Pswd=request.POST['Password']
        EmailId=request.POST['Email']
        Data=DataEntry(UserName=UName,Password=Pswd,Email=EmailId)
        Data.save()
        subject="Greetings from Altos Technologies"
        message= f"Congratulations,\n You have successfully registered at Altos Technologies.\n Username: {UName} \n Password: {Pswd} \n\n Thank You"
        recip=Data.Email
        send_mail(subject,message,settings.EMAIL_HOST_USER,[recip])
    return redirect(table)

     
def table(request):
    authentication=DataEntry.objects.all()
    return render(request,'table.html',{'Data':authentication})

def delete(request,pk):
    Data=DataEntry.objects.get(id=pk)
    Data.delete()
    return redirect('table')