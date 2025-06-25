import logging
import logging.config
from pythonjsonlogger import jsonlogger

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    logHandler = logging.StreamHandler()
    logHandler.setFormatter(
        jsonlogger.JsonFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(logHandler)

    logger.debug("This is debug", extra={"more_data": True})
    logger.info("This is info")
    logger.warning("This is warning")
    logger.error("This is error")
    logger.critical("This is critical")

    try:
        a = [1, 2, 3]
        a[4]
    except Exception as e:
        logger.error(str(e), exc_info=True)  # Capture  stack trace
