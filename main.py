import os
import sys
from argparse import ArgumentParser
from pathlib import PurePath

import fitz


def split(src_file: str, dst_file: str, from_page: int, to_page: int):
    with fitz.open(src_file) as src, fitz.open() as dst:
        dst.insert_pdf(src, from_page=from_page, to_page=to_page)
        dst.save(dst_file)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-d', '--dir')
    args = parser.parse_args()
    src_dir = args.dir
    dst_dir = f'{src_dir}/result'

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for file in os.listdir(src_dir):
        if not file.endswith('.pdf'):
            continue

        path = PurePath(src_dir, file)
        print(path)

        split(str(path), f'{dst_dir}/{path.name}', 0, 0)
