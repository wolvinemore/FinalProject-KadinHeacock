#### INF601 Advanced Python
#### Kadin Heacock
#### FinalProject-KH

# FinalProject-KH

Using Flask to create a web app that helps with decision making! Simply ask the 8-Ball what you want and it will give you an answer.

# Description



## Getting Started

Make sure you are good at what you do and what you do is master CHATGPT

### Dependencies

Run this command in order to install the dependencies on Mac or Linux 
```
pip install -r requirements.txt
```
If running windows, then run this command to install the dependencies 
```
py -m pip install -r requirements.txt 
```

### Executing program


Set up the SQL database:

Use this command to initialize your SQL server

```
flask --app flaskr init-db   ---Linux or Mac 

py -m flask --app flaskr init-db   ---Windows

This can be set up any way you prefer. However I prefer setting it up by creatin a folder main and creating tables.

```

Run these commands to start the server on your local host machine.

```
Navigate to http://127.0.0.1:5000/auth/register to register you account and then click the login link to log into your account.

Navigate to *http://127.0.0.1:5000/source* in order to launch the software
```
To run this server live for public usage, run this command and ensure this is the output:

```
pip install waitress or py - m pip install waitress

*waitress-serve --call 'flaskr:create_app'*

Serving on http://0.0.0.0:8080
```

### How to use

After the page is initially set up and the database is set up. Get to doing some threat research and collect some data!

### Output 

This should create a website that would allow you to insert indicators of compromise(IOC) data and share it with others.
As well as share detailed information about the cyber threat you are researching. 
The website also allows users to register an account and then login with said account.

Checkout and register at this link so you can view your API usage for AbuseIPDB
https://www.abuseipdb.com/account/api


## Author

Kadin Heacock

## Acknowledgments

[Professor Zeller]

[Python Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)

[Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/factory/)

[Flask API](https://pythonbasics.org/flask-rest-api/)

[error handling](https://stackoverflow.com/questions/22633227/sqlite-ambiguous-column-name)
