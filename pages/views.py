from django.shortcuts import render,redirect
from .models import Employee
from pages.forms import EmployeeForm
# Create your views here.
def emp_list(request):
    employee = Employee.objects.all()
    return render(request, 'home.html', {'employee': employee})

def emp_detail(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'detail.html', {'employee': employee})

def emp_update(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
     form = EmployeeForm(request.POST,instance=employee)
     if form.is_valid():
         form.save()
         return redirect('detail:detail',employee.id)
    form = EmployeeForm(instance=employee,data=request.POST)
    return render(request, 'update.html', {'form': form})

def emp_delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home:home')

def emp_create(request):
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    form = EmployeeForm()
    return render(request, 'create.html',{'form':form})
