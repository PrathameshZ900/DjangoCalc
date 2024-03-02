from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CalculatorForm

def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            value1 = form.cleaned_data.get('Value1')
            operator = form.cleaned_data.get('Operater')
            value2 = form.cleaned_data.get('Value2')

            # Perform calculation based on operator
            if operator == '+':
                result = value1 + value2
            elif operator == '-':
                result = value1 - value2
            elif operator == '*':
                result = value1 * value2
            elif operator == '/':
                result = value1 / value2
            else:
                result = None  # Handle invalid operator

            # Redirect to ans view with result as parameter
            return redirect('ans', result=result)

    else:
        form = CalculatorForm()

    data = {
        'title': "Calculator",
        'form': form
    }
    return render(request, 'calculator.html', data)

def ans(request, result):
    print("Result:", result)  # Print result in terminal
    return HttpResponse("Result printed in terminal")
