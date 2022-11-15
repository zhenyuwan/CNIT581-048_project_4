from ipaddress import ip_address
from pyexpat import model
from turtle import pu
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        return "ID:" + str(self.id) + ";" + str(self.user.email)    

class firewall_practice(models.Model):
    # has one to many relationship to firewall_rules, route_table, interface, nat_rules

    creation_date = models.DateTimeField(auto_now_add=True)

class firewall_rules(models.Model):
    # firewall_rules class, has 10 attributes

    # foreign key will be that of the firewall_practice
    firewall_practice_id = models.ForeignKey(firewall_practice, on_delete=models.CASCADE, null=True)
    
    # zone; define the zone where the rule will be applied
    zone = models.CharField(max_length=40)

    # direction; define the direction of the rule relative to the interface, can be either IN or OUT
    direction = models.CharField(max_length=3)

    # source_ip: define the ip address of the source, example: 192.168.100.101/24
    source_ip = models.GenericIPAddressField(protocol = 'IPv4')

    # source_protocol: define layer 4 protocl, can be either UDP or TCP
    source_protocol = models.CharField(max_length=3)

    # source_detail: define the port number, can be from 0 to 65536
    source_detail = models.CharField(max_length=5)

    # destination_ip, protocol and detail are the same as above 
    destination_ip = models.GenericIPAddressField(protocol = 'IPv4')

    destination_protocol = models.CharField(max_length=3)

    destination_detail = models.CharField(max_length=5)

    # action: define the action taken by the firewall when matches, can be deny, drop or allow
    action = models.CharField(max_length=5)

    # Description: describe what this rule is for, does not have impact on if the rule matches
    description = models.CharField(max_length=100)

    #automatically update when changes
    pub_date = models.DateTimeField('date_published', auto_now=True)

    def __str__(self):
        return self.zone + ";" + self.direction + ";" + self.source_ip + ";" + self.source_detail + ";" + self.source_protocol + ";" + self.destination_ip + ";" + self.destination_detail + ";" + self.destination_protocol + ";" + self.description

class route_table(models.Model):
    #define the route in the firewall, has four attributes
    
    # foreign key will be that of the firewall_practice
    firewall_practice_id = models.ForeignKey(firewall_practice, on_delete=models.CASCADE, null=True)

    #destination: define the destination network, example:192.168.100.101/24
    destination = models.CharField(max_length=18)

    #next_hop: define the next hop of the route, example: 192.168.100.101
    next_hop = models.GenericIPAddressField(protocol = 'IPv4')

    #interface: define which interface the traffic would go out
    interface = models.CharField(max_length=20)

    #metric : define how many jump would take, usually 1
    metric = models.PositiveSmallIntegerField()

    #automatically update when changes
    pub_date = models.DateTimeField('date_published', auto_now=True)

class interface(models.Model):
    #interface defines how many interfaces are on the firewall, has 3 attributes

    # foreign key will be that of the firewall_practice
    firewall_practice_id = models.ForeignKey(firewall_practice, on_delete=models.CASCADE, null=True)

    #zone: define which interface the traffic would go out
    zone = models.CharField(max_length=40)

    # ip_address: define the ip address assigned to the interface
    ip_address = models.GenericIPAddressField(protocol = 'IPv4')

    # subnet_mask: define the subnet mask for the IP address, example 255.255.255.0
    subnet_mask = models.GenericIPAddressField(protocol = 'IPv4')

    #automatically update when changes
    pub_date = models.DateTimeField('date_published', auto_now=True)

    # a function to display the 
    def __str__(self):
        return self.zone + ';' + self.ip_address + '/' + self.subnet_mask + ';' + str(self.current_time)

class nat_rules(models.Model):
    # nat_rules defines the natting rules in the firewall, has 8 attributes

    # foreign key will be that of the firewall_practice
    firewall_practice_id = models.ForeignKey(firewall_practice, on_delete=models.CASCADE, null=True)

    # nat_type: define the type of natting, can be either SNAT or DNAT
    # SNAT stands for static nat while DNAT stands for dynamic nat
    nat_type = models.CharField(max_length=4)

    # host_name: description for the natting rule 
    host_name = models.CharField(max_length=40)

    # actual_zone: source zone of the natting, can be any zone defined earlier
    actual_zone = models.CharField(max_length=40)

    # actual_address: address that is to be translated. 
    actual_address = models.GenericIPAddressField(protocol = 'IPv4')

    # actual_subnet_mask: the subnet mask for the address to be translated, example 255.255.255.0
    actual_subnet_mask = models.GenericIPAddressField(protocol = 'IPv4')

    # mapped_zone: define the zone where the source address is translated
    # has one-to-one relationship with zones in other class
    mapped_zone = models.CharField(max_length=40)

    # mapped_address: the address that is to be translated into
    mapped_address = models.GenericIPAddressField(protocol = 'IPv4')

    # mapped_subnet_mask: the subnet mask for the address that is to be translated into, example 255.255.255.0
    mapped_subnet_mask = models.GenericIPAddressField(protocol = 'IPv4')

    #automatically update when changes
    pub_date = models.DateTimeField('date_published', auto_now=True)

    