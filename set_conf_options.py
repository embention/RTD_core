import argparse
import os
import shutil
from datetime import datetime


def get_project_title(path_index):
    with open(os.path.join(path_index, "index.rst"), "r", encoding="utf-8") as index_file:
        previous_line = ""
        for line in index_file.readlines():
            if "****" in line or "####" in line or "====" in line:
                if ".." not in previous_line[0:2] and not previous_line[0:1].isspace() and "####" not in previous_line and "****" not in previous_line and not previous_line.isspace() and "====" not in previous_line and previous_line:
                    return ' '.join(previous_line.replace("\n", "").replace("\t", "").split())
            previous_line = line
    return ""


def main():
    parser = argparse.ArgumentParser(description='Set options in conf.py.')
    parser.add_argument('--author', type=str, help='Document author', required=True)
    parser.add_argument('--project_path', type=str, help='RTD Project path', required=True)
    inputs = parser.parse_args()
    author = inputs.author
    project_path = inputs.project_path
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf.py")
    static_path_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_static")
    static_path_dst = os.path.join(project_path, "_static")
    shutil.copytree(static_path_src, static_path_dst)
    year = str(datetime.now().strftime('%Y'))

    # Get project settings
    dir_conf_path = project_path.split(os.sep)
    project = get_project_title(project_path)
    if not project:
        if dir_conf_path[-2][:7] == "RTD_UM-":
            project = dir_conf_path[-2].replace("RTD_UM-", "")
        else:
            project = dir_conf_path[-2].replace("RTD-", "")
    language = dir_conf_path[-1]
    file_conf_in = open(conf_path, "r").readlines()
    file_conf_out = open(os.path.join(project_path, "conf.py"), "w", encoding="utf-8")
    for line in file_conf_in:
        if line.find("# ***___set_copyright___***") != -1:
            file_conf_out.write("copyright= u'" + year + ", "+author+"'\n")
        elif line.find("# ***___set_author___***") != -1:
            file_conf_out.write(
                "author = '"+author+"'\n")
        elif line.find("# ***___set_project___***") != -1:
            file_conf_out.write(
                "project = '" + project + "'\n")
        elif line.find("# ***___set_language___***") != -1:
            file_conf_out.write(
                "language = '" + language + "'\n")
        else:
            file_conf_out.write(line)
    file_conf_out.close()


if __name__ == '__main__':
    main()
