import time
import os
import transmissionrpc

client = transmissionrpc.Client(
    address='',
    port='',
    user='',
    password=''
    )

watch_tv = ''
watch_movie = ''
download_dir_tv = ''
download_dir_movie = ''

<<<<<<< HEAD
=======

>>>>>>> small update
def add(watch_dir, download_dir):
    watch_dir = os.listdir(watch_tv)
    if watch_dir != []:
        for i in watch_dir:
<<<<<<< HEAD
            print watch_tv + '/' + i
            client.add_torrent(watch_tv + '/' + i, download_dir=download_dir)
            time.sleep(1)
            os.remove(watch_tv + '/' + i)
            time.sleep(1)
=======
            if i.lower().endswith('.torrent'):
                client.add_torrent(watch_tv + '/' + i, download_dir=download_dir)
                time.sleep(1)
                os.remove(watch_tv + '/' + i)
                time.sleep(1)
>>>>>>> small update

while True:
    add(watch_tv, download_dir_tv)
    add(watch_movie, download_dir_movie)
<<<<<<< HEAD
    time.sleep(60)
=======
    time.sleep(60)
>>>>>>> small update
