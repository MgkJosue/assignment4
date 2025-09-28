from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
import math

def calculator_view(request):
    result = None
    error = None
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            try:
                a = form.cleaned_data['a']
                b = form.cleaned_data['b']
                c = form.cleaned_data['c']
                
                # Check if a, b, and c are numeric (Django forms already validate this)
                # Additional validation checks
                
                # If a is less than 1, display a message
                if a < 1:
                    error = "Value A is too small (must be >= 1)"
                # If c is negative, provide a specific error message
                elif c < 0:
                    error = "Value C cannot be negative"
                else:
                    # If b is equal to 0, note it won't affect the result
                    b_message = ""
                    if b == 0:
                        b_message = " (Note: B is 0 and will not affect the result)"
                    
                    # If c is greater than or equal to 0, compute c^3
                    c_cubed = c ** 3
                    
                    # If the result of c^3 is greater than 1000
                    if c_cubed > 1000:
                        # Multiply the square root of c^3 by 10
                        intermediate_result = math.sqrt(c_cubed) * 10
                    else:
                        # Otherwise, divide the square root by a
                        intermediate_result = math.sqrt(c_cubed) / a
                    
                    # Add b to the final result
                    final_result = intermediate_result + b
                    
                    result = f"Final Result: {final_result:.2f}{b_message}"
                    
            except Exception as e:
                error = f"Calculation error: {str(e)}"
    else:
        form = InputForm()
    
    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error
    })