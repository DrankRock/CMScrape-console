import subprocess
import time

def start_flaresolverr():
    try:
        print("Starting flaresolverr")
        # Check if a container with the name "flaresolverr" already exists
        check_existing_command = ["docker", "ps", "-aq", "--filter", "name=flaresolverr"]
        existing_container_id = subprocess.run(check_existing_command, check=True, stdout=subprocess.PIPE, text=True).stdout.strip()

        if existing_container_id:
            # Stop and remove the existing container
            stop_and_remove_command = ["docker", "rm", "-f", "flaresolverr"]
            subprocess.run(stop_and_remove_command, check=True)
            print(f"Existing container with name 'flaresolverr' stopped and removed.")

        # Docker run command to start flaresolverr
        start_command = [
            "docker", "run", "-d",
            "--name=flaresolverr",
            "-p", "8191:8191",
            "-e", "LOG_LEVEL=info",
            "--restart", "unless-stopped",
            "ghcr.io/flaresolverr/flaresolverr:latest"
        ]
        result = subprocess.run(start_command, check=True, capture_output=True, text = True)
        time.sleep(5)
        print("flaresolverr started successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error starting flaresolverr: {e}")

def stop_flaresolverr():
    try:
        # Get the container ID of flaresolverr
        container_id_command = ["docker", "ps", "--filter", "name=flaresolverr", "--format", "{{.ID}}"]
        result = subprocess.run(container_id_command, check=True, stdout=subprocess.PIPE, text=True)
        container_id = result.stdout.strip()

        # Stop and remove the flaresolverr container
        if container_id:
            stop_and_remove_command = ["docker", "rm", "-f", container_id]
            subprocess.run(stop_and_remove_command, check=True)
            print(f"flaresolverr container with ID {container_id} stopped and removed.")
        else:
            print("flaresolverr container not found.")

    except subprocess.CalledProcessError as e:
        print(f"Error stopping or removing flaresolverr: {e}")

if __name__ == "__main__":
    start_flaresolverr()

    # Wait for a moment before stopping (just for demonstration purposes)
    try:
        import requests

        url = "http://localhost:8191/v1"
        headers = {"Content-Type": "application/json"}
        data = {
            "cmd": "request.get",
            "url": "http://www.google.com/",
            "maxTimeout": 60000
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.text)
    except KeyboardInterrupt:
        print("Script interrupted. Stopping flaresolverr.")
    
    stop_flaresolverr()
