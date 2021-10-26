from django.db.models.expressions import F
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from screeninfo import get_monitors
from user_agents import parse
from ip2geotools.databases.noncommercial import DbIpCity
import socket
from .models import *

#matplotlib pacakages needed
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np

#Email package
from django.core.mail import send_mail

#check for vpn 
import logging, os, time
#THESE ARE GLOBAL VARIABLES TO KEEP TRACK OF DEVICE COUNT SO IT DOESN'T EARSE WHEN THE USER REFRESHES THE PAGE 
mobile = 0 
tablet = 0
monitor = 0
public_addy = ""
def vpn(request):
    PING_HOST= request.META.get("REMOTE_ADDR")
    while True:
        retcode = os.system('ping -c 1 %s' % PING_HOST)
        global public_addy
        if retcode:  
        # perform action for lost connection
            logging.warn('Lost visibility with %s' % PING_HOST)
            public_addy = "VPN-ACTIVE"
            print(f"\n {public_addy}\n")
            # return HttpResponse("WHY YOU HIDING BEHIND A VPN")  # sleep 10 seconds
            return HttpResponseRedirect("/index")
        else:
            public_addy = "NO-VPN"
            print(f"\n {public_addy}\n")
            index(request)
def index(request):
    global plublic_addy
    vibe_check = public_addy
    if vibe_check == "":
        return HttpResponseRedirect("/")
    if request.method == "GET":
        # global public_addy
        print("#######################################################################\n")
        print(f"\n##### USER AGENT INFORMATION #####\n")

    #THIS CALLS FOR THE NAME OF DEVICE MAKING THE REQUEST
        device=socket.gethostname()
        print(f"Device Name: {device}")
        print(f"VPN: {public_addy}")
    #THIS IS DJANGO 2.2 INBUILT FUNCTION. THIS ALLOWS TO RETRIVE THE IP ADDRESS MAKING THE REQUEST
        address=request.META.get("REMOTE_ADDR")
        print(f"IP: {address}")

    #PASS THE {adress} VARIABLE UNTO THE GEO LOCATION, THE API_KEY IS ALWAYS 'free"
        response = DbIpCity.get(f"{address}", api_key='free')
        print(f"User Location: {response.city}, {response.region} {response.country}")
        print(f"User Exact Location: Lattitude {response.latitude} Longitude {response.longitude}")
        city_name = str(response.city)
        region_name = str(response.region)
        country_name = str(response.country)
        latitude_exact = response.latitude
        longitude_exact = response.longitude

    #THIS IS DJANGO 2.2 INBUILT FUNCTION. THIS ALLOWS TO RETRIVE THE INFORMATION ON THE DEVICE
        user_info = request.headers['User-Agent']

    #THIS IS HOW TO PARSE THE {user_info} STRING. THIS THE user_agent PACKAGE AT WORK
        ua_string = str(user_info)
        user_agent = parse(ua_string)
        print(f"OS: {user_agent.os.family}")
        print(f"Browser: {user_agent.browser.family} v{user_agent.browser.version_string}")
        print(f"Device: {user_agent.device.family}")
        device_type = None
        if user_agent.is_mobile == True:
            device_type = "Mobile"
            global mobile
            mobile+=1
        if user_agent.is_tablet == True:
            device_type = "Tablet"
            global tablet
            tablet+=1
        if user_agent.is_pc == True:
            device_type = "Desktop"
            global monitor
            monitor+=1
        print(f"Device Type: {device_type}")
        print(f"Touch Capabilities: {user_agent.is_touch_capable}")
        print(f"Bot Request: {user_agent.is_bot}")
    #THIS SHOWS THE REQUEST NUMBER GIVING THEM ONE MORE UNIQUE ID 
        ticket=mobile+tablet+monitor
        #check if ip address is in the database
        
        ticket_exists = users.objects.filter(ticket_id=ticket)
        if ticket_exists:
            ticket = users.objects.all().count() + 1
        #DB CREATION
        a = users.objects.create(
            source = public_addy,
            flagged = False,
            ip = address,
            is_bot = user_agent.is_bot,
            visit_count =+ 1,
            ticket_id = ticket,
            )
        a.save()
        b = locations.objects.create(
            this_ticket = users.objects.get(ticket_id=ticket),
            country=country_name,
            city=city_name,
            region=region_name,
            lat=latitude_exact,
            lon=longitude_exact,
            )
        b.save()
        c = devices.objects.create(
            this_ticket = users.objects.get(ticket_id=ticket),
            name=device,
            type=device_type,
            family=user_agent.device.family,
            touch_capability=user_agent.is_touch_capable,
            os=user_agent.os.family,
            browser_name=user_agent.browser.family,
            )
        c.save()
        addy = public_addy
        if addy == "VPN-ACTIVE":
            d = users.objects.get(ticket_id=ticket)
            d.flagged = True
            d.save()
            flag = True
        print(f"Ticket #{ticket}")
        print(f"\n FLAGGED = {flag}\n")
        print("\n#### REQUEST COUNT and DEVICE COUNT #####\n")
        print(f"Total Request: Mobile - {mobile}, Tablet - {tablet}, Monitor - {monitor}\n")
        print("#######################################################################\n")
        #email 
        send_mail(
            f"New Visitor Ticket #{ticket}",
            f'''\n##### USER AGENT INFORMATION #####\n
            VPN: {public_addy}
            FLAGGED = {flag}\n 
            Device Name: {device}
            IP: {address}
            User Location: {response.city}, {response.region} {response.country}
            User Exact Location: Lattitude {response.latitude} Longitude {response.longitude}
            Device Type: {device_type}
            OS: {user_agent.os.family}
            Browser: {user_agent.browser.family} v{user_agent.browser.version_string}
            Touch Capabilities: {user_agent.is_touch_capable}
            Bot Request: {user_agent.is_bot}
            Device: {user_agent.device.family}
            \n#### REQUEST COUNT and DEVICE COUNT #####\n
            Total Request: Mobile - {mobile}, Tablet - {tablet}, Monitor - {monitor}\n
    #######################################################################\n
            ''',
            'carlitos.206.spam@gmail.com',   # from email
            ['carlitos.206.spam@gmail.com'],  # to email
        fail_silently=False,
        )
        if user_agent.is_bot == True:
            print("THE MITCHELLS GOT ME")
            return HttpResponse("NO BOTS")
        return render(request, 'index.html', {'ticket': ticket})
        
        # return render(request, "index.html")
    else:
        if request.method == "POST":
            return HttpResponseRedirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

