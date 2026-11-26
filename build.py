import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "modules"))
from logger import logger
from run import run

logger.info("Building Kuroi whit cargo")
run("cargo build --release")
