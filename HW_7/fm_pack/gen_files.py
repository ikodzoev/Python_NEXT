import os
import random
import string


def gen_files(extension: str, directory: str, min_name_len: int = 6, max_name_len: int = 30, min_bytes: int = 256,
              max_bytes: int = 4096, num_files: int = 42):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(num_files):
        name_len = random.randint(min_name_len, max_name_len)
        name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_len))
        filename = f"{name}.{extension}"
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                num_bytes = random.randint(min_bytes, max_bytes)
                f.write(os.urandom(num_bytes))


def gen_files_with_exts(extensions: dict, directory: str, min_name_len: int = 6, max_name_len: int = 30,
                        min_bytes: int = 256, max_bytes: int = 4096):
    for ext, num_files in extensions.items():
        gen_files(ext, directory, min_name_len, max_name_len, min_bytes, max_bytes, num_files)


# gen_files("txt", 'test_dir', 6, 30, 256, 4096, 42)
