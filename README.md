DAT (Dev and Alarm Tool)
DAT is a web application that provides multiple tools, including a note app and 17 different converters (e.g., Roman to numerical). Built with Django and deployed on Vercel, it offers a seamless user experience.

Features
 Note-taking functionality  
 17+ conversion tools (e.g., Roman to Number, Temperature, Currency, etc.)  
 User authentication & session management  
 Deployed on Vercel for fast, serverless performance  

Installation

Prerequisites
Make sure you have 'Python verasion 3.9 or more', 'pip', and 'Git' installed.

Clone the Repository in a new folder
 ```sh git clone https://github.com/Infinity-3/DAT.git```

Then create a virtual environent(venv) with this command
venv name can be anything; better name it related to project
 ```sh python -m venv venv_name```

Then activate the venv
```sh venv_name\scripts\activate'''

Then change directory to the project and open VScode in that directory
``` sh cd DAT
code . ```

And install the required packages to run the project
```sh pip install -r requirements.txt```

Start the Django development server by this command
```sh python manage.py runserver```

Database Setup & Migrations
 Run the following commands to apply database migrations:
 ```sh python manage.py migrate
 python manage.py createsuperuser  # Create admin user if required```

