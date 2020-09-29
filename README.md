# Furnace
This is a  web site for testing and verify performance and functional testing
tools

# Introduction

# Development environment
- python 3.8
- django 2.2.7
https://djangoproject.com/
- create development virtual env by
\> python -m venv Furance/venv

active virtual environment by execute
\> venv\Scripts\activate.bat

install all required libraries
\> pip install -r requirements.txt
- pinject
https://github.com/google/pinject
- coverage.py
https://coverage.readthedocs.io/en/coverage-5.0.3/


# Test web pages location
- save in the fixtures directory
- all the loaded web pages will be dynamic injected test helper scripts

# Directory Specification
- fixture_helpers, will contain all the JavaScript files which will be automatic
inject into the test pages
- fixtures contain all the test pages
- models, contain test data model
- venv, contain python virtual environment, currently the python version is 3.8


# Automatic load fixtures policies
- if the directory contain a index.html then added as loaded file
- if the directory doesn't contain a index.html then


# Features
1. record action lists and timestamp
2. provide exact network transformation statistic
3. provide test fields for different kinds of dom elements, javascript features
4. provide test fields for animations both in javascript and css
5. provide test fields for authentication

# Install


# TODO:
1. packaged into docker
2. automatic build and deployed
3. add template support for the fixtures folder. If a file ends with .tpl.html will be treat as a django template





