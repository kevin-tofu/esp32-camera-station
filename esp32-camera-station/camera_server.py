from dataclasses import dataclass


@dataclass
class CameraServer():
    
    url: str
    api_image: str = 'image'
    
    @classmethod
    def from_defaults(
        cls,
        url: str
    ) -> 'CameraServer':
        cls(url)