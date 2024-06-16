import os
import argparse
import time

from dotenv import load_dotenv

from camera_server import CameraServer
from config import Config
from logconf import mylogger
logger = mylogger(__name__)


def envs2config(env_path: str) -> Config:
    # load_dotenv(verbose=True)
    load_dotenv(env_path, verbose=True)
    cam_url = os.environ.get('CAMERASERVER_URL', None)
    sleep_in_loop_ms = int(os.environ.get('SLEEP_IN_LOOP_MS', 100))
    cam = CameraServer(cam_url)
    logger.info(f"CAMERASERVER_URL : {cam_url}")
    cfg = Config.from_defaults(
        cam,
        sleep_in_loop_ms
    )

    return cfg


def main(
    env_path: str
):
    cfg = envs2config(env_path)
    print(cfg)
    
    
    while True:
        time.sleep(cfg.sleep_in_loop_ms)
        
        

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='What this program is going to do.'
    )
    parser.add_argument(
        '--env_path', '-EP', type=str, default='.env', help='path for env variables'
    )
    args = parser.parse_args()

    main(args.env_path)