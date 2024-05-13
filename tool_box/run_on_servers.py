#!/usr/bin/python3
"""A fabric script that executes a specified script on my servers."""
from fabric.api import run, env, put
from decouple import config

env.hosts = config('SERVERS').split(',')
env.user = config('REMOTE_USER')
env.key_filename = config('SSH_PRIVATE_KEY_PATH')

def run_script(script_path):
    """Setup firewall."""

    # get file name
    file_name = script_path.split('/')[-1]
    file_path = '~/scripts/{}'.format(file_name)

    # create folder to hold scripts
    if run('mkdir -p ~/scripts').failed:
        return False
    
    # copy script to servers
    if put(script_path, file_path).failed:
        return False
    
    # confirm file is executable
    if run('chmod +x {}'.format(file_path)).failed:
        return False

    # run script
    if run(file_path).failed:
        return False
    return True
