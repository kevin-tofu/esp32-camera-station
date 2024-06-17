import os
import argparse
import time
import utils
import camera_server
from logconf import mylogger
logger = mylogger(__name__)


def main(
    env_path: str
):
    cfg = utils.envs2config(env_path)
    print(cfg)
    
    try:
        # cfg.camera.test_connection(max_attempts=-1)
        temp = cfg.camera.test_connection()
        print("temp:", temp)
    except camera_server.ServerDownException as e:
        logger.info(f"Error - {e}")
        raise Exception(f"Error - {e}")


    while True:
        time.sleep(
            float(cfg.sleep_in_loop_ms) / 1000.0
        )
        
        #Measurement Update
        
        
        #Control Update
        
        
        #Information Update
        

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='What this program is going to do.'
    )
    parser.add_argument(
        '--env_path', '-EP', type=str, default='.env', help='path for env variables'
    )
    args = parser.parse_args()

    main(args.env_path)