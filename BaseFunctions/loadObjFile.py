from configparser import ConfigParser


def config_parser():
    cfg = ConfigParser()
    cfg.read('../FilesDirectory/objectConfig.ini', encoding="utf8")
    return cfg
