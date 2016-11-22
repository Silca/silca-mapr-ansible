from jinja2.utils import soft_unicode

def volume_name(number):
    if number < 1 or number > 26:
        raise ValueError('Bad volume letter for drive, should be between 1 and 26 !!')
    return chr(96 + number)

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'volume_name': volume_name,
        }
