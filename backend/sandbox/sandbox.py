import docker
import logging
import time

import config

class Sandbox:
    """
    This class creates a sandbox environment using docker containers.

    It imports the code as an environment variable.

    """

    def __init__(self, code: str):
        self.code = code

        # Prepare execution output
        self.stdin = None
        self.stdout = None
        self.stderr = None
        self.status_code = None

    def run(self, input: str = ""):
        """ Runs the code with the provided input.

        Saves the program outputs as members of this object.
        Attributes
        ----------
        input : str
            Program input.
        """
        self.stdin = input

        # Run the sandbox docker container
        client = docker.from_env()
        container_config = {
            'image': "python3_sandbox",
            'detach': True,
            'environment': {
                'USER_CODE': self.code,
                'USER_INPUT': input 
            }
        }

        container = client.containers.run(**container_config)
        logging.info("Started container ID:", container.id)

        # Stop the container after the set timeout
        start_time = time.time()
        while container.status == "running":
            if time.time() - start_time > config.SANDBOX_TIMEOUT_S:
                logging.info("Stopping the container. Timeout exceeded.")
                container.stop()
            time.sleep(1)

        # Delete the container
        container.remove()
        logging.info("Container removed.")

        # Capture the sandbox output
        self.stdout = container.logs().decode('utf-8')
        self.stderr = container.attrs['State']['ExitCode']

    def status_code(self) -> int:
        return self.status_code

    def stdout(self) -> str:
        return self.stdout
    
    def stderr(self) -> str:
        return self.stderr
    
    def stdin(self) -> str:
        return self.stdin