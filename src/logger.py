import logging
import logging.config

logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
    )

    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")
    logging.critical("This is critical")

    try:
        a = [1, 2, 3]
        a[4]
    except Exception as e:
        logging.error(str(e), exc_info=True)  # Capture  stack trace
