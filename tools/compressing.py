import brotli

class BrotliCompressor:
    def compress(self, data):
        return brotli.compress(data)

    def decompress(self, data):
        return brotli.decompress(data)
