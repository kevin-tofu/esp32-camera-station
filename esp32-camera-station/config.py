from dataclasses import dataclass
from camera_server import CameraServer


@dataclass
class Config():
    
    camera: CameraServer
    sleep_in_loop_ms: int
    
    @classmethod
    def from_defaults(
        cls,
        camera: CameraServer,
        sleep_in_loop_ms: int=50
    ) -> 'Config':
        return cls(
            camera=camera,
            sleep_in_loop_ms=sleep_in_loop_ms
        )
