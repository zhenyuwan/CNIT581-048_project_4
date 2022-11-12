from django import forms


class get_firewall_rules(forms.Form):
    zone = forms.CharField(label='zone', max_length=40)

    # direction; define the direction of the rule relative to the interface, can be either IN or OUT
    direction = forms.CharField(max_length=3)

    # source_ip: define the ip address of the source, example: 192.168.100.101/24
    source_ip = forms.GenericIPAddressField(protocol = 'IPv4')

    # source_protocol: define layer 4 protocl, can be either UDP or TCP
    source_protocol = forms.CharField(max_length=3)

    # source_detail: define the port number, can be from 0 to 65536
    source_detail = forms.CharField(max_length=5)

    # destination_ip, protocol and detail are the same as above 
    destination_ip = forms.GenericIPAddressField(protocol = 'IPv4')

    destination_protocol = forms.CharField(max_length=3)

    destination_detail = forms.CharField(max_length=5)

    # action: define the action taken by the firewall when matches, can be deny, drop or allow
    action = forms.CharField(max_length=5)

    # Description: describe what this rule is for, does not have impact on if the rule matches
    description = forms.CharField(max_length=100)