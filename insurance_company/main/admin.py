from django.contrib import admin
from .models import Agent, Client, Contract, Object, Office, Rate

admin.site.register(Agent)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Object)
admin.site.register(Office)
admin.site.register(Rate)
