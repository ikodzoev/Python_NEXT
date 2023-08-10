from fm_pack.gen_files import gen_files
from fm_pack.sort_files import sort_files
from fm_pack.rename_files import rename_files

if __name__ == '__main__':
    gen_files("txt", 'fm_pack', 6, 30, 256, 4096, 42)
    gen_files("mp4", 'fm_pack', 6, 30, 256, 4096, 42)
    rename_files('new_name', 5, 'txt', 'dest_ext', )
    sort_files('fm_pack')
