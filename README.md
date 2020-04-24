# Welcome!

Ladies Get Coffee is a networking platform for women. Mentees and mentors can connect to learn about their profession, company and life experience. They first connect online and then meet up for coffee in real life.

This is a mini version of a networking platform with the following capabilities:
- create a profile (login, logout, authentication)
- scroll through existing profiles
- edit profile (add job, email, company, university)
- message a user
- see messages

To see this app in action visit: https://ladies-get-coffee.herokuapp.com/

This is what you should see: 
![alt text](https://github.com/annapaux/ladies-get-coffee/blob/master/readme_images/pages_1.png)
![alt text](https://github.com/annapaux/ladies-get-coffee/blob/master/readme_images/pages_2.png)


## Run it locally
optionally create a virtual environment
`python3 -m venv 'coffee-venv'`
`source coffe-venv/bin/activate`

clone the app or download the zip file
```
git clone https://github.com/annapaux/ladies-get-coffee/
cd ladies-get-coffee
```

change the database pointer in the settings.py file
```
# coffee_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

install the requirements with:
`pip install -r requirements.txt`

make the database migrations and run the server with:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open the website in the browser: http://127.0.0.1:8000/


## Code Notes

The `coffee_project` folder includes all general settings. The main app is in the `app` folder, where the templates, views and models  of the authentication models and the overview are included. The `messenger` app includes the features to message someone and view messages. The `api` app includes the APIs for GET requests to company, university and incredible APIs.

### Main App
All templates use `app/templates/base.html` as base, which includes the header, login/logout links etc. `app/templates/home.html` is the landing page for authenticated users, whereas `app/templates/landing_page.html` is the landing page for any visitors. Any authentication pages are in the `app/templates/registration/` folder.

What urls lead to what page (view) can be seen in the `coffee_project/urls.py` file. The views can lead to landing page, sign up and editing the profile. (See logic in `app/views.py`) For example, 'edit_profile/' loads the edit_profile() view, which queries the data from the database, if the user already provided additional information, or shows an empty form if the user has not provided information yet.

Authentication happens with Django's built-in User profile and auth package. The base User only has a username and password. An additional model is the UserProfile, which saves the additional information (e.g. job, name) and the schema can be found in `app/models.py`, with a one-to-one foreign key to the user model.



## Run Tests
`python3 manage.py test`

To specify an app: `python3 manage.py test app`

To increase error messages: `python3 manage.py test --verbosity 2`
