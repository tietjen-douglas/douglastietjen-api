# Portfolio Website for Douglas Tietjen
## Introduction

A Django REST API backend for the portfolio website of Douglas Tietjen, showcasing a full stack development and deployment on to AWS.  The front end will be using React to output to the user.

## Development Server Setup
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

## Application Code
* [Python](https://www.python.org/)
* [Django](http://djangoproject.org/)
* [Django REST Framework](https://pypi.org/project/djangorestframework/)

## Tools
* [Microsoft Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/)
* [ModHeader](https://modheader.com/) or via the Chrome Extension Store

## Getting Started
1. Install the Developer Server and Tools (Vagrant, VirtualBox, VSCode, Git, etc.)
2. Clone the project to your machine `[git clone https://github.com/tietjen-douglas/douglastietjen-api.git]`
3. Navigate into the directory using Git Bash `[cd douglastietjen-api]`
4. Build the development server `[vagrant up]`
5. Connect to the development server `[vagrant ssh]` - exit the development server `[exit]`
6. Navigate into directory development server uses `[cd /vagrant]`
7. Source a virtual environment `[python -m venv ~/env]`
8. Activate virtual environment `[source ~/env/bin/activate]` - deactivate `[deactivate]`
9. Install the dependencies `[pip install -r requirements.txt]`

## Run the application
Make sure you are connected to the server and have the environment activated and then do the following:
1. `[python manage.py runserver 0.0.0.0:8000]`
2. Open a browser to this URL: http://127.0.0.1:8000/
The Vagrantfile script links the development server and localhost port 8000 together.

## See also React Front End Project

* [React](https://reactjs.org) - A progressive JavaScript framework.
* GitHub Repo coming later.


## GitHub Repository

(https://github.com/tietjen-douglas/douglastietjen-api)
