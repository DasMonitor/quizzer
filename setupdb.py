#!/usr/bin/python3
#Dependecies
# Download the following package from: 
# https://dev.mysql.com/downloads/connector/python/
# dpkg -i mysql-connector-python-cext_2.1.7-1ubuntu14.04_amd64.deb 


from __future__ import print_function
from datetime import date, datetime, timedelta
from time import sleep
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'questions'
#DB_NAME = 'deal_test'

cnx = mysql.connector.connect(user='root', password='think1@3$')
cursor = cnx.cursor()

#typically we try to connect with error handling
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET utf8".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME  
    print("Connected to DB {}.".format(DB_NAME))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
#end typically


TABLES = {}
TABLES['biochem'] = (
    "CREATE TABLE `biochem` ("
    "  `qid` int(11) NOT NULL AUTO_INCREMENT,"
    "  `question` varchar(4096) NOT NULL,"
    "  `choices` varchar(2048) NOT NULL,"
    "  `answers` varchar(2048) NOT NULL,"
    "  `num_right` int(32) NOT NULL,"
    "  `num_wrong` int(32) NOT NULL,"
    "  `image_dir` varchar(256),"
    "  PRIMARY KEY (`qid`)"
    ") ENGINE=InnoDB")

TABLES['histo'] = (
    "CREATE TABLE `histo` ("
    "  `qid` int(11) NOT NULL AUTO_INCREMENT,"
    "  `question` varchar(4096) NOT NULL,"
    "  `choices` varchar(2048) NOT NULL,"
    "  `answers` varchar(2048) NOT NULL,"
    "  `num_right` int(32) NOT NULL,"
    "  `num_wrong` int(32) NOT NULL,"
    "  `image_dir` varchar(256),"
    "  PRIMARY KEY (`qid`)"
    ") ENGINE=InnoDB")

#TABLES['watchlist'] = (
#    "CREATE TABLE `watchlist` ("
#    "  `item_no` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `name` varchar(64) NOT NULL,"
#    "  `upc` varchar(12) NOT NULL,"
#    "  `sku` int(32) NOT NULL,"
#    "  `msrp` int(12) NOT NULL,"
#    "  `salePrice` int(12) NOT NULL,"
#    "  `storeId` int(12) NOT NULL,"
#    "  `status` varchar(20) NOT NULL,"
#    "  `last_seen_date` date NOT NULL,"
#    "  `webUrl` varchar(256) NOT NULL,"
#    "  `imageUrl` varchar(256) NOT NULL,"
#    "  `requestId` varchar(256) NOT NULL,"
#    "  `productId` varchar(32) NOT NULL,"
#    "  `categoryId` varchar(64) NOT NULL,"
#    "  `email` varchar(64) NOT NULL,"
#    "  PRIMARY KEY (`item_no`)"
#    ") ENGINE=InnoDB")
#
#
#TABLES['walmart_clearance'] = (
#    "CREATE TABLE `walmart_clearance` ("
#    "  `item_no` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `name` varchar(64) NOT NULL,"
#    "  `upc` varchar(12) NOT NULL,"
#    "  `sku` int(32) NOT NULL,"
#    "  `msrp` int(12) NOT NULL,"
#    "  `salePrice` int(12) NOT NULL,"
#    "  `last_seen_date` date NOT NULL,"
#    "  `webUrl` varchar(256) NOT NULL,"
#    "  PRIMARY KEY (`item_no`)"
#    ") ENGINE=InnoDB")
#
#TABLES['walmart_categories'] = (
#    "CREATE TABLE `walmart_categories` ("
#    "  `cat_index` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `cat_id` varchar(64) NOT NULL,"
#    "  `cat_name` varchar(256) NOT NULL,"
#    "  PRIMARY KEY (`cat_index`)"
#    ") ENGINE=InnoDB")
#
#
#TABLES['store_data'] = (
#    "CREATE TABLE `store_data` ("
#    "  `storeId` int(11) NOT NULL,"
#    "  `state` varchar(2) NOT NULL,"
#    "  `zip` int(9) NOT NULL,"
#    "  `address` varchar(512) NOT NULL,"
#    "  `city` varchar(128) NOT NULL,"
#    "  `country` varchar(64) NOT NULL,"
#    "  `phone` varchar(32) NOT NULL,"
#    "  PRIMARY KEY (`storeId`)"
#    ") ENGINE=InnoDB")






#TABLES['target_deals'] = (
#    "CREATE TABLE `deals` ("
#    "  `item_no` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `name` varchar(64) NOT NULL,"
#    "  `upc` varchar(12) NOT NULL,"
#    "  `dcpi` varchar(32) NOT NULL,"
#    "  `msrp` int(12) NOT NULL,"
#    "  `salePrice` int(12) NOT NULL,"
#    "  `storeId` int(12) NOT NULL,"
#    "  `status` varchar(20) NOT NULL,"
#    "  `last_seen_date` date NOT NULL,"
##    "  `webUrl` varchar(256) NOT NULL,"
##    "  `imageUrl` varchar(256) NOT NULL,"
#    "  `requestId` varchar(256) NOT NULL,"
#    "  `productId` varchar(32) NOT NULL,"
#    "  PRIMARY KEY (`item_no`)"
#    ") ENGINE=InnoDB")

#TABLES['departments'] = (
#    "CREATE TABLE `departments` ("
#    "  `dept_no` char(4) NOT NULL,"
#    "  `dept_name` varchar(40) NOT NULL,"
#    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
#    ") ENGINE=InnoDB")
#
#TABLES['salaries'] = (
#    "CREATE TABLE `salaries` ("
#    "  `emp_no` int(11) NOT NULL,"
#    "  `salary` int(11) NOT NULL,"
#    "  `from_date` date NOT NULL,"
#    "  `to_date` date NOT NULL,"
#    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
#    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
#    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#    ") ENGINE=InnoDB")
#
#TABLES['dept_emp'] = (
#    "CREATE TABLE `dept_emp` ("
#    "  `emp_no` int(11) NOT NULL,"
#    "  `dept_no` char(4) NOT NULL,"
#    "  `from_date` date NOT NULL,"
#    "  `to_date` date NOT NULL,"
#    "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
#    "  KEY `dept_no` (`dept_no`),"
#    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
#    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
#    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#    ") ENGINE=InnoDB")
#
#TABLES['dept_manager'] = (
#    "  CREATE TABLE `dept_manager` ("
#    "  `dept_no` char(4) NOT NULL,"
#    "  `emp_no` int(11) NOT NULL,"
#    "  `from_date` date NOT NULL,"
#    "  `to_date` date NOT NULL,"
#    "  PRIMARY KEY (`emp_no`,`dept_no`),"
#    "  KEY `emp_no` (`emp_no`),"
#    "  KEY `dept_no` (`dept_no`),"
#    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
#    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
#    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#    ") ENGINE=InnoDB")
#
#TABLES['titles'] = (
#    "CREATE TABLE `titles` ("
#    "  `emp_no` int(11) NOT NULL,"
#    "  `title` varchar(50) NOT NULL,"
#    "  `from_date` date NOT NULL,"
#    "  `to_date` date DEFAULT NULL,"
##    "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
#    "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
#    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#    ") ENGINE=InnoDB")
#
#After we successfully create or change to the target database and setup our tables dictionary
# we now iterate over the items of the TABLES dictionary and create tables in the db

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

#Close our cursor, and close our connection
cursor.close()
cnx.commit()
cnx.close()
