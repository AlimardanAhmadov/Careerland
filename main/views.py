from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, redirect 
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import RegistrationForm, ContactForm, CareerForm
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = "sk_test_jNv3kMTJ2PwPDuJz66KBKTFx00xZiVHQLo"



def home(request):
    context = {
        'name': 'Alimardan',
    }
    return render(request, "base.html", context)


def email(request):
    if request.method == 'POST':
        form= RegistrationForm(request.POST or None)

        if form.is_valid():
            from_email = form.cleaned_data.get("from_email")
            phone_number = form.cleaned_data.get('phone_number')
            comment = from_email + ' istifadəçisi qeydiyyatdan keçmək üçün müraciət etdi, əlaqə nömrəsi ' + phone_number
            send_mail('Qeydiyyat Formu', comment, from_email, [settings.EMAIL_HOST_USER])
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    context= {
        'form': form
        }
    return render(request, 'base.html', context)


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)

        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get("name")
            message = contact_form.cleaned_data.get("message")
            number = contact_form.cleaned_data.get("number")
            topic = contact_form.cleaned_data.get("topic")
            email = contact_form.cleaned_data.get("email")
            
            send_mail(
                topic,
                message,
                email,
                ['eelimerdan752@gmail.com']
            )
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')


def exams(request):
    return render(request, 'exams.html')


def gallery(request):
    return render(request, 'gallery.html')    


def career(request):
    if request.method == "POST":
        career_form = CareerForm(request.POST or None)
        
        if career_form.is_valid():
            career_form.save()
            teach_message = career_form.cleaned_data.get("teach_message")
            teach_email = career_form.cleaned_data.get("teach_email")
            
            send_mail(
                'Is qeydiyyati',
                teach_message,
                teach_email,
                ['eelimerdan752@gmail.com']

            )
    else:
        career_form = CareerForm()

    context = {
        'career_form': career_form,
    }

    return render(request, 'career.html', context)


def abroad(request):
    return render(request, 'abroad.html')    


def civil_service(request):
    return render(request, 'service.html')    


def driving(request):
    return render(request, 'driving.html')


def details(request):
    return render(request, 'details.html')


def charge(request):
    if request.method == 'POST':
        print('Data: ', request.POST)

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=500,
            currency='azn',
            description='Purchase'
        )

        return redirect('civil_service')

    return render(request, 'payment.html')



def civil_service_exams(request):
    return render(request, 'civil.html')