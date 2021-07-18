# Simple web app built with Flask

## Install dependencies
` pip install -r requirements.txt `

## Set up development server
- ` set FLASK_APP=main.py `
- ` set FLASK_ENV=development |  set FLASK_ENV=production `
- ` flask run `

## WSGI server for Linux systems: Gunicorn
` gunicorn -b 0.0.0.0:5000 -w num_workers wsgi:app`
