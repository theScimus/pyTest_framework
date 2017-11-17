import json
import os


CONFIG_FILE = "config/config.json"


class Config(object):

    def __init__(self):
        print(os.path.abspath(CONFIG_FILE))
        self.__read_config(CONFIG_FILE)

    def __read_config(self, file):
        self.configuration = json.loads(open(file).read())

