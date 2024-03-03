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
