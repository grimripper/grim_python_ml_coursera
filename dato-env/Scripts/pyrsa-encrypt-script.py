#!c:\mycode\grim_python_ml_coursera\dato-env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rsa==3.1.2','console_scripts','pyrsa-encrypt'
__requires__ = 'rsa==3.1.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('rsa==3.1.2', 'console_scripts', 'pyrsa-encrypt')()
    )
