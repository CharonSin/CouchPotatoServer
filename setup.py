from esky import bdist_esky
from setuptools import setup
import sys
import version
import os


# Include proper dirs
base_path = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(base_path, 'libs')

sys.path.insert(0, base_path)
sys.path.insert(0, lib_dir)

def getDataFiles(dirs):
    data_files = []
    for directory in dirs:
        for root, dirs, files in os.walk(directory):
            print files
            if files:
                for filename in files:
                    if filename[:-4] is not '.pyc':
                        data_files.append((root, [os.path.join(root, filename)]))

    return data_files

# Windows
if sys.platform == "win32":
    import py2exe

    FREEZER = 'py2exe'
    FREEZER_OPTIONS = dict(
        compressed = 0,
        bundle_files = 3,
        dll_excludes = [
            'MSVCP90.dll',
            'mswsock.dll',
            'powrprof.dll',
            'USP10.dll',
        ],
        packages = ['couchpotato', 'libs'],
        includes = [
            'telnetlib',
            'xml.etree.ElementTree',
            'xml.etree.cElementTree',
            'xml.dom',
            'xml.dom.minidom',
            'netrc',
            'csv',
        ],
        skip_archive = 1,
    )
    exeICON = 'icon.ico'
    DATA_FILES = getDataFiles([r'.\\couchpotato', r'.\\libs'])


# OSX
elif sys.platform == "darwin":
    import py2app

    FREEZER = 'py2app'
    FREEZER_OPTIONS = dict(
        argv_emulation = False,
        iconfile = 'icon.icns',
        plist = dict(
            LSUIElement = True,
        ),
        packages = ['couchpotato', 'libs'],
        includes = [
            'telnetlib',
            'xml.etree.ElementTree',
            'xml.etree.cElementTree',
            'xml.dom',
            'xml.dom.minidom',
            'netrc',
            'csv',
        ],
    )
    exeICON = None
    DATA_FILES = ['icon.png']

# Common
NAME = "CouchPotato"
APP = [bdist_esky.Executable("Desktop.py", name = NAME, icon = exeICON,)]
ESKY_OPTIONS = dict(
    freezer_module = FREEZER,
    freezer_options = FREEZER_OPTIONS,
    bundle_msvcrt = True,
)

# Build the app and the esky bundle
setup(
    name = NAME,
    scripts = APP,
    version = version.VERSION,
    data_files = DATA_FILES,
    options = dict(bdist_esky = ESKY_OPTIONS),
)

