import time
from enum import Flag, auto
from dataclasses import dataclass
import requests
from logconf import mylogger
logger = mylogger(__name__)


class CameraStatus(Flag):
    working = auto()
    notworking = auto()
    unchecked = auto()


class ServerDownException(Exception):
    def __init__(self, server, message="Server is down"):
        self.server = server
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} for {self.server}"


@dataclass
class CameraServer():
    
    url: str
    api_image: str = 'image'
    status: CameraStatus = CameraStatus.unchecked
    timeout: int=3
    
    @classmethod
    def from_defaults(
        cls,
        url: str
    ) -> 'CameraServer':
        cls(url)
    
    def test_connection(self, max_attempts: int=5):
        
        print('max_attempts', max_attempts)
        if max_attempts < -1:
            return CameraStatus.unchecked

        attempts = 0
        while attempts < max_attempts:
            time.sleep(float(200 / 1000.0))
            logger.info(f" {str(attempts + 1)}-th trail to connect with")
            try:
                response = requests.get(
                    f"{self.url}/healthCheck",
                    timeout=self.timeout
                )
                logger.info(response.status_code)
                response.raise_for_status()
                # if response.status_code == 200:
                self.status = CameraStatus.working
                return CameraStatus.working
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempts + 1} failed: {e}")
                attempts += 1

        raise ServerDownException(
            self.url,
            f"Failed to connect {self.url} after {max_attempts} attempts"
        )
