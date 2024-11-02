import os

class FileFragmenter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.fragments = []

    def assemble(self, fragment_dir):
        if not os.path.exists(fragment_dir):
            raise FileNotFoundError(f"Directory '{fragment_dir}' not found.")

        with open(self.filepath, 'wb') as outfile:
            for filename in sorted(os.listdir(fragment_dir)):
                fragment_path = os.path.join(fragment_dir, filename)
                with open(fragment_path, 'rb') as infile:
                    outfile.write(infile.read())

    def unassemble(self, fragment_dir, fragment_size=1024):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File '{self.filepath}' not found.")

        os.makedirs(fragment_dir, exist_ok=True)
        with open(self.filepath, 'rb') as infile:
            fragment_num = 0
            while True:
                chunk = infile.read(fragment_size)
                if not chunk:
                    break
                fragment_path = os.path.join(fragment_dir, f"fragment_{fragment_num:04d}")
                with open(fragment_path, 'wb') as outfile:
                    outfile.write(chunk)
                fragment_num += 1
