import hdfsdata
import os

hdfs = hdfsdata.HdfsData()
hdfs.delete("/tmp/lines.html")
hdfs.copylocalfile("d:/lines.html","/tmp/")
os.remove("d:/lines.html")
hdfs.copyhdfsfile("/tmp/lines.html","d:/lines.html")