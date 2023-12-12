#!/usr/bin/python3
'''create unique FileStorage instance for your application'''
from models.engine.file_storage import FileStorage

'''Variable storage, an instance of FileStorage'''
storage = FileStorage()
storage.reload()
