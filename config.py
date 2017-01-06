#!/usr/bin/python
import configparser

"""
    Class config  reads configuration file
"""

class Config:
# Configuration file initializer method
  def __init__(self, filename=""):
    self.config = configparser.RawConfigParser()
    if not filename:
      self.config.read("config.properties")
    else:
      self.config.read(filename)
# Method to read property
  def readConfig(self,section,property):
    try:
      return self.config.get(section, property)
    except configparser.NoOptionError:
        raise

