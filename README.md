# dboilerplate3

[![Join the chat at https://gitter.im/esmorga/dboilerplate3](https://badges.gitter.im/esmorga/dboilerplate3.svg)](https://gitter.im/esmorga/dboilerplate3?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

dboilerplate3 is a django template for setting up projects quickly, based in python 3 and django 1.11. There are two options to use it:

* Install it from the repository:

Clone the repository to your computer and run afterwards this command:

    $ django-admin startproject --template=/path/to/the/template <your_project_name>

* Install it from GitHub

This is the easiest way to install the template

    $ django-admin startproject --template=https://github.com/esmorga/dboilerplate3/archive/master.zip <your_project_name>

You can get a good grip of how this boilerplate works by looking the
[documentation](http://dboilerplate3.readthedocs.org/en/latest/)

## Requirements
- Django 1.11.x
- Python 3.6.x

PLEASE NOTE: This boilerplate is still in development, the documentation
is not finished yet. You can help us if you want!

D-Boilerplate is a simple django boilerplate that we use at Havas Worldwide London to speed up our development process.

Features:

- Foundation 6 (Foundation Sites)
- Embedded sitemaps
- SCSS/JS via grunt
- Muti environment requirements files
- Multi environment settings files
- Database data generator (for development stage, thanks Kaleidos)
- Improved logging mechanism


## Grunt Readme

You will need grunt, bower and compass installed for this boilerplate uses SCSS syntax for the CSS compiling

### Requirements

- Ruby 2.3+
- NodeJS 7.7.x

To install the required tools do (as root):

    # npm install -g bower grunt grunt-cli
    # gem install compass

#### After that enter the project and run

    $ npm install
    $ npm update
    $ bower install
    $ bower update
    $ grunt
    $ ./manage.py collectstatic


#### Building project

From frontend folder run...

    'grunt' - Build js and CSS files
    'watch' - Watch for changes to js or CSS files

#### Copyright

You're free to copy, modify and distribute this code under the MIT license.

(c) 2014-2017 Esmorga Software
