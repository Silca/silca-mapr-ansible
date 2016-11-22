from jinja2.utils import soft_unicode

####################################################################################
# Generate from a tupple of IPs a random list of the given IPs
####################################################################################
# Example in a playbook
#- hosts: localhost
#  gather_facts: yes
#  tasks:
#    - set_fact:
#        test:  "{{ ('192.168.2.3', groups['mapr-node']) | pretty_random }}"
#    - debug: var=test
####################################################################################

def randomlist(tupple):
    (node, rabbit_nodes) = (tupple[0], tupple[1])
    num = int(node.split('.')[3])
    return ','.join(map(lambda x: rabbit_nodes[x % (len(rabbit_nodes))],  range(len(rabbit_nodes))))


class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'pretty_random' : randomlist,
        }

