from django.shortcuts import render, redirect
from .forms import LocationForm

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with your desired redirect URL
    else:
        form = LocationForm()
    return render(request, 'geocoding/add_location.html', {'form': form})
