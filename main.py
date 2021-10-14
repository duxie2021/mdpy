import argparse
from compiler import compiler


def parse_args():
    parser = argparse.ArgumentParser(description='mdpy ...')
    parser.add_argument('--note-directiony', '-d', required=True, help='note directiony')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    compiler.compile(args.note_directiony)
