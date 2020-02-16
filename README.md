### Patient appointment system build in Python, using Django framework.

##### The program do:
- Inserts correctly registered patient for a visit into database.
- Sends an email to the managing person.
- Sends an email to patient if the visit is correctly registered.
- Shows appointments on the admin page.
- Allows you to select a date set by the manager of site.
- Allows admin to manage visits.
- You cannot enter the date, you must select it.
- Allows you to cancel your visit by entering an email.
- Displays information about the correct registration of the visit.
- Confirms deleting the visit by entering the code sent to the email address

##### The program checks:
- If the selected visit date is not already taken.
- If the email address has already been arranged for the visit.
- If the selected date is correct.
- If the given name is entered correctly.
- If the email is entered correctly.
- If all fields are filled in correctly.
- If the code provided to cancel the visit is correct.

##### Sending emails:
- To configure program to send emails go to: Patient_Appointment_System -> Patient_Appointment_System -> settings.py -> go to the bottom of the file and enter your details.
- Change email adress in views.py on line 51.

##### Admin panel:
- Login: szypkiwonsz
- Password: admin

##### Packages to install:
- pip install Django
- pip install django-crispy-forms

##### Version of software used:
- Python 3.7.x
- Django 2.2.5

