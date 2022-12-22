#!/usr/bin/python3
# This is a fabric script that generates a .tgz archive from
# the contents of the web_static folder of your repo and
# stores it in the versions folder:
from fabric.api import local, lcd, env
from datetime import datetime


def do_pack():
    # Create the versions directory if it does not exist
    local("if [ ! -d versions ]; then mkdir versions; fi")

    # Get the current date and time
    dt = datetime.utcnow()
    
    # Create the archive name
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
								 dt.month,
								 dt.day,
								 dt.hour,
								 dt.minute,
								 dt.second)
    # Change to the web_static directory
    with lcd("web_static"):
        # Create the tar file
        local("tar -cvzf {} web_static".format(archive_name))

    # Return the path to the archive
    return archive_name
