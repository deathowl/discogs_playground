from __future__ import print_function
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import threading
import os
from config import working_dir


class DownloaderThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.running = True

    def run(self):
        print("Starting " + self.name)
        file_name = self.url.split('/')[-1]
        file_path = "%s/%s" % (working_dir.rstrip("/"), file_name)
        u = urlopen(self.url)
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        if os.path.isfile(file_path):
            local_size = os.path.getsize(file_path)
            if local_size == file_size:
                print("File already downloaded : %s, skipping download" % file_name)
                return
            else:
                print("File partially downloaded. Removing: %s" % file_name)
                os.unlink(file_path)
        print("Downloading: %s Bytes: %s" % (file_name, file_size))

        f = open(file_path, 'wb')
        file_size_dl = 0
        block_sz = 8192
        while self.running:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status += chr(8) * (len(status) + 1)
            print(status, end="")
        print("Download  of  %s completed" % file_name)
        f.close()
        print("Exiting " + self.name)


class DownloadManager:
    def __init__(self, files):
        self.threads = []
        self.files = files

    def get_files(self):
        for f in self.files:
            t = DownloaderThread(f)
            t.daemon = True
            t.start()
            self.threads.append(t)
        while True:
            running = False
            for t in self.threads:
                t.join(600)
                running = t.isAlive()
                if running:
                    break  # Found at least thread, that still lives, moving on
            if not running:
                print("Finished Downloading files")
                break  # No more running downloads, moving on.

    def abort_downloads(self):
        for t in self.threads:
            t.running = False
