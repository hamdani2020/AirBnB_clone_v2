#!/usr/bin/python3
"""compressed the static files"""

from fabric.api import local
import os
from datetime import datatime

def do_pack():
    """compress all the content in the web_static into
    .tgz archive
    """
    if not os.path.exists("version")

