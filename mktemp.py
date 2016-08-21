#!/usr/bin/env python
import click
import datetime
import os
import platform
import shutil
import sys

IS_WINDOWS = (platform.uname()[0].lower() == 'windows')

if IS_WINDOWS:
    TEMP_FOLDER = os.path.expandvars("%TEMP%")
else:
    TEMP_FOLDER = "/tmp"

WORKSPACE = os.path.join(TEMP_FOLDER, "workspaces")
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
NOW = datetime.datetime.now().strftime("%H-%M-%S")

def ensure(path):
    if not os.path.exists(path):
        os.mkdir(path)
        
@click.command()
@click.option('-r', '--raw', is_flag=True)
def main(raw):
    """
    Create a workspace under "<your_temp>/workspaces/<todays_date>/<current_time>". If you're
    on Windows, an Explorer window pointing to it will open.
    
    Use the "-r/--raw" argument to just print the path on its own and not open a window (on Windows).
    You can then use this like so: "cd $(mktemp -r)" to make a temp folder & navigate to it in one go.
    """
    ensure(WORKSPACE)
    today_space = os.path.join(WORKSPACE, TODAY)
    ensure(today_space)
    new_workspace = os.path.join(today_space, NOW)
    ensure(new_workspace)
    if raw:
        click.echo("{0}".format(new_workspace))
    else:
        click.echo("Created a new workspace at: {0}".format(new_workspace))
        if IS_WINDOWS:
            import subprocess
            subprocess.Popen('explorer "{0}"'.format(new_workspace))
    
    
if __name__ == '__main__':
    sys.exit(main() or 0)