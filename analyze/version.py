import importlib
import platform
import site
import sys
import subprocess
import threading
import traceback

class InstallerClass(threading.Thread):
    py_setuptool = ['python', '-m', 'pip', 'install', '-U', 'pip', 'setuptools']
    py_update = ['python', '-m', 'pip', 'install', '--upgrade', 'pip']
    py_mat = ['python', '-m', 'pip', 'install', 'matplotlib']

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        try:
            py_update_win = subprocess.run(self.py_update, encoding='utf-8', stderr=subprocess.PIPE)
            py_setup_win= subprocess.run(self.py_setuptool, encoding='utf-8', stderr=subprocess.PIPE)
            py_mat_win= subprocess.run(self.py_mat, encoding='utf-8', stderr=subprocess.PIPE)
            print(py_update_win)
            print(py_setup_win)
            print(py_mat_win)
            print(sys.version)

        except Exception:
            traceback.print_exc()

thread = InstallerClass()
thread.run()
