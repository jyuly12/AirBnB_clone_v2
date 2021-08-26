#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive 
from the contents of the web_static folder
"""


def do_pack():
    """Defines do_pack class that compresses web_static files"""
    from fabric.api import local
    from datetime import datetime
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        file_name = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None