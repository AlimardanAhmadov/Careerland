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
            from_user = form.cleaned_data.get("from_user")
            from_surname = form.cleaned_data.get("from_surname")
            phone_number = form.cleaned_data.get('phone_number')
            form.save()

            comment = from_email + " istifadəçisi qeydiyyatdan keçmək üçün müraciət etdi, əlaqə nömrəsi " + phone_number
            pro_comment = from_user + " " + from_surname
            send_mail(pro_comment, comment, from_email, [settings.EMAIL_HOST_USER], fail_silently=False)

            return redirect('home')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'base.html', context)


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)

        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get("name")
            surname = contact_form.cleaned_data.get('surname')
            message = contact_form.cleaned_data.get("message")
            number = contact_form.cleaned_data.get("number")
            email = contact_form.cleaned_data.get("email")
            
            topic_comment = str(name) + " " + str(surname)
            cantact_comment = email + " - " + message + " , istifadeçinin əlaqə nömrəsi: " + number

            send_mail(
                topic_comment,
                cantact_comment,
                email,
                ['eelimerdan752@gmail.com'],
                fail_silently=False
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
            teach_name = career_form.cleaned_data.get('teach_name')
            teach_surname = career_form.cleaned_data.get("teach_surname")
            teach_message = career_form.cleaned_data.get("teach_message")
            teach_email = career_form.cleaned_data.get("teach_email")
            comment = teach_email + " - " + teach_message
            user_comment = teach_surname + " " + teach_name
            career_form.save()
            
            
            send_mail(
                user_comment,
                comment,
                teach_email,
                ['eelimerdan752@gmail.com'],
                fail_silently=False,
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
            amount=100,
            currency='azn',
            description='Purchase'
        )

        return redirect('civil_service')

    return render(request, 'payment.html')



def civil_service_exams(request):
    return render(request, 'civil.html')