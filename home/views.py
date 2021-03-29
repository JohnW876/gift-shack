from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Contact form code from
# https://www.ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'giftshack@example.com', ['giftshack@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, f'Contact message successfully sent! Thank you, we will be in touch shortly')
            return redirect ('home')


    form = ContactForm()
    return render(request, 'home/contact.html', {'form':form})
