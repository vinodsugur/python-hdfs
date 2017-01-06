# python-hdfs

Pre-requisite
Python version 3.5.1
+ module hdfs
+ module configparser

Configure ".hdfscli.cfg" as per hadoop distribution host and url.

Hadoop distribution with protocol httpfs enabled. In case if port is other than 14000 then do modify the ".hdfscli.cfg". 

Please note that protocol webhdfs is also supported but since this was tested on mapr which only supports httpfs hence mentiond about httpfs.

config.properties is a text file which defines the property.
module config.py has class Config which has methods to reads the property file.
module hdfsdata.py has class HdfsData which has methods to upload, download and delete files from HDFS.
script test.py has defined test cases.

Avro file writing is in-progress, and will be part of next release.
