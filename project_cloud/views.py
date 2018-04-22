from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from megamaninn.forms import SignUpForm
def index(request):
    template=loader.get_template('test.html')
    context= {

    }

    return HttpResponse(template.render(context,request))

def loginpage(request):
    template=loader.get_template('login.html')
    context= {

    }

    return HttpResponse(template.render(context,request))

def home(request):
    template=loader.get_template('homepage.html')
    context= {

    }

    return HttpResponse(template.render(context,request))

def editpage(request):
    template=loader.get_template('edit_profile.html')
    context= {

    }

    return HttpResponse(template.render(context,request))


def signuppage(request):
    if request.method == "GET":
     template=loader.get_template('signup.html')
     context= {

     }

     return HttpResponse(template.render(context,request))
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



def bookpage(request):
    template=loader.get_template('booking.html')
    context= {

    }

    return HttpResponse(template.render(context,request))
def reviewpage(request):
    template=loader.get_template('review.html')
    context= {

    }

    return HttpResponse(template.render(context,request))

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