import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/DELL/PycharmProjects/behaveBDDhybridFrameworkwithPOM/configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get("basic info","url")
        return url

    @staticmethod
    def getBrowser():
        browser = config.get("basic info","browser")
        return browser