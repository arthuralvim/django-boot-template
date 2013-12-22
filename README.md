django-boot-template
====================

Just a template that I use when booting new django projects (for now only works in Python 2.7).


Usage
=====

You can build it directly:

.. code-block:: console

    django-admin.py startproject --template=https://github.com/arthuralvim/django-boot-template/archive/master.zip --extension=py,env,gitignore --name=Procfile,Makefile PROJECTNAME
    python bootstrap.py
    python boot-project.py

or you can download it and pass the template path:

.. code-block:: console
    git clone git@github.com:arthuralvim/django-boot-template.git
    django-admin.py startproject --template=path/to/django-boot-template --extension=py,env,gitignore --name=Procfile,Makefile PROJECTNAME
    python bootstrap.py
    python boot-project.py

License
=====

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
