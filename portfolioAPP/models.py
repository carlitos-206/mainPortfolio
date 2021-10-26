from django.db import models

class users(models.Model):
    #about the user
    flagged = models.BooleanField(default=False)
    source = models.CharField(max_length=100)
    ticket_id = models.CharField(max_length=255)
    ip = models.CharField(max_length=64, null=True, blank=True)
    if ip == None or ip == "":
        ip = "Unknown"
    is_bot = models.CharField(max_length=255, default="False")
    if is_bot == None or is_bot == "":
        is_bot = "False"
    visit_count = models.IntegerField(default=0)
    if visit_count == None or visit_count == "":
        visit_count = 0
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class locations(models.Model):
    this_ticket = models.ForeignKey(users, related_name="l_ticket", on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    if country == None or country == "":
        country = "Unknown"
    city = models.CharField(max_length=255)
    if city == None or city == "":
        city = "Unknown"
    region = models.CharField(max_length=255)
    if region == None or region == "":
        region = "Unknown"
    lat = models.CharField(max_length=255, null=True)
    if lat == None or lat == "":
        lat = 0
    lon = models.CharField(max_length=255, null=True)
    if lon == None or lon == "":
        lon = 0
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class devices(models.Model):
    this_ticket = models.ForeignKey(users, related_name="d_ticket", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    if name == None or name == "":
        name = "Unknown"
    type = models.CharField(max_length=255)
    if type == None or type == "":
        type = "Unknown"
    family = models.CharField(max_length=255)
    if family == None or family == "":
        family = "Unknown"
    os = models.CharField(max_length=255)
    if os == None or os == "":
        device_os = "Unknown"
    touch_capability = models.BooleanField(default=False)
    browser_name = models.CharField(max_length=255)
    if browser_name == None or browser_name == "":
        broswer_name = "Unknown"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # #about the users device