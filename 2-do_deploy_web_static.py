#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.90.15.228", "35.153.66.157"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
    archive_path (str): Path to the archive file.

    Returns:
    bool: True if all operations have been done correctly, False otherwise.
"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress archive to /data/web_static/releases/<archive>
        archive_filename = os.path.basename(archive_path)
        new_archive = os.path.splitext(archive_filename)[0]
        releases_path = '/data/web_static/releases/'
        run('mkdir -p {}{}'.format(releases_path, new_archive))
        run('tar -xzf /tmp/{} -C {}{}'.format(archive_filename, releases_path, new_archive))

        # Move the contents of the archive to the proper location
        run('mv {}{}/web_static/* {}{}'.format(releases_path, new_archive, releases_path, new_archive))

        # Remove unnecessary directories
        run('rm -rf {}{}/web_static'.format(releases_path, new_archive))

        # Remove the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Remove the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked to the new version
        run('ln -s {}{} /data/web_static/current'.format(releases_path, new_archive))

        return True

    except Exception as e:
        return False
