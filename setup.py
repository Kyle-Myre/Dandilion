from cx_Freeze import setup, Executable

files = ['static/Icon.ico','static/']
build_options = {'packages': [], 'excludes': [] , 'include_files' : files}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(
        script='src/main.py', 
        base=base, target_name = 'Dandilion' , 
        icon='static/Icon.ico'
    )
]

setup(
    name='Dandilion',
    version = '1.0',
    description = 'Dandilion',
    options = {'build_exe': build_options},
    executables = executables
)
