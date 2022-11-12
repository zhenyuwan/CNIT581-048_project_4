# app view page, can be under a project

from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

from .models import firewall_rules
from .forms import get_firewall_rules


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
    return HttpResponse(template.render(context,request))

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
@staff_member_required
def get_input_firewall_rules(request):
    
    template = loader.get_template('firewall_rules/firewall_practice_django.html')
    # if the user access the form after the first time, use POST to populate the form
    rules = firewall_rules.objects.all()        

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