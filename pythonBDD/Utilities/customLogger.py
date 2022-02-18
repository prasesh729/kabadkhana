import logging.handlers
import logging

class LogGen:
    @
    logging.basicConfig(filename='pythonBDD/Logs/yourAppLog.log',
                        format="(asctime)s-%(message)s",
                        datefmt="%d-%b-%y",filmode="w")

    rotate_file=logging.handlers.RotatingFileHandler(
        "pythonBDD/Logs/yourApp.log", maxBytes= 1024*1024*20 back
    )

        logger =logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
        return logger