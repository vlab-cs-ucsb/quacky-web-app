
# Quacky Web App

This is a Django web application for [Quacky](https://vlab.cs.ucsb.edu/quacky/).

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
- Python 3
- [ABC](https://github.com/vlab-cs-ucsb/ABC)

## Download
<pre>
git clone https://github.com/ganeshsankaran/quacky-web-app.git
cd quacky-web-app
git pull origin master
</pre>

## Setup
Install prerequisites from `requirements.txt` using `pip3`.
<pre>
sudo pip3 install -r requirements.txt
</pre>

## Usage
Start the server on port 80.
<pre>
sudo python3 manage.py runserver 0.0.0.0:80 &!
</pre>
<i>Note: Please make sure that the firewall allows HTTP traffic.</i>
