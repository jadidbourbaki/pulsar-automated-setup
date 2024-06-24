#!/usr/bin/python3

import os
import sys
import pathlib

import util

def have_miniforge():
    miniforge_dir = pathlib.Path.home() / pathlib.Path("miniforge3")
    return miniforge_dir.is_dir()

def install_miniforge(): 
    util.log_info("detecting system version")

    uname = str(util.check_shell_output("uname")).strip()
    uname_m = str(util.check_shell_output("uname -m")).strip()

    util.log_info(f"system versions - uname: {uname}, uname_m: {uname_m}")
    util.log_info("installing miniforge with detected system version")

    os.system(f"curl -L -O \"https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-{uname}-{uname_m}.sh\"")
    os.system(f"bash Miniforge3-{uname}-{uname_m}.sh")

    util.log_info("installed miniforge.")

def install_sage_math():
    util.log_info("installing sagemath")

    util.log_info("detecting python version")
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    util.log_info(f"python version: {python_version}")

    os.system(f"mamba create -n sage sage python={python_version}")

    util.log_info("activating sage-math")

    os.system("conda activate sage")

    util.log_info("done installing sagemath")

def install_pulsar():
    util.log_info("downloading pulsar from google drive")

    home = util.get_home_directory()
    util.log_info(f"detected home directory: {home}")

    file_id = "1Jazsfp2SnRaRvm3LNCXgQ1fR81Q5m8mh"
    os.system("pip install gdown")
    os.system(f"gdown {file_id} -O {home}/pulsar.zip")

    util.log_info("extracting pulsar")

    os.system(f"unzip {home}/pulsar.zip")

    util.log_info("done installing pulsar")

# This expects a folder called ~/pulsar in your home directory
def install_pulsar_requirements():
    util.log_info("installing requirements for pulsar")
    home = util.get_home_directory()
    util.log_info(f"detected home directory: {home}")

    if not pathlib.Path(f"{home}/pulsar").is_dir():
        util.log_error("could not find a folder called 'pulsar' in home directory")
        return
    
    os.system("python3 -m pip install -r {home}/pulsar/requirements.txt")
    os.system("python3 -m pip install torch torchvision torchaudio")

    util.log_info("done installing requirements for pulsar")

if __name__ == '__main__':
    if not have_miniforge():
        util.log_info("did not detect miniforge. installing miniforge.")
        install_miniforge()
        util.log_error("please close this ssh session and start a new one.")
        exit(0)

    util.log_info("detected miniforge. proceeding.")
    install_sage_math()
    install_pulsar()
    install_pulsar_requirements()
    util.log_info("all done! :-)")
    






