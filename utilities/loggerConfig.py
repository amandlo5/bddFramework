import logging


class LogGen:
    @staticmethod
    def logGen():
        logger = logging.getLogger()

        fhandler = logging.FileHandler(
            filename="C:/Users/DELL/PycharmProjects/behaveBDDhybridFrameworkwithPOM/Logs/bddlog")
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s", datefmt="%m/%d/%Y %I:%M:%S")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.INFO)
        return logger
