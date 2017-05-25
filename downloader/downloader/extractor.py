from config import working_dir
import gzip
import os


class ExtractManager:
    def __init__(self, urls):
        files = []
        for url in urls:
            file_name = url.split('/')[-1]
            file_path = "%s/%s" % (working_dir.rstrip("/"), file_name)
            files.append(file_path)
        self.files = files

    def execute(self):
        for compressed_name in self.files:
            base = os.path.basename(compressed_name)
            print("Decompressing %s" % base)
            dest_name = os.path.join(working_dir, base[:-3])
            with gzip.open(compressed_name, 'rb') as infile:
                with open(dest_name, 'w') as outfile:
                    for line in infile:
                        outfile.write(line)
