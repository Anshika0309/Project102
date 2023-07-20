import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "D:\Books"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_moved(self, event):
        print(f"{event.src_path} file has been moved or renamed!")

    def on_modified(self, event):
        print(f"Looks like file {event.src_path} has been upgraded!")        


event_handler = FileEventHandler()
observe = Observer()
observe.schedule(event_handler, fromdir, recursive=True)
observe.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observe.stop()        



