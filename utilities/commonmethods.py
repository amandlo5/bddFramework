from datetime import datetime


def generateEmailRandom():
    time_stmp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amolmandloi"+time_stmp+"@gmail.com"