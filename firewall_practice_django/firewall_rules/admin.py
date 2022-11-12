from django.contrib import admin

# NOTE: should import from firewall_rules.models instead of firewall_practice_django.firewall_rules.models
from firewall_rules.models import firewall_rules, nat_rules, route_table,interface

# Register your models here.
admin.site.register(interface)

admin.site.register(firewall_rules)

admin.site.register(nat_rules)

admin.site.register(route_table)