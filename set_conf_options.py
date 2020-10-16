import argparse
import os
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='Set options in conf.py.')
    parser.add_argument('--author', type=str, help='Document author', required=True)
    inputs = parser.parse_args()
    author = inputs.author
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf.py")
    year = str(datetime.now().strftime('%Y'))

    file_conf_in = open(conf_path, "r").readlines()
    file_conf_out = open(conf_path, "w", encoding="utf-8")
    for line in file_conf_in:
        if line.find("# ***___set_copyright___***") != -1:
            file_conf_out.write("copyright= u'" + year + ", "+author+"'\n")
        elif line.find("# ***___set_author___***") != -1:
            file_conf_out.write(
                "author = "+author+"\n")
        else:
            file_conf_out.write(line)
    file_conf_out.close()


if __name__ == '__main__':
    main()
