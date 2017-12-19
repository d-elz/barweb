from django.shortcuts import render

from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist
import sys, os

from db import Bardb

from django.contrib.auth.decorators import login_required# @login_required
import json
from Bar_Coordinator.bar0.coordinator.operations import DatabaseOperationCoordinator ,RegisterCoordinator

db = Bardb()
# Create your views here.
def index(request):

    main_title = "Bar"
    name_menu = "main"
    context = {
                "main_title": main_title,
                "name_menu": name_menu,

        }

    return render(request , 'bar/home.html' , context )

def about(request):

    main_title = "Bar"
    name_menu = "About"
    context = {
                "main_title": main_title,
                "name_menu": name_menu,

        }

    return render(request , 'bar/about.html' , context )

def contact(request):

    main_title = "Bar"
    name_menu = "Contact"
    context = {
                "main_title": main_title,
                "name_menu": name_menu,

        }

    return render(request , 'bar/contact.html' , context )


def login(request):

    main_title = "Bar"
    name_menu = "Log In"
    context = {
                "main_title": main_title,
                "name_menu": name_menu,

        }

    return render(request , 'bar/logIn.html' , context )


def auth_view(request):

    main_title = "Bar"
    name_menu = "main"
    context = {
                "main_title": main_title,
                "name_menu": name_menu,

        }

    return render(request , 'bar/home.html' , context )


def logout(request):

    main_title = "Bar"
    name_menu = "Log Out"
    context = {
                "main_title": main_title,
                "name_menu": name_menu,

        }

    return render(request , 'bar/logout.html' , context )

def register_user(request):

    db = DatabaseOperationCoordinator()
    rg = RegisterCoordinator()

    if request.method == 'POST':
        nym = request.POST.get("nym")
        pk = request.POST.get("pk")

        check_nym_exist = db.checking_pseudonym(nym)

        if check_nym_exist:
            rg.coordinator_operation(data)
            print ""
        else:
            print ""
    #return render(request , 'bar/register.html' , context )
    return HttpResponse(request , 'bar/exchange_keys.html')

def exchange_keys(request):

    main_title = "Bar"
    name_menu = "ExchangeKeys"
    exchange_keys = db.select_entries("ExchangeKeyList")
    context = {
                "main_title": main_title,
                "name_menu": name_menu,
                "exchange_keys" :    exchange_keys,
        }

    return render(request , 'bar/exchange_keys.html' , context )

def exchange_client(request):

    exchange_keys = db.select_entries("ExchangeKeyList")

    #return HttpResponse(json.dumps(resp), mimetype="application/json" )
    return HttpResponse(json.dumps(exchange_keys), content_type='application/json')

def active_client(request):

    active_users = db.select_entries("ActiveList")

    #return HttpResponse(json.dumps(resp), mimetype="application/json" )
    return HttpResponse(json.dumps(active_users), content_type='application/json')

def public_client(request):

    public_users = db.select_entries("PublicList")

    #return HttpResponse(json.dumps(resp), mimetype="application/json" )
    return HttpResponse(json.dumps(public_users), content_type='application/json')


def active_users(request):

    main_title = "Bar"
    name_menu = "ActiveUsers"
    active_users = db.select_entries("ActiveList")
    context = {
                "main_title": main_title,
                "name_menu": name_menu,
                "active_users": active_users,
                }

    return render(request , 'bar/active_users.html' , context )

def public_users(request):

    main_title = "Bar"
    name_menu = "PublicUsers"
    public_users = db.select_entries("PublicList")
    context = {
                "main_title": main_title,
                "name_menu": name_menu,
                "public_users" : public_users

        }

    return render(request , 'bar/public_users.html' , context )
