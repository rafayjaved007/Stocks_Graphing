<h1>Graphs of Stocks</h1>

First of all, install python 3.9 in your system

<h2>Create the virtual environment</h2>
Go to the root directory and run the following command

`virtualenv venv`

<h2>Activate the virtual environment</h2>
You can activate the python environment by running the following command:

Mac OS/Linux

`source venv/bin/activate`

Windows

`venv\Scripts\activate`


Go to the root directory

<h3>Install dependencies</h3>

`pip install -r requirements.txt`

<h3>Migrate the database</h3>

`python manage.py migrate`

<h3>Run the project on local machine</h3>

`python manage.py runserver`

And navigate to http://127.0.0.1:8000/

<h2>To deploy the project on AWS Elastic Beanstalk:</h2>
Follow instructions from the given link of Official Documentation:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
