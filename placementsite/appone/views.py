from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'appone/home.html')

def about(request):
	return render(request,'appone/about.html')

def contact(request):
	if request.method=="POST":
		name=request.POST.get('name','')
		email=request.POST.get('email','')
		rollno=request.POST.get('rollno','')
		gpa=request.POST.get('gpa','')
		phn=request.POST.get('phn','')
		res=request.POST.get('res','')
		contact=Contact(name=name, email=email, rollno=rollno, gpa=gpa,phn=phn,res=res)
		contact.save()
	return render(request,'appone/contact.html')
