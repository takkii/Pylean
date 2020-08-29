import traceback
import subprocess
import sys
import importlib
import site
import platform

class InstallerClass:
    py_setuptool = ['python', '-m', 'pip', 'install', '-U', 'pip', 'setuptools']
    py_update = ['python', '-m', 'pip', 'install', '--upgrade', 'pip']

    def py_up_method(self):
        try:
            py_update_win = subprocess.run(self.py_update, encoding='utf-8', stderr=subprocess.PIPE)
            print(py_update_win)
        except Exception:
            traceback.print_exc()

    def py_version(self):
        try:
            print(sys.version)
            print(sys.version_info)
        except Exception:
            tracebeck.print_exec()

    def py_setup_method(self):
        try:
            py_setup_win= subprocess.run(self.py_setuptool, encoding='utf-8', stderr=subprocess.PIPE)
            print(py_setup_win)
        except Exception:
            traceback.print_exc()

InstClass = InstallerClass()
InstClass.py_up_method()
InstClass.py_setup_method()
InstClass.py_version()
