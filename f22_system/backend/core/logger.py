from loguru import logger

logger.add(
    "file.log",
    rotation="500 MB",
    compression="zip",
    serialize=True,
    level="INFO"
)
