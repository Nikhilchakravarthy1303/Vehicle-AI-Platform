import logging
import os
from pathlib import Path


def setup_logging():

    logger = logging.getLogger("VehicleAIPlatform")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    default_log_path = "vehicle_incidents.log"

    log_path = os.getenv(
        "LOG_FILE_PATH",
        default_log_path
    )

    Path(log_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file_handler = logging.FileHandler(log_path)

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger