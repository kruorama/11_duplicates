import os
import ar


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Input path to folder')

    parser.add_argument(
        'dirpath',
        help='Path to a folder')
    args = parser.parse_args()
    return args

def get_files_list(dirpath):
    dirs = os.listdir(path)
    return dirs

def get_file_size(filepath):
    size = os.path.getsize(filepath)
    return size


if __name__ == '__main__':
    args = get_parser_args
    files_list = get_files_list(args.dirpath)
    print(files_list)
    print(type(files_list))
