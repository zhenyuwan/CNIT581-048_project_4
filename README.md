# Intended Audience and Realized Funtions
This is a web-based tool to help student understand the firewall rules. This tool will test students
understand to the creating firewall rules, dividing subnet.
The intended audience is anyone with basic network knowledge and who are willing to learn
how to set up firewall properly.
So far, this tool only partially implemented the subnet practice and firewall practice part. For
playground part of this web app, they are not interactive yet.

One user named “admin” has been set up. Admin user has access to add view and edit view.

On each page, there is a navigation panel which user can click to be directed to another webpage.

On each page, there is also a Night mode button user can click to set the background color. This
function is not complete yet. Some of the HTML element become invisible after switching.

On the Subnet Practice page, there are three text input boxes. User can enter subnet address in
the box and click on Submit button to test whether the result is correct.

On the firewall practice page, a form where user can add new item has been created. In this form,
user can input specification for firewall rules. There are around four rules configured as
examples. After clicking submit button, an ajax function will be called and output hyperlinks to
detailed view of each firewall rules. The form will also be saved to the database. Submit button
also can reset the form. Meanwhile, upon each time the page is refreshed, Django will format the
firewall rule table based on the records in the database using get request. After **the latest update**
, this page allow the user to **edit individual rule**, and **delete a particular rule**. The workflow will 
be the model for future implementation.

On the playground page, there is a table. Underneath the table is a New Line button. Upon click
this button, user can create a new row for the firewall rule table. The newly created row will
eventually allow user to input text to it. 

On the home page, a user **login and signup** function is added. So far, only username and password 
are required. After a user is successfully signed up, the user will be redirected to the home page.

## Installation
User will need to install sqlite database to run the program.
An admin user has been configured:

Username: admin

Password: admin

After unzip the file, in the directory project3/firewall_practice_django/, run the command

*pip3 install wikipedia*

to install the wikipedia module for the **API**

then run the command

*python manage.py runserver*

to start the test server

Access the home page in http://localhost:8000/pages/index

## Hosted Version
Access the django development server at:

http://3.133.247.115:8000/pages/index
