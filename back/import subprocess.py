import subprocess

def check_docker_installed():
    try:
        # Run "docker --version" command to check if Docker is installed
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Docker is installed.")
        return True
    except subprocess.CalledProcessError:
        print("Docker is not installed.")
        return False

if __name__ == "__main__":
    check_docker_installed()
