from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from company.models import Company


# Create your views here.
def company_home(request):
    return render(request,'company.html')


def add_company(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        tech_stack = request.POST.get('tech_stack')
        address = request.POST.get('address')
        year_of_passing = request.POST.get('year_of_passing')

        Company.objects.create(
            company_name=company_name,
            role=role,
            salary=salary,
            tech_stack=tech_stack,
            address=address,
            year_of_passing=year_of_passing,
            added_by=request.user  # Auto capture logged-in user
        )

        messages.success(request, "Company added successfully!")
        return redirect('view_company')  # redirect to companies list

    return render(request,'add_company.html',{"password":True,'action':'add_company'})


def view_company(request):
   companies = Company.objects.all()
   for company in companies:
       company.auto_update_status()
   context = {
       'companies': companies
   }
   return render(request, 'view_company.html', context)


def update_company(request,id):
    company=get_object_or_404(Company,id=id)
    if request.method=='POST':
        company.company_name=request.POST.get('company_name')
        company.role=request.POST.get('role')
        company.salary=request.POST.get('salary')
        company.tech_stack=request.POST.get('tech_stack')
        company.address=request.POST.get('address')
        company.year_of_passing=request.POST.get('year_of_passing')
        company.save()
        return redirect('view_company')
    return render(request,'add_company.html',{'password':False,'action':'Update','company':company})


def delete_company(request,id):
    company = get_object_or_404(Company, id=id)
    company.delete()
    return redirect('view_company')