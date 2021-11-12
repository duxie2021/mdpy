import argparse
from compiler import compiler


def parse_args():
    parser = argparse.ArgumentParser(description='mdpy ...')
    parser.add_argument('--note-directiony', '-d', required=True, help='note directiony')
    parser.add_argument('--file', '-f', default=None, required=False, help='file')
    parser.add_argument('--assets-repository-path', default=None, required=False, help='assets repository path')
    parser.add_argument('--assets-folder-path', default=None, required=False, help='assets folder path')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    compiler.compile(args.note_directiony, args.file, args.assets_repository_path, args.assets_folder_path)
