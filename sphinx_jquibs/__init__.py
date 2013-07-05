__all__ = ('__version__', '__build__','conf',)
__version__ = (0,0,1)
__build__ = ''

import os

def get_version():
    return '.'.join( map( lambda v:str(v),__version__) )

def get_html_theme_path():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]
