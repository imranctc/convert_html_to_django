# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')
from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
  # Redirect to the same page after successful submission
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
