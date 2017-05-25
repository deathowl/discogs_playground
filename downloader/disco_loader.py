from config import files
from downloader import grabber, extractor
import sys
print("Starting Discogs Loader")
download_manager = grabber.DownloadManager(files)
file_extractor = extractor.ExtractManager(files)
try:
    download_manager.get_files()
    print("Download finished")
    print("Extracting files")
    file_extractor.execute()
    print("Files extracted")
except KeyboardInterrupt:
    print("Killing download threads")
    download_manager.abort_downloads()
    sys.exit(1)

print("Exiting Main Thread")
