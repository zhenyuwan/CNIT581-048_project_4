from django.urls import path
from django.contrib.auth import views as auth_views

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

    path('pages/<int:practice_id>/firewall_practice', views.get_input_firewall_rules, name='firewall_practice'),

    path('pages/subnet_practice', views.get_page_subnet_practice, name='subnet_practice'),

    path('pages/playground', views.get_page_playground, name='playground'),

    path('pages/output/firewall_rules', views.show_firewall_rules, name='show_rules'),

    path('pages/details/firewall_rules/<int:firewall_rules_id>', views.show_firewall_rules_details, name='details'),
    
    path('signout/', views.signout, name='signout'),

    path('signup/', views.signup, name='signup'),

    path('signin/', views.signin, name='signin'),

    path('action/delete/<int:firewall_rules_id>', views.delete_entry, name='delete_entry'),

    path('pages/firewall_practice/<int:firewall_rules_id>', views.edit_entry, name='edit_entry'),
]