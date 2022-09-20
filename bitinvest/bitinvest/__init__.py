import logging
import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# This allows easy placement of apps within the interior
# apps directory.

# sys.path.append(str(BASE_DIR / "apps"))
env = environ.Env()
env_dir = os.path.join(BASE_DIR, "envs", ".env")

if os.path.exists(env_dir):
    environ.Env.read_env(env_dir)

# Logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s :: %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
