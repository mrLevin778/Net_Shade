import zipfile
import gzip
import shutil
import os

class FileCompressorDecompressor:

    def compress_zip(self, file_path, archive_path):
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, arcname=os.path.basename(file_path))

    def decompress_zip(self, archive_path, extract_path):
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            zipf.extractall(extract_path)

    def compress_gzip(self, file_path, archive_path):
        with open(file_path, 'rb') as f_in:
            with gzip.open(archive_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def decompress_gzip(self, archive_path, extract_path):
        with gzip.open(archive_path, 'rb') as f_in:
            with open(extract_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
