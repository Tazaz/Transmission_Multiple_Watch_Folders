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
backup_dir = 'remove'


def add(watch_dir, download_dir, after):
    watch_dir = os.listdir(watch_tv)
    if watch_dir != []:
        for i in watch_dir:
            if i.lower().endswith('.torrent'):
                try:
                    client.add_torrent(watch_tv + '/' + i, download_dir=download_dir)
                    time.sleep(1)
                    if after == 'remove':
                        os.remove(watch_tv + '/' + i)
                    else:
                        os.rename(watch_tv + '/' + i, after + '/' + i)
                except:
                    print 'Unexpected error'
                time.sleep(1)

while True:
    add(watch_tv, download_dir_tv, backup_dir)
    add(watch_movie, download_dir_movie, backup_dir)
    time.sleep(60)