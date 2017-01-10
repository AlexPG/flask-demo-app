# Flask demo-app
This is a simple project written in flask for demo purposes.

# Requirements
+ Python 3.4
+ Virtualenv

# Installation
Download the repo in your target directory and unzip it. Create a virtualenv and activate it. Finally install all the packages in requirements.txt file with the following command:
```python
pip install -r requirements.txt
```

# Usage
First of all we have to create the database. Open postgresql client and type 
```python
create database data_dev;
```
Then, back in the console
```python
python manage.py createdb
```
will create all tables and relationships.

Finally 
```python
python manage.py runserver
```
will run the development server.

Now you can navigate to [localhost:5000](http://localhost:5000) or [localhost:5000/api/](http://localhost:5000/api/).

# Test
To run all the tests simply write 
```python
py.test
```