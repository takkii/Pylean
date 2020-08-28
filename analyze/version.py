import traceback
import subprocess
import sys
import importlib
import site
import platform

class InstallerClass:
    py_update = ['python', '-m', 'pip', 'install', '--upgrade', 'pip']

    def py_up_method(self):
        try:
            py_update_win = subprocess.run(self.py_update, encoding='utf-8', stderr=subprocess.PIPE)
            print(py_update_win)
            print(sys.version)
            print(sys.version_info)
        except Exception:
            traceback.print_exc()

InstClass = InstallerClass()
InstClass.py_up_method()
