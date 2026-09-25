from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from main.models import SiteSettings
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Murojaatingiz muvaffaqiyatli yuborildi! Tez orada javob beramiz.")
            return redirect('contacts:contact')
    else:
        form = ContactForm()
    context = {
        'settings': SiteSettings.objects.first(),
        'form': form,
    }
    return render(request, 'contacts/contact.html', context)
