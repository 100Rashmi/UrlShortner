import random
import string
import logging
import sys

from commons.constants import OFF_SET, CANDIDATES


class Logger:
    class __Logger:
        _logger = None

        def __init__(self):
            self.logger = logging.getLogger()
            self.logger.addHandler(logging.StreamHandler(sys.stdout))
            self.logger.setLevel(logging.INFO)

        def info(self, message):
            self.logger.info("**Adya** " + message)

        def error(self, message):
            self.logger.error("**Adya** " + message)

        def exception(self, message):
            self.logger.exception("**Adya** " + message)

        def debug(self, message):
            self.logger.debug("**Adya** " + message)

        def warn(self, message):
            self.logger.warning("**Adya** " + message)


    instance = None

    def __init__(self):
        if not Logger.instance:
            Logger.instance = Logger.__Logger()

    def __getattr__(self, name):
        return getattr(self.instance, name)



def convert_To_base_64(autoinc_id):
    autoinc_id = autoinc_id+OFF_SET
    rem = []
    quotient=0
    while autoinc_id>0:
        quotient=autoinc_id/64
        rem.append(autoinc_id%64)
        autoinc_id=quotient
    rem.reverse()
    final_encoded_str = ""
    for r in rem:
        final_encoded_str += CANDIDATES[r]
    Logger().info("final encoded url : {}".format(final_encoded_str))
    return final_encoded_str


# one time generation
def generate():
    lowercase =','.join(string.ascii_lowercase[:26]).split(",")
    upercase = ','.join(string.ascii_uppercase[:26]).split(",")
    numbers = [str(i) for i in range(0,10)]
    candidate = lowercase+upercase+numbers+["_","-"]
    random.shuffle(candidate)
