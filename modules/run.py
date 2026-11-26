import subprocess
from logger import logger

def run(s):
    logger.info(f"Running {s}")
    subprocess.run(s, shell=True)
