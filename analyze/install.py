import importlib
import platform
import site
import subprocess
import sys
import traceback

class InstallerClass:
    sci_win = ['python', '-m', 'pip', 'install', 'scikit-learn']
    nump_win = ['python', '-m', 'pip', 'install', 'numpy']
    pan_win = ['python', '-m', 'pip', 'install', 'pandas']
    req_win = ['python', '-m', 'pip', 'install', 'requests-html']
    bs4_win = ['python', '-m', 'pip', 'install', 'beautifulsoup4']
    mat_win = ['python', '-m', 'pip', 'install', 'matplotlib']

    sci = ['python3', '-m', 'pip', 'install', 'scikit-learn']
    nump = ['python3', '-m', 'pip', 'install', 'numpy']
    pan = ['python3', '-m', 'pip', 'install', 'pandas']
    req = ['python3', '-m', 'pip', 'install', 'requests-html']
    bs4 = ['python3', '-m', 'pip', 'install', 'beautifulsoup4']
    mat = ['python3', '-m', 'pip', 'install', 'matplotlib']

    def sci_win_method(self):
        try:
            ret_sci_win = subprocess.run(self.sci_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_sci_win)
        except Exception:
            traceback.print_exc()
    def nump_win_method(self):
        try:
            ret_nump_win = subprocess.run(self.nump_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump_win)
        except Exception:
            traceback.print_exc()
    def pan_win_method(self):
        try:
            ret_pan_win = subprocess.run(self.pan_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan_win)
        except Exception:
            traceback.print_exc()
    def req_win_method(self):
        try:
            ret_req_win = subprocess.run(self.req_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_req_win)
        except Exception:
            traceback.print_exc()
    def bs4_win_method(self):
        try:
            ret_bs4_win = subprocess.run(self.bs4_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_bs4_win)
        except Exception:
            traceback.print_exc()
    def mat_win_method(self):
        try:
            ret_mat_win = subprocess.run(self.mat_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_mat_win)
        except Exception:
            traceback.print_exc()


    def sci_method(self):
        try:
            ret_sci = subprocess.run(self.sci, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_sci)
        except Exception:
            traceback.print_exc()
    def nump_method(self):
        try:
            ret_nump = subprocess.run(self.nump, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump)
        except Exception:
            traceback.print_exc()
    def pan_method(self):
        try:
            ret_pan = subprocess.run(self.pan, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan)
        except Exception:
            traceback.print_exc()
    def req_method(self):
        try:
            ret_req = subprocess.run(self.req, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_req)
        except Exception:
            traceback.print_exc()
    def bs4_method(self):
        try:
            ret_bs4 = subprocess.run(self.bs4, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_bs4)
        except Exception:
            traceback.print_exc()
    def mat_method(self):
        try:
            ret_mat = subprocess.run(self.mat, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_mat)
        except Exception:
            traceback.print_exc()

if sys.version_info[0] == 2:
  print("This installer is Python2 not supported.")

elif sys.version_info[0] == 3:
    pf = platform.system()
    if pf == 'Windows':
       InstClass = InstallerClass()
       InstClass.sci_win_method()
       InstClass.nump_win_method()
       InstClass.pan_win_method()
       InstClass.req_win_method()
       InstClass.bs4_win_method()
       InstClass.mat_win_method()

    elif pf == 'Darwin':
       InstClass = InstallerClass()
       InstClass.sci_method()
       InstClass.nump_method()
       InstClass.pan_method()
       InstClass.req_method()
       InstClass.bs4_method()
       InstClass.mat_method()

    elif pf == 'Linux':
       InstClass = InstallerClass()
       InstClass.sci_method()
       InstClass.nump_method()
       InstClass.pan_method()
       InstClass.req_method()
       InstClass.bs4_method()
       InstClass.mat_method()

    else:
       print("Installer does not support OS other than Windows, MacOS and Linux kernel.")


else:
  print("A version other than Python2 and Python3. Does not match.")

importlib.reload(site)
