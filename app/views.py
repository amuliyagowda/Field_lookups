from django.shortcuts import render

# Create your views here.

from app.models import *

def display_dept(request):
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.all().order_by('ename')
    QLEO=Emp.objects.exclude(job='Salesman')
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.filter(ename__startswith='a')
    QLEO=Emp.objects.filter(ename__endswith='th')
    QLEO=Emp.objects.filter(ename__contains='ll')
    QLEO=Emp.objects.filter(ename__in=['Allen','miller'])
    QLEO=Emp.objects.filter(hiredate__month=5)
    QLEO=Emp.objects.filter(hiredate__year=1981)
    QLEO=Emp.objects.filter(hiredate__day=22)
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)
    

def display_salgrade(request):
    QLSO=Salgrade.objects.all()
    QLSO=Salgrade.objects.filter(losal__gt='2001')
    QLSO=Salgrade.objects.filter(hisal__gte='2000')
    QLSO=Salgrade.objects.filter(losal__lt='2002')

    d={'QLSO':QLSO}
    return render(request,'display_salgrade.html',d)
