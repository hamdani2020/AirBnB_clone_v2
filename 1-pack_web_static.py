#!/usr/bin/python3
"""compressed the static files"""

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """compress all the web_server
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fname = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fname))
        return fname
    except:
        return None
