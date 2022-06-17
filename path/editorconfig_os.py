from os import path
import os


def make_editorconfig(dir_path):
    '''
    Create `.editorconfig` file in given dir and return the filename
    '''
    filename = os.path.joint(dir_path, '.editorconfig')
    if not os.path.exists(filename):
        os.makedirs(dir_path, exist_ok=True)
        open(filename, mode='wt').write('')
    return filename
