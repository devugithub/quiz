from django.shortcuts import render

from django.http import HttpResponse
from  quizapp1.models import userregistration
# Create your views here.
def user(request):
    return render(request,"user.html")
def userprofile(request):
    return render(request,"userprofile.html")


def home(request):
    if request.method=="POST":
        usernameh=request.POST.get("username")
        passwordh=request.POST.get("password")
        user1=userregistration.objects.filter(login=usernameh,password=passwordh)
        print("user1")
        if user1:
            # return Response({'su':"login Successful"})
            
            return render(request,"userprofile.html")
            print()
            
        else:
            # return Response({'error':"Invalid credentials"})
            return render(request,"home.html")
    return render(request,"home.html")        

    
def question(request):
    return render(request,"question.html")
def quiztemplate(request):
    return render(request,"quiztemplate.html")    
    
def registration1(request):
    if request.method=="POST":
        login2=request.POST["loginname"]
        password2=request.POST["password"]
        email2=request.POST["email"]
        fname2=request.POST["fname"]
        sname2=request.POST["sname"]
        age2=request.POST["age"]
        gender2=request.POST["gender"]
        userregistration(login=login2,password=password2,email=email2,fname=fname2,sname=sname2,age=age2,gender=gender2).save()
        return render(request,"home.html")
    return render(request,"registration1.html")

def javaquiz(request):
    return render(request,"javaquiz.html")  

    
def aiquiz(request):
    return render(request,"aiquiz.html")  