#!/usr/bin/python3

import os
import sys
import util

def install_sage_math(): 
    util.log_info("detecting system version")

    uname = util.check_shell_output("uname")
    uname_m = util.check_shell_output("uname -m")

    util.log_info(f"system versions - uname: {uname}, uname_m: {uname_m}")

    util.log_info("detecting python version")
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    util.log_info(f"python version: {python_version}")

    util.log_info("installing sage-math with detected system and python version")

    os.system(f"curl -L -O \"https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-{uname}-{uname_m}.sh\"")
    os.system(f"bash Miniforge3-{uname}-{uname_m}.sh")

    os.system(f"mamba create -n sage sage python={python_version}")

    util.log_info("activating sage-math")

    os.system("conda activate sage")

    util.log_info("done installing sagemath")




