django-project-template
====================

Just a template that I use when booting new django projects (for now only works in **Python 2.7** and **Django 1.6**).


Usage
=====

You can build it directly:

    django-admin.py startproject --template=https://github.com/arthuralvim/django-project-template/archive/master.zip --extension=py,html,env,gitignore,sublime-project --name=Procfile,Makefile PROJECTNAME
    python bootstrap.py
    python boot-project.py

or you can download it and pass the template path:

    git clone git@github.com:arthuralvim/django-project-template.git
    django-admin.py startproject --template=path/to/django-project-template --extension=py,html,env,gitignore,sublime-project --name=Procfile,Makefile PROJECTNAME
    python bootstrap.py
    python boot-project.py

License
=====

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

Version 1, January 2014

Copyright (C) 2014 Arthur Alvim <afmalvim@gmail.com>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
