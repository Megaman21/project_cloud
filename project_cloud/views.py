from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from megamaninn.forms import SignUpForm
from megamaninn.models import Review


def index(request):
    template = loader.get_template('test.html')
    context = {

    }

    return HttpResponse(template.render(context, request))


def loginpage(request):
    if request.method == "GET":
        template = loader.get_template('login.html')
        context = {

        }
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return render(request, 'homepage.html')
        else:
            return render(request, 'login.html')

    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('homepage.html')
    context = {

    }

    return HttpResponse(template.render(context, request))


def editpage(request):
    # template = loader.get_template('edit_profile.html')
    # context = {
    #
    # }
    #
    # return HttpResponse(template.render(context, request))
    if request.method == "GET":
        user = request.user
        return render(request, 'edit_profile.html', {'user': user})
    if request.method=="POST":
        # user=request.user
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        user = User.objects.get(username=email)
        user.first_name=firstname
        user.last_name=lastname
        user.email=email
        user.save()
        obj=request.user
        return render(request,'edit_profile.html',{'user':obj})

def signuppage(request):
    if request.method == "GET":
        template = loader.get_template('signup.html')
        context = {

        }

        return HttpResponse(template.render(context, request))
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        username = email

        firstname = name.strip().split(' ')[0]
        lastname = ' '.join((name + ' ').split(' ')[1:]).strip()

        if username and password:
            user, created = User.objects.get_or_create(username=username, email=email, first_name=firstname,
                                                       last_name=lastname)

            if created:
                user.set_password(password)
                user.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return render(request, 'homepage.html')
    else:
        return render(request, 'signup.html')


def bookpage(request):
    template = loader.get_template('booking.html')
    context = {

    }

    return HttpResponse(template.render(context, request))


def reviewpage(request):
    # template = loader.get_template('review.html')
    # context = {
    #
    # }
    #
    # return HttpResponse(template.render(context, request))
    # reviews_all=Review.objects.all()
    user = request.user
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST['rating']
        description = request.POST['message']
        reviewx = Review(user_id=user, review=description, rating=rating)
        reviewx.save()
        return render(request, 'homepage.html')
    if request.user.is_authenticated:
        reviews_all = Review.objects.all()
        return render(request, 'review.html',
                      {'reviews_all': reviews_all})


def doregister(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        form.save()
        return redirect('login.html')
        # else:
        #     form = SignUpForm()
        #     arg = {'forms': form}
        #     return render(request, 'signup.html', arg)
    else:
        form = SignUpForm()
        args = {'forms': form}
        return render(request, 'signup.html', args)
