import subprocess
import platform
from utils import log

def check_docker_installed():
    try:
        # Run "docker --version" command to check if Docker is installed
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print("Docker is installed.")
        return True
    except subprocess.CalledProcessError:
        print("Docker is not installed.")
        return False

def update_libseccomp():
    try:
        # Check libseccomp2 version using apt-cache policy
        check_command = "apt-cache policy libseccomp2"
        result = subprocess.run(check_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Parse the output to get the installed version
        installed_version_line = next(line for line in result.stdout.split('\n') if 'Installed:' in line)
        installed_version = installed_version_line.split()[-1]

        # Check if the version is already 2.5.x
        if not installed_version.startswith("2.5."):
            # Update libseccomp2
            update_command = "sudo apt install libseccomp2=2.5.1-1~bpo10+1"  # You can adjust the version as needed
            subprocess.run(update_command, shell=True, check=True)
            print(f"libseccomp2 updated to version 2.5.1-1~bpo10+1. Please restart the Docker daemon and the container.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_docker_installed()
    update_libseccomp()
