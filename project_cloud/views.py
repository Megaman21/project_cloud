from django.http import HttpResponse
from django.template import loader

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

def signuppage(request):
    template=loader.get_template('signup.html')
    context= {

    }

    return HttpResponse(template.render(context,request))

def bookpage(request):
    template=loader.get_template('booking.html')
    context= {

    }

    return HttpResponse(template.render(context,request))