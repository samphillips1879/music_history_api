#Music History API
This api allows registered users to browse and modify the contents of the Music History database.



##Installing and using the API

1. Install [Python 3.6](https://www.python.org/)
1. Install [pip](https://pip.pypa.io/en/stable/installing/)
1. Install Django 1.10.5 via pip: `pip install django`
1. Clone this repository to your machine: `git clone https://github.com/samphillips1879/music_history_api.git`
1. Perform database migrations. In the main project directory `~/Music_History` (where `manage.py` is located), run the command `python manage.py migrate`
1. Start the development server. Run the command `python manage.py runserver`. Take note of the IP address and host port given.
1. To use the API, start a browser, and navigate to the IP and port, followed by `/api/`. i.e. ```http://127.0.0.1:8000/api/```. 
2. Alternatively, the administration page may be found at  `/admin/`.


##Installed Dependencies 

The API relies upon the following dependencies:

1. Python >v.3.6
1. Django >v1.10.5

##System Config

The API should run on all systems that meet the dependency requirements.