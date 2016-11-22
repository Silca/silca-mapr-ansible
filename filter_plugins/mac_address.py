from jinja2.utils import soft_unicode
from ansible.utils.hashing import md5s, checksum_s

def mac_address(value):
    """
    Generate a Mac address from a String (used for kvm mac adress and proxmox).
    """
    _md5string = md5s(value)
    return ':'.join(["02" , _md5string[0:2], _md5string[2:4], _md5string[4:6], _md5string[6:8], _md5string[8:10]])

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'mac_address': mac_address,
        }
