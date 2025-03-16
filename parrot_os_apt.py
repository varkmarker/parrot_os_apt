from colr import Colr as colr
import os
import sys

class Colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))
    def green(data):
        print(colr().hex("#00ff8d", data, rgb_mode=True))
    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))

def check_root_permission():
    # Check if the script is being run with root privileges
    if os.geteuid() != 0:
        Colors.red("\n THIS SCRIPT REQUIRES ROOT PERMISSIONS. PLEASE RUN WITH 'sudo'.\n")
        sys.exit(1)
    else:
        Colors.red("\n YOU HAVE ROOT PERMISSIONS.\n")
        Colors.red("\n DOWNLOADING THE [ .deb ] FILE\n")
        os.system('wget https://deb.parrot.sh/parrot/pool/main/p/parrot-archive-keyring/parrot-archive-keyring_2024.12_all.deb')
        Colors.red("\n INSTALLING THE PACKAGE \n")
        os.system('wget https://deb.parrot.sh/parrot/pool/main/p/parrot-archive-keyring/parrot-archive-keyring_2024.12_all.deb')
        Colors.red("\n UPDATE THE REPOSITORYS\n")
        os.system('sudo apt update')
        Colors.green("\n HAVE A GREAT DAY! \n HAPPY HACKING \n")


if __name__ == "__main__":
    check_root_permission()
