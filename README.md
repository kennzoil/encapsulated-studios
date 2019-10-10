# Commercial Website Template
### A Django webapp project template running on a PostgreSQL engine

## Table of contents

- [**for returning developers:**](#for-returning-developers)

    - [entering your development environment](#entering-your-local-dev-environment)
    
    - [updating the master repository](#adding-your-updates-to-the-official-codebase)

- [**for developers just joining the project:**](#for-developers-just-getting-started)

    - [take care of these installations first](#prerequisites-for-development)
    
    - [hook up your git repo connections](#hook-up-git)
    
    - [create your local dev environment](#create-your-local-virtual-dev-environment)
    
- [**we are using:**](#technologies-we-are-using)

    - [these dev tools](#current-dev-tools)
  
    - [this database](#current-database)
  
    - [this backend](#current-backend)
  
    - [this middleware](#current-middleware)
    
    - [these deployment tools](#current-deployment-tools)
    
    - [these hosting services](#current-hosting-services)
    
    - [these custom scripts](#current-custom-scripts)
  

- [**we're thinking about using:**](#technologies-to-consider)

    - [these deployment tools](#deployment-tools)

    - [these frontend tools](#frontend)
  
    - [these backend tools](#backend)
  
    - [this middleware](#middleware)

### for returning developers

#### entering your local dev environment

- each time you sit down to work on the project, follow these steps:
    
    - `cd` into the project root (eg. `cd ~/development/ProjectName/`).
    - in your terminal, run [this command](#current-custom-scripts): `source dev-start`.
    
    **Note:** Remember that for `dev-start` to work, you **must** have *virtualenv*, *pip*, and *git* [installed](#for-developers-just-getting-started) **and** the proper remote repositories [linked](#for-developers-just-getting-started) to your local git repository.

#### adding your updates to the official codebase

- whenever you have commits that you would like to include in the master repository (upstream), follow these steps:

    - make sure all your updates are merged into your local `master` branch
    - `cd` into the project root (eg. `cd ~/development/ProjectName/`).
    - in your terminal, run the command `./dev-update`.
    - if any merge conflicts arise after running the command, fix the conflicts locally and restart this process.
    
    **Note:** For help fixing merge conflicts, see [here](https://githowto.com/resolving_conflicts).

### for developers just getting started

#### prerequisites for development

- in order to be able to work on this project, you must first [install these onto your local machine](#current-dev-tools):
    - *virtualenv*
    - *pip*
    - *git*

#### hook up git

- **there are three copies (repositories) of this projects code that ou will be working with:**
    - First, **the remote master repository**, also known as ["upstream"](https://stackoverflow.com/questions/2739376/definition-of-downstream-and-upstream). This is the official live code of the project; an exact copy of the code that is currently running the live application. *Ideally*, nobody should ever manually change any of the master repository code; the only way the master repository's code should ever be updated is with [pull requests](https://confluence.atlassian.com/bitbucket/create-a-pull-request-945541466.html) coming from the developers own forks.
    - Second, **your remote fork**. This is your personal [copy of the master repository](https://stackoverflow.com/questions/7057194/what-is-the-difference-between-forking-and-cloning-on-github) code to which you will be pushing updates from your local computer. You can create your own fork using [these instructions](https://help.github.com/en/articles/fork-a-repo). **Hint:** forking a repository is entirely done on GitHub. **Another hint:** Remember, the remote master repository is not owned by you. When you fork the master repository, you are creating your own repository that is a copy of the master repository.
    - Third, **your local repository**. This is your forked code sitting on your local computer, which is where you will actually be coding. To get your newly forked repository code onto your computer, [follow these steps](https://help.github.com/en/articles/cloning-a-repository). Now you have your forked code locally and can work on your local and remote repositories as you would on any other git project. *The only difference is the added final step of making pull requests to merge your remote fork commits into the master repository.*

- **to summarize:** [fork the master repository](https://help.github.com/en/articles/fork-a-repo) and [clone your fork onto your local machine](https://help.github.com/en/articles/cloning-a-repository).
    
- **now all we need to do is connect the two remote repositories to your local repository.** This is called *adding remotes*.
    - `cd` into the project root (eg. `cd ~/development/ProjectName/`)
    - run the command `git remote add origin <fork_url>` where `<fork_url>` is the copied URL link from your GitHub fork page.
    - run the command `git remote add upstream <master_url>` where `<master_url>` is the copied URL link from the master repo GitHub page.
    
    **Note:** if you need help doing this, [here's some](https://help.github.com/en/articles/adding-a-remote).
    **IMPORTANT NOTE:** in order for our local dev script `dev-update` to work, your origin remote must be named `origin` and your upstream remote must be named `upstream` in the commands above.
    
- **this is what the development process looks like when using a full-fledged collaborative git environment:**
    - sit down and [get ready to start coding](https://images-na.ssl-images-amazon.com/images/I/91tUjWt1uwL._SL1500_.jpg).
    - [**update**](#current-custom-scripts) your local repository with any changes that may have been added upstream (the master repository).
    - once your local code is up to date, **start development**.
    - **push your new commits** to your remote fork as needed.
    - when you would like to move your commits to the master repository, [**create a pull request**](https://www.atlassian.com/blog/bitbucket/5-pull-request-must-haves) from your remote fork. Be sure to add detailed notes on the changes you've made to the project in your pull request.

- once you have your [dependencies installed](#prerequisites-for-development) and your [remote repositories hooked into your local git repository](#hooking-up-git), you can do a one-time creation of your development environment.

#### create your local virtual dev environment

- once you have your [dependencies installed](#prerequisites-for-development) and your [remote repositories hooked into your local git repository](#hooking-up-git), follow these steps to create your own local virtual environment for development:

    - `cd` into the project root (eg. `cd ~/development/ProjectName/`)
    - in your terminal, run the command `source dev-start`.

- if you want to understand more about why we use a virtual environment for development, check out the *virtualenv* entry in the [current dev tools](#current-dev-tools) section below.

- **once you have installed your prerequisite dependencies, hooked up your git repositories, and created your local virtual environment, you are ready to start working on this project!**

    - congrats, you've now [graduated](#for-returning-developers).

### technologies we are using

#### current dev tools

- *virtualenv >= v16.0.0* - [docs](https://virtualenv.pypa.io/en/latest/) - Why do we use [virtualenv](https://www.pythonforbeginners.com/basics/python-virtualenv-usage)?

    OSX / Linux installation [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#linux-and-macos).

- *pip >= v19.1* - [docs](https://pip.pypa.io/en/stable/reference/) - How and why do we use [pip](https://www.pythonforbeginners.com/basics/how-to-use-pip-and-pypi)?

    OSX / Linux installation [here](https://pip.pypa.io/en/stable/installing/).
   
- *git* - [docs](https://git-scm.com/docs) - Why do we use [git](https://codeburst.io/number-one-piece-of-advice-for-new-developers-ddd08abc8bfa)?

    OSX installation [here](https://www.atlassian.com/git/tutorials/install-git#mac-os-x).
    
    Linux installation [here](https://www.atlassian.com/git/tutorials/install-git#linux).

#### current database

- *PostgreSQL v11.5* (aka psql, "post-grezz") - [docs](https://www.postgresql.org/docs/11/index.html) - Why do we [use PostgreSQL](https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989)?

    OSX installation [here](https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d).
   
    Ubuntu installation [here](https://tecadmin.net/install-postgresql-server-on-ubuntu/).

#### current backend

- *Django v2.2* - [docs](https://docs.djangoproject.com/en/2.2/) - Why do we [use Django](https://www.educba.com/uses-of-django/)? Why should we [use Django >=2.0](https://www.merixstudio.com/blog/Django2-how-will-it-change-Python-development/)?

- *Python 3 >= v3.7* - [docs](https://docs.python.org/3.7/) - I don't really need to explain why we're using python. It's fast, it's easy, and it's how Django works.

#### current middleware

- *django-pipeline v1.6.14* - [docs](https://buildmedia.readthedocs.org/media/pdf/django-pipeline/1.6.14/django-pipeline.pdf) - Compresses and caches static files.

- *psycopg2 v2.8.2* - [docs](http://initd.org/psycopg/docs/) - Why do we use [psycopg2](https://dba.stackexchange.com/questions/111969/what-exactly-is-psycopg2)?

    psycopg2 is Django middleware that is installed via `pip install -r requirements.txt`.

    **Note:** If you're experiencing issues installing psycopg2, check [this](https://github.com/python-pillow/Pillow/issues/3438#issuecomment-435169249) out.
    
- *babel >= v7.0* - [docs](https://babeljs.io/docs/en/) - allows us to write modern ES6+ Javascript and not worry about browser compatibility: we use Babel to transpile our ES6+ into ES5 before the deployment process.

#### current frontend

- *Bootstrap 4 v0.0.8* - [docs](https://django-bootstrap4.readthedocs.io/en/latest/index.html)

#### current deployment tools

- *Docker* - [docs](https://docs.docker.com/) - Why do we [use Docker](https://ropenscilabs.github.io/r-docker-tutorial/01-what-and-why.html)?

    [Here](https://docs.docker.com/compose/gettingstarted/) is how we use Docker to run our application in a virtual container.
    
    [Here](https://www.freecodecamp.org/news/how-to-set-up-continuous-deployment-in-your-home-project-the-easy-way-41b84a467eed/) is how we use Docker to utilize continuous integration and continuous deployment workflows.

#### current hosting services

- *Heroku* - [docs](https://devcenter.heroku.com/) - Why do we [use Heroku over AWS](https://hackernoon.com/should-i-use-heroku-or-aws-3bfcd4706a36)?

- *Amazon S3* - [docs](https://aws.amazon.com/s3/) - Why do we [use Amazon S3](https://aws.amazon.com/s3/faqs/)?

    [This](https://devcenter.heroku.com/articles/s3) is how we use Amazon S3 to host static files for our Heroku apps.
    
#### current custom scripts

- **for developer use:**
    
    - `./dev-restart` (symlinked to `./lib/scripts/restart`): **Run this whenever you want to see your local CSS and Javascript changes in your browser.** Running this script from the project root will stop the Django development server process on port 8000, execute `python manage.py collectstatic`, and restart the Django development server on port 8000. The `collectstatic` command makes copies of your CSS and Javascript files and puts them into a specific folder that Django searches through whenever the application requests CSS or Javascript files. Running `./restart` is a quick way to update this folder with your most recent code changes.
    
    - `./dev-update` (symlinked to `./lib/scripts/dev-update`): **Run this if you would like to synchronize your repositories with master.** Running this from the project root will fetch upstream changes, pull those upstream changes into your local repository, and push your local repository to your fork.
    
    - `./dev-start`: **Run with the command `source dev-start` whenever you sit down for a new development session.** Sourcing this script from the project root will do the following steps in succession: enter your virtual environment, or create and enter one if one doesn't exist; update all python and node dependencies; and finally, update your local and forked repositories with any changes from upstream.
    
    **Note:** due to the nature of scripts activating other scripts, running `./dev-start` without using `source` won't activate your virtual environment. This will cause the script to install all your python dependencies globally. Make sure you use `source` when running this script!

- **for application use:**

    - `./lib/scripts/activate`: used by `./dev-start` to activate your local virtual environment.
    - `./lib/scripts/update`: used by `./dev-start` to update your local and forked repositories with upstream changes. Also pushes any new local commits to your remote fork.

### technologies to consider

#### deployment tools

#### frontend
- *SCSS* - [docs](https://sass-lang.com/documentation) - why would we want to [use SCSS](https://alistapart.com/article/why-sass/)?

    - SCSS is a superset of CSS (which means you can write pure CSS in a `.scss` file) that allows us to use many more tools unavailable in CSS, such as variables and modules.
    - SCSS must be transpiled down to CSS before the deployment process; we can do this using the node module [scss-compile](https://www.npmjs.com/package/scss-compile), and adding a script to our `package.json`.


#### backend

#### middleware
