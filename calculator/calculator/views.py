from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CalculatorForm

def calculator(request):
    c = ""
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            opr = request.POST.get("opr")
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
    except:
        c = "Invalid operation..."
    
    print(c)  # This print statement will output the result in the console
    
    return render(request, 'calculator.html', {"c": c})
def evenOdd(request):
    c=""
    try:
        if(request.method=="POST"):
            if(request.POST.get("num")==""):
                return render(request,'evenOdd.html',{'error':True})
            
            n=int(request.POST.get("num"))
            if(n%2==0):
                c="It is Even Number"
            else:
                c="It is Odd Number"
    except:
        c="It is not a Number...."
        pass
    print(c)    
    return render(request,"evenOdd.html",{"c":c})               
def marksheet(request):
    t=0
    try:
        if(request.method=="POST"):
            s1=int(request.POST.get("s1"))
            s2=int(request.POST.get("s2"))
            s3=int(request.POST.get("s3"))  
            s4=int(request.POST.get("s4"))
            s5=int(request.POST.get("s5"))
            t=s1+s2+s3+s4+s5
            

    except:
        pass
    print(t)
    per=t*100/500

    next=""
    if(per>80):
        next="Go for next Class In A-div"
    elif(per>60):
        next="Go for Next Class In B-div"
    elif(per>35):
        next="Go for Next Class In C-div"
    else:
        next="Sorry!! Yout Fail Try Again!!!"        
    return render(request,"marksheet.html",{"per":per,"next":next})    