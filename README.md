#Django Webapp Boilerplate Template

#### technologies we are using

**tools**

- virtualenv [>=16.0.0](https://virtualenv.pypa.io/en/latest/) - Why should we use [virtualenv](https://www.pythonforbeginners.com/basics/python-virtualenv-usage)?

   OSX / Ubuntu installation [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

- pip [>=19.1](https://pip.pypa.io/en/stable/reference/) - Why should we use [pip](https://www.pythonforbeginners.com/pip/)?

   OSX / Ubuntu installation [here](https://pip.pypa.io/en/stable/installing/).

**database**

- PostgreSQL [v11.3](https://www.postgresql.org/about/news/1939/) (aka psql, "post-grezz") - [Why should we use it?](https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989)

   OSX installation [here](https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d).
   
   Ubuntu installation [here](https://tecadmin.net/install-postgresql-server-on-ubuntu/).

**backend**

- Django [v2.1](https://docs.djangoproject.com/en/2.2/releases/2.1/) - Why should we [use Django](https://www.educba.com/uses-of-django/)? Why should we [use Django >=2.0](https://www.merixstudio.com/blog/Django2-how-will-it-change-Python-development/)?

- Python >=3.6 - I don't really need to explain why we're using python. It's fast, it's easy, and it's how Django works.

**middleware**

- psycopg2 [v2.8.2](http://initd.org/psycopg/docs/) - Why should we use [psycopg2](https://dba.stackexchange.com/questions/111969/what-exactly-is-psycopg2)?

    psycopg2 is Django middleware that is installed via `pip install -r requirements.txt`.

    **Note:** If you're experiencing issues installing psycopg2, check [this](https://github.com/python-pillow/Pillow/issues/3438#issuecomment-435169249) out.

#### technologies to consider

**frontend**
- SASS - https://sass-lang.com/ - write in SASS, which is very similar to CSS but includes variables and syntanctic sugar, and then run the SASS compiler to turn it into CSS.


**backend**

**middleware**
- babel (ES6 compiler) -  - allows us to write modern Javascript and not worry about browser compatibility: the babel compiler will turn our code into ES5.https://pypi.org/project/django-babel/