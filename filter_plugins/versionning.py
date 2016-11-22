
def major_minor(value):
    return '.'.join([ version(0)(value), version(1)(value)])

def major_minor_patches(value):
    return '.'.join([ version(0)(value), version(1)(value), version(2)(value)])

def version(position):
    def version_parser(value):
        return value.split('.')[position]
    return version_parser

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'major': version(0),
            'minor': version(1),
            'patch': version(2),
            'major_minor': major_minor,
            'major_minor_patches': major_minor_patches,
        }
