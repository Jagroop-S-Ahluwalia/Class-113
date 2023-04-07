import os
import shutil
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


dir_tree = {"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p',
                                                                                       '.m4v', '.avi', '.mov'], "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']}


from_dir =r"C:\Users\jagsm\Downloads"

to_dir =r"C:\Users\jagsm\Downloads\class133e"

class Jagroop(FileSystemEventHandler):
    def on_created(self, event):
        name,extenstion=os.path.splitext(event.src_path)

        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)

            if extenstion in value:
                file_name = os.path.basename(event.src_path)

                print('downloaded ' + file_name )



                path1 = from_dir+'/'+file_name
                path2 = to_dir+'/'+key
                path3 = to_dir+'/'+key+'/'+file_name


                if os.path.exists(path2):
                    print('moving '+ file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)

                else:
                    os.makedirs(path2)
                    print('moving '+ file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)


myEventHandler = Jagroop()

myobserver = Observer()

myobserver.schedule(myEventHandler,from_dir,recursive=True)

myobserver.start()

try:
    while True:
        time.sleep(1)
        print("code is running...")

except KeyboardInterrupt:
    print('stopped')
    myobserver.stop()