'''
Copyright 2019-Present The OpenUBA Platform Authors
This file is part of the OpenUBA Platform library.
The OpenUBA Platform is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
The OpenUBA Platform is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with the OpenUBA Platform. If not, see <http://www.gnu.org/licenses/>.
'''

import logging
from enum import Enum

DB_CONFIG = {
    "type": "mongo"
}

class DBType(Enum):
    FS = 1
    HDFS = 2

'''
@name connector
@description this should enable the database, to be invoked using Query
'''
class Connector():
    def __init__(self, type):
        print("connector made")
        if type == "fs":
            self.type = FSConnectorType()
        elif type == "hdfs":
            self.type = HDFSConnector()
        else:
            raise Exception("Unsupported Connector type")

    def connect(self):
        self.type.attempt_to_connect()


'''
@name FSDBConnector
@description connect to flat files
'''
class FSConnector(Connector):
    def __init__(self):
        print("FS db type initiated")

    def attempt_to_connect(self):
        print("Connecting to FS")

'''
@name HDFSConnector
@description connect to HDFS
'''
class HDFSConnector(Connector):
    def __init__(self):
        print("HDFS db type initiated")

    def attempt_to_connect(self):
        print("Connecting to HDFS")




'''
@name DB
@description fundamental database parent class
'''
class DB():
    def __init__(self):
        print("db initiated")

        try:
            pass
        except Exception as e:
            logging.error(e)


'''
@name DBRead
@description read a
'''
class DBRead(DB):
    def read(self):
        logging.info("DBREAD")
        pass

'''
@name DBWrite
@description
'''
class DBWrite(DB):
    def write(self):
        logging.info("DBREAD")
        pass


'''
@name WriteNewActorToDB
@description
'''
class WriteNewActorToDB(DBWrite):
    def set(self, actor_object):
        logging.info("write_actor")
        self.write()

'''
@name ReadUserFromDB
@description
'''
class ReadActorFromDB(DBRead):
    def get(self, actor_object):
        logging.info("read_actor")
        self.read()
