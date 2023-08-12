from fm_pack.crawl_dirs import get_dir_info
from fm_pack.create_json import create_json
from fm_pack.csv_to_json import csv_to_json
from fm_pack.json_to_csv import save_to_csv
from fm_pack.txt_to_json import convert_to_json

if __name__ == '__main__':
    get_dir_info(get_dir_info('/fm_pack/test_dir/output.json'))

    convert_to_json('fm_pack/test_dir/input.txt', 'fm_pack/test_dir/output.json')

    create_json('/fm_pack/test_dir/data1.json')

    save_to_csv('/fm_pack/test_dir/data1.json', '/fm_pack/test_dir/data.csv')

    csv_to_json('/fm_pack/test_dir/data.csv', '/fm_pack/test_dir/data2.json')
