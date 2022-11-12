from django.urls import path

from . import views

urlpatterns = [

    # an index page http://localhost/firewall_rules/
    path('', views.test_page, name='index'),
    # route: string that contains a URL pattern, in this case, local?
    # view: Call a function. In this case, test_page() function in views.py
    # name: name is the URL, change the name parameter in urls.py under firewall_practice_django
    # will make global change to url patterns
    

    path('pages/index', views.get_page_index, name='index'),

    path('pages/terms', views.get_page_terms, name='terms'),

    path('pages/firewall_practice', views.get_input_firewall_rules, name='terms'),

    path('pages/subnet_practice', views.get_page_subnet_practice, name='terms'),

    path('pages/playground', views.get_page_playground, name='terms'),

    path('pages/output/firewall_rules', views.show_firewall_rules, name='show_rules'),

    path('pages/details/firewall_rules/<int:firewall_rules_id>', views.show_firewall_rules_details, name='details')
]