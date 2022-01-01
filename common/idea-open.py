import os
import argparse
from termcolor import colored

momo_base_dir = '/Users/momo/IdeaProjects'
atour_base_dir = '/Users/momo/IdeaProjects/atour'


def find_dir(base_dir, target, exact_match=False):
    result = []
    for file in os.listdir(base_dir):
        if exact_match and target == file or not exact_match and target in file:
            abs_path = '/'.join([base_dir, file])
            pom_file_path = '/'.join([abs_path, 'pom.xml'])
            if os.path.exists(pom_file_path):
                result.append(abs_path)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name', help='project to open with idea.')
    parser.add_argument('-e', '--exact', action='store_true', help='exact match')
    args = parser.parse_args()

    projects = []
    projects.extend(find_dir(momo_base_dir, args.project_name, args.exact))
    projects.extend(find_dir(atour_base_dir, args.project_name, args.exact))
    if len(projects) == 1:
        print(colored('\n'.join(projects), 'green'))
        os.system('open -a IntelliJ\ IDEA {}'.format(projects[0]))
    elif len(projects) > 1:
        print(colored('\n'.join(projects), 'green'))
    else:
        print(colored('nothing matched !', 'red'))


main()
