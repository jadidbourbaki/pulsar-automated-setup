import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_info(s :str):
    print(f"{bcolors.OKGREEN}{s}{bcolors.ENDC}")

def check_shell_output(cmd : str) -> str:
    return subprocess.check_output(cmd, shell=True)