# app view page, can be under a project

from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User as authUser
from django.contrib import messages

from .models import firewall_rules
from .forms import get_firewall_rules
from .forms import register_form

import wikipedia

def check_admin(user):
   return user.is_superuser

def test_page(request):
    return HttpResponse("Hello world")

# Home page view
def get_page_index(request):
    template = loader.get_template('firewall_rules/index.html')
    sample_string = "This is a string output by template function in django"
    context = {
        'sample_string' : sample_string,
    }
    return HttpResponse(template.render(context,request))

# list page view
def get_page_terms(request):
    template = loader.get_template('firewall_rules/terms.html')
    context = {}
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search,sentences = 10) #No of sentences that you want as output
        except:
            return HttpResponse("Wrong Input")
        return render(request,"firewall_rules/terms.html",{"result":result})
    
    return HttpResponse(template.render(context, request))

def get_page_firewall_practice(request):
    template = loader.get_template('firewall_rules/firewall_practice.html')
    context = {}
    return HttpResponse(template.render(context,request))

# create view
@staff_member_required
def get_page_playground(request):
    template = loader.get_template('firewall_rules/playground.html')
    context = {}
    return HttpResponse(template.render(context,request))

# edit view
def get_page_subnet_practice(request):
    template = loader.get_template('firewall_rules/subnet_practice.html')
    context = {}
    return HttpResponse(template.render(context,request))

# add view
def get_input_firewall_rules(request, practice_id):
    
    template = loader.get_template('firewall_rules/firewall_practice_django.html')
    
    # retrieve the firewall_rules object with foreign key specified by practice_id
    rules = firewall_rules.objects.all().filter(firewall_practice_id = practice_id)        

    # if the user access the form after the first time, use POST to populate the form
    if request.method == 'POST':
        form = get_firewall_rules(request.POST)
        if form.is_valid():
            zone = form.cleaned_data['zone']
            direction = form.cleaned_data['direction']
            source_ip = form.cleaned_data['source_ip']
            source_protocol = form.cleaned_data['source_protocol']
            source_detail = form.cleaned_data['source_detail']
            destination_ip = form.cleaned_data['destination_ip']
            destination_protocol = form.cleaned_data['destination_protocol']
            destination_detail = form.cleaned_data['destination_detail']
            action = form.cleaned_data['action']
            description = form.cleaned_data['description']
            
            # save input data to database
            p = firewall_rules(zone=zone, 
                direction=direction, 
                source_ip=source_ip, 
                source_protocol=source_protocol, 
                source_detail=source_detail, 
                destination_protocol=destination_protocol,
                destination_ip=destination_ip,
                destination_detail=destination_detail,
                action=action,
                description=description )
            
            p.save()
            form = get_firewall_rules()
    else:
        form = get_firewall_rules()

    context = {
        'form' : form,
        'firewall_rules' : rules,
    }

    return HttpResponse(template.render(context, request))

def show_firewall_rules(request):
    template = loader.get_template('firewall_rules/firewall_rules_output.html')
    rules = firewall_rules.objects.all()        
    context = {
        'firewall_rules': rules
        }
    return HttpResponse(template.render(context,request))

# detail view of one item
def show_firewall_rules_details(request,firewall_rules_id):
    template = loader.get_template('firewall_rules/firewall_rules_detailed_view.html')

    rule = firewall_rules.objects.get(pk=firewall_rules_id)

    zone = rule.zone
    direction = rule.direction
    source_address = rule.source_ip
    destination_address = rule.destination_ip
    port_numnber = rule.destination_detail
    action = rule.action
    description = rule.description

    context = {
        'zone': zone,
        'direction' : direction,
        'source_address' : source_address,
        'destination_address' : destination_address,
        'port_number' : port_numnber,
        'action' : action,
        'description' : description,
    }
    return HttpResponse(template.render(context,request))

def signout(request):
    logout(request)
    print(request.user)

    return redirect('/pages/index')

def signin(reqesut):
    if reqesut.method == "GET":
        return render(reqesut, "firewall_rules/signin.html", {})
    username = reqesut.POST['username']
    password = reqesut.POST['password']
    user = authenticate(reqesut, username=username, password=password)
    if user is not None:
        login(request=reqesut, user=user)
        # Redirect to a success page.
        return redirect('/pages/index')
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Invalid Login")

def signup(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/pages/index')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = register_form()
    
    context = {
        'form' : form,
    }
    template = loader.get_template('firewall_rules/signup.html')

    return HttpResponse(template.render(context, request))

def delete_entry(firewall_rules_id):
    firewall_rules.objects.filter(pk=firewall_rules_id).delete()
    return redirect("/pages/firewall_practice")

def edit_entry(request,firewall_rules_id):
    if request.method == "POST":
        entry = get_object_or_404(firewall_rules, pk=firewall_rules_id)
        form = get_firewall_rules(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect("/pages/firewall_practice")
    
    # if Get request is being used, call get_input_firewall_rules to
    # render the /pages/firewall_practice webpage
        
    template = loader.get_template('firewall_rules/firewall_practice_django.html')
    rules = firewall_rules.objects.all()

    # Populate the form with the data of the firewall rule that is about to be edited
    current_rule = firewall_rules.objects.all().filter(pk=firewall_rules_id)
    form = get_firewall_rules(initial={
        'zone': current_rule.values_list('zone', flat=True).first(),
        'direction': current_rule.values_list('direction', flat=True).first(),
        'source_ip': current_rule.values_list('source_ip', flat=True).first(),
        'source_protocol': current_rule.values_list('source_protocol', flat=True).first(),
        'source_detail': current_rule.values_list('source_detail', flat=True).first(),
        'destination_ip': current_rule.values_list('destination_ip', flat=True).first(),
        'destination_protocol': current_rule.values_list('destination_protocol', flat=True).first(),
        'destination_detail': current_rule.values_list('destination_detail', flat=True).first(),
        'action': current_rule.values_list('action', flat=True).first(),
        'description': current_rule.values_list('description', flat=True).first(),
    })

    context = {
    'form' : form,
    'firewall_rules' : rules,
    }
    return HttpResponse(template.render(context, request))


        