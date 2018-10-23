import configparser
import MySQLdb.cursors

config = configparser.ConfigParser()
#Path to your configuration file
config.read('/home/analog/quizzer.config')

def connect():
    return MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])
