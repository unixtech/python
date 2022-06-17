from pathlib import Path

'''
Function is clear before you, You have to write the code that
makes Dir if doesn't exist & make the `editorconfig` file for
good.
'''


def make_editorconfig(dir_path: str) -> str:
    path = Path(dir_path, '.editorconfig')
    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch()
    return path
