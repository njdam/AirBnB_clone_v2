#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local, runs_once
from os import path, mkdir, stat


@runs_once
def do_pack():
    """A Function that pack all static files into Archives."""
    if not path.isdir("versions"):
        mkdir("versions")

    # Making of  the archive file name by retrieving and using current time
    current_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
    )

    # Trying to pack the all web static files into archives
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archive_size = stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception:
        output = None
    return output
