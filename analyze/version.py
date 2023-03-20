"""import module"""
import sys
import threading
import traceback
import subprocess


class InstallerClass(threading.Thread):
    """InstallerClass"""
    py_setuptool = [
        'python', '-m', 'pip', 'install', '-U', 'pip', 'setuptools'
    ]
    py_update = ['python', '-m', 'pip', 'install', '--upgrade', 'pip']

    def __init__(self):
        threading.Thread.__init__(self)

        def run(self):
            try:
                py_update_win = subprocess.run(self.py_update,
                                               encoding='utf-8',
                                               stderr=subprocess.PIPE)
                py_setup_win = subprocess.run(self.py_setuptool,
                                              encoding='utf-8',
                                              stderr=subprocess.PIPE)
                print(py_update_win)
                print(py_setup_win)
                print(sys.version)

            except Exception:
                traceback.print_exc()


thread = InstallerClass()
thread.run()
