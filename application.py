import sys
#
## The "/home/StokBook1" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/StokBook1/myproject"
path = '/home/StokBook1/OutMed-F/flaskr'
if path not in sys.path:
    sys.path.append(path)

from flaskr import create_app
application = create_app() # noqa
application.run(port='65454')