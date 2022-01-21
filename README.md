
# Quacky Web App

This is a Django web application for [Quacky](https://github.com/vlab-cs-ucsb/quacky/).

## Contents
- `QuackyWebApp/settings.py` contains settings
- `quackyv1/templates` contains HTML templates to render
- `quackyv1/forms.py` contains classes for forms
- `quackyv1/urls.py` contains mappings of urls to views
- `abc_v1/utils.py` contains utility functions for translating and analyzing policies
- `abc_v1/views.py` contains functions for views
- `static/codemirror-5.57.0` contains source code for CodeMirror, a JavaScript text editor
- `static/editor.js` contains code to initialize editor instances
- `static/jquery-3.5.1.min.js` contains source code for jQuery

## Prerequisites
- Python 3.8 or higher
- [Quacky](https://vlab.cs.ucsb.edu/quacky/)

## Download
```
git clone https://github.com/ganeshsankaran/quacky-web-app.git
cd quacky-web-app
```

## Setup
Install Git and Pip 3.
```
sudo apt install git python3-pip # replace "apt" with your package manager
```

Install prerequisites from `requirements.txt` using `pip3`.
```
sudo pip3 install -r requirements.txt
```

## Usage
Start the server on port 80.
```
sudo python3 manage.py runserver 0.0.0.0:80 &!
```
*Note: Please make sure that the firewall allows HTTP traffic.*
