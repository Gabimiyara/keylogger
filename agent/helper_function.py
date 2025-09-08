import os
import platform

def get_hostname():
    hostname = os.environ.get('COMPUTERNAME') or os.environ.get('HOSTNAME')
    if hostname:
        return hostname
    return platform.node()

