
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


# import json
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .forms import ContactForm
# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'index.html')
#         else:
#             errors = {field: form.errors[field][0] for field in form.errors}
#             return JsonResponse({'success': False, 'message': 'Form validation errors', 'errors': errors})
#     else:
#         form = ContactForm()

#     return render(request, 'index.html', {'form': form})