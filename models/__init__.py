#!/usr/bin/python3
"""init a storage object.

   If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   iniy a database storage engine (DBStorage).
   or, init a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()