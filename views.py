from django.shortcuts import render,redirect
from  django.http import HttpResponse
from student_list.models import Mexico
from student_list.form import createform,Mexicoform

def index(request):
   return render(request,'index.html')
def mexico(request):
   form=Mexicoform()
   context={'form':form}
   if request.method=="POST":
      form=Mexicoform(request.POST)
      if form.is_valid():
         form.save()
         return redirect('mexico')
  
   return render(request,'mexico.html',context)
def student(request):
   student=Mexico.objects.all()
   context={'student':student}

   return render(request,'student.html',context)
def form(request):
   form=createform()
   context={'form':form}
   return render(request,'form.html',context)

def update(request,id):
   student=Mexico.objects.get(id=id) 
   # form=Mexicoform(request.POST,instance=student)
   name=student.name
   dept=student.department
   age=student.age
   place=student.place
   college=student.college
   id=student.id
   context={'id':id,'name':name,'dept':dept,'age':age,'place':place,'college':college}
   if request.method=="POST":
      student=Mexico.objects.get(id=id) 
      student.name=request.POST['name']
      student.dept=request.POST['dept']
      student.age=request.POST['age']
      student.place=request.POST['place']
      student.college=request.POST['college']
      student.save()
      return redirect('student')
   return render(request,'update.html',context) 

