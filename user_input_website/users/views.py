from django.shortcuts import render, redirect
from .forms import UserInputForm

def user_input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()  # Save the input to the database
            return redirect('success')  # Redirect to success page after submission
    else:
        form = UserInputForm()

    return render(request, 'users/input_form.html', {'form': form})

def success_view(request):
    return render(request, 'users/success.html')