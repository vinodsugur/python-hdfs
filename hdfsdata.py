#!/usr/bin/python

import hdfs
import config
import os

"""
Class to connect, read and write hadoop filesystem
"""

class HdfsData:
    #Initialize Hadoop environment connection details
    def __init__(self):
        configFile = config.Config()
        self.environment=configFile.readConfig("hdfs","environment")
        #Connect to Hadoop
        self.client = hdfs.Config().get_client(self.environment)
    #Method to delete file from Hadoop
    def delete(self,filename):
        self.client.delete(filename,recursive=True)
    #Method to copy data in Hadoop
    def copylocalfile(self,sourcefile,targetfile):
        self.client.upload(targetfile, sourcefile, overwrite=False, n_threads=1, temp_dir=None, chunk_size=65536, progress=None,
               cleanup=True)
    def copyhdfsfile(self,sourcefile,targetfile):
        self.client.download(sourcefile, targetfile, overwrite=False, n_threads=1, temp_dir=None)

