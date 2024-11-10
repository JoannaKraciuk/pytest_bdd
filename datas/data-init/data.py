import configparser
import os
import os.path

URL_INI = "\\url.ini"

class UrlPaths:

    def __init__(self):
        self.path = os.path.dirname(__file__) + "\\url.ini"
        self.data = configparser.ConfigParser(interpolation=None)
        self.data.read(self.path)

    def get_dict_path_for_page(self, _section):
        return dict(self.data[_section])

class PageDatas:

    def __init__(self, file_name):
        self.data = configparser.ConfigParser(interpolation=None)
        self.data.read(self.path, encoding='UTF-8')

    def get_dict_section(self, _section):
        return dict(self.data[_section])

    def get_key_values(self, _section, _key):
        return list(filter(None, (x.strip() for x in self.data.get(_section, _key).splitlines())))

    def get_value(selfself, _section, _key):
        return self.data.get(_section, _key)



