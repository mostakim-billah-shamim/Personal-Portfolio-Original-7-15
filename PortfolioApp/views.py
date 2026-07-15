import threading # 🟢 একদম উপরে এটি ইম্পোর্ট করুন
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout

# 🟢 ব্যাকগ্রাউন্ডে ইমেইল পাঠানোর জন্য একটি আলাদা ফাংশন তৈরি করুন
def send_email_background(subject, body, from_email, to_email):
    try:
        send_mail(subject, body, from_email, to_email, fail_silently=False)
    except Exception as e:
        # ব্যাকগ্রাউন্ডে এরর হলে প্রিন্ট হবে, কিন্তু মেইন পেজ লোডিং আটকাবে না
        print(f"Email sending failed: {e}")


def Homepage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactModel.objects.create(
            name= name,
            email=email,
            subject=subject,
            message = message
        )

        
        email_subject = f"Portfolio Contact: {subject}"
        email_body = f"You have received a message from your portfolio website. \n\n "\
                        f"Name: {name} \n "\
                        f"Email: {email} \n "\
                        f"Message: \n {message} "
        
        # 🟢 ৩. থ্রেড (Thread) তৈরি করে মেইল ব্যাকগ্রাউন্ডে পাঠিয়ে দেওয়া
        email_thread = threading.Thread(
            target=send_email_background,
            args=(email_subject, email_body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        )
        email_thread.start() # এটি ব্যাকগ্রাউন্ডে কাজ শুরু করবে
        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')
    cont={
        'tdata': TestimonialModel.objects.all()
    }

    return render(request, 'pages/home.html', cont)




def LoginPage(request):
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.warning(request, 'You Dont Have Permission to Access this Site. Please Stay in Homepage')
            return redirect('home')
    else:
        form = LoginForm()

    cont= {
        'form': form,
        'title': 'Login Form',
        'btn': 'Login'
    }
    
    return render(request, 'pages/baseForm.html', cont)



def LogoutPage(req):
    logout(req)
    messages.warning(req, 'you are logged out!!!')
    return redirect('home')
















def TestimonialPage(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for your comments")
            return redirect('home')
    else:
        form = TestimonialForm()
    cont ={
        'form':form,
        'title': 'Testimonial Form',
        'btn': 'Submit'

    }
    return render(request, 'pages/baseForm.html', cont)


def TestimonialListPage(request):
    data= TestimonialModel.objects.all().order_by('-id')
    Cdata = ContactModel.objects.all().order_by('-id')
    cont={
        'data':data,
        'Cdata': Cdata
    }
    return render(request, 'pages/testimoniallist.html', cont)


def TestimonialDeletePage(request, id):
    
    TestimonialModel.objects.get(id=id).delete()
    messages.warning(request, 'Testimonial Deleted')
    return redirect('testimoniallist')


def ContactDeletePage(request, id):    
    ContactModel.objects.get(id=id).delete()
    messages.warning(request, 'Contact Deleted')
    return redirect('testimoniallist')


