# Evionix Application
**Owned: Somnath Bandyopadhyay**
**Author: Sayan Bandyopadhyay**

[![Version](https://img.shields.io/badge/Version-1.0-blue)](https://github.com/sayan98/vrddhi)
[![Python](https://img.shields.io/badge/Language-Python-blue)](https://www.python.org/)


## Description
This is the official website for the Evionix application. The application is a simple web application for displaying the Evionix website.

## Installation
To install the application, you need to have the Vrddhi framework installed. You can install the Vrddhi framework by running the following command:
```bash
$ python3 -m pip install virtualenv
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

## Usage
To run the application, you can run the following command:
```bash
$ gunicorn -w 4 --bind 127.0.0.0.1:8000 passenger_wsgi:application
OR
$ python3 -m flask run
```


## License
This application is proprietary and is not open source. You can use the application for personal use only.
