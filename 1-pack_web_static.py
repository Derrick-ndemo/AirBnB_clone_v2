#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.

from fabric.api import local, env
import time
import os

env.hosts = ['localhost']


def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive.

    Returns:
        (str): Archive path if generated correctly, None otherwise.
    """
    timestamp = time.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    try:
        local("tar -czvf {} web_static/".format(archive_path))
        return archive_path
    except Exception as e:
        return None
