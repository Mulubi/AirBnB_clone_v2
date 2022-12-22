# This is a fabric script that generates a .tgz archive from
# the contents of the web_static folder of your repo and
# stores it in the versions folder:

from fabric.api import local, lcd, env
from datetime import datetime

env.hosts = ['localhost']

def do_pack():
    # Create the versions directory if it does not exist
    local("if [ ! -d versions ]; then mkdir versions; fi")

    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Create the archive name
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Change to the web_static directory
    with lcd("web_static"):
        # Create the tar file
        local("tar -czf ../versions/{} *".format(archive_name))

    # Return the path to the archive
    return "versions/{}".format(archive_name)
