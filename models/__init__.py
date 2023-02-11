#!/usr/bin/python3
"""
create a unique FileStorage instance for application 
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
