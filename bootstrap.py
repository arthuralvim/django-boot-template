# -*- coding: utf-8 -*-
import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
import urllib2

REPO = 'https://github.com/arthuralvim/dj-kickstart.git'
VENV = os.environ.get('WORKON_HOME', '~/.virtualenvs/')
PRO = os.environ.get('PROJECT_HOME', '~/projects/')

def extend_parser(optparse_parser):

    optparse_parser.add_option(
        "--path",
        dest="path",
        default=VENV,
        help="Parent path of virtualenvs."
    )

    optparse_parser.add_option(
        "--project",
        dest="project",
        default=PRO,
        help="Path to projects."
    )

    optparse_parser.add_option(
        '--git',
        dest='git',
        default=REPO,
        help='Location of a git repository to use for the installation.')


def adjust_options(options, args):

    if not args:
        return

    package = args[0]
    if '==' in args[0]:
        args[0], version = args[0].split('==', 1)

    PVENV = join(os.path.expanduser(options.path), args[0])
    PPRO = join(os.path.expanduser(options.project), args[0])

    # check if virtualenv path is ok
    if os.path.exists(PVENV):
        print 'Virtualenv already exists.'
        sys.exit(1)

    # check if project path is ok
    if os.path.exists(PPRO):
        print 'Project already exists.'
        sys.exit(1)

    # check if repository url exists
    try:
        urllib2.urlopen(options.git)
    except urllib2.HTTPError, e:
        print 'Problems with repository URL: {0}.'.format(e)
        sys.exit(1)
    except urllib2.URLError, e:
        print 'Problems with repository URL: {0}.'.format(e)
        sys.exit(1)

    args[0] = PVENV

def after_install(options, home_dir):

    PNAME = home_dir.split('/')[-1]
    PVENV = home_dir
    PPRO = join(os.path.expanduser(options.project), PNAME)
    PY = join(PVENV, 'bin', 'python')
    PIP = join(PVENV, 'bin', 'pip')

    os.chdir(PRO)

    # download code
    call_subprocess(['git', 'clone', options.git, PNAME], show_stdout=True)

    os.chdir(PPRO)

    # install requirements.txt
    subprocess.call([PIP, 'install', '-r', 'requirements.txt'])
    # run syncdb
    subprocess.call([PY, 'manage.py', 'syncdb', '--all', '--noinput'])
    # run migrate
    subprocess.call([PY, 'manage.py', 'migrate',])
    # run collectstatic
    subprocess.call([PY, 'manage.py', 'collectstatic', '-y',])

    print "Now run the server => python manage.py runserver or run heroku's foreman."

"""))

f = open('boot-project.py', 'w').write(output)
