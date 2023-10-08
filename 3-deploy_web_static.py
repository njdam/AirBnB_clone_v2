#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local, runs_once, put, run, env
from os import path, mkdir, stat

# List of host server's IP Addresses
env.hosts = ["52.72.28.52", "100.26.239.179"]


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


def do_deploy(archive_path):
    """This function distribute an archive to the web servers."""
    # If path is not exists return false
    if (path.isfile(archive_path) is False):
        return (False)
    # Declaring filename, foldername, and folder path in servers
    filename = path.basename(archive_path)
    foldername = filename.replace(".tgz", "")
    folderpath = "/data/web_static/releases/{}/".format(foldername)

    # We start here by declaring the deploying success to be equal to False
    result = False
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(filename))
        # Making folder path directories
        run("mkdir -p {}".format(folderpath))
        # Extraction by decompressing tgz file to be saved in folder path
        run("tar -xzf /tmp/{} -C {}".format(filename, folderpath))
        # Deleting the archive with name as filename
        run("rm -rf /tmp/{}".format(filename))
        # Moving all files in web_static to it's root directory
        run("mv {}web_static/* {}".format(folderpath, folderpath))
        # Force deleting web static folder
        run("rm -rf {}web_static".format(folderpath))
        # Force removing /data/web_static/current
        run("rm -rf /data/web_static/current")
        # Linking folder path (new release) to current folder
        run("ln -s {} /data/web_static/current".format(folderpath))
        # Is it deployed, True if not return False
        print("New version deployed!")
        result = True
    except Exception:
        result = False
    return (result)


def deploy():
    """A function that deploy or distributes an archive to web servers."""
    archive_path = do_pack()
    return (do_deploy(archive_path) if archive_path else False)
