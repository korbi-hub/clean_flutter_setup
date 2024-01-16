#!/usr/bin/env python3

import subprocess
import asyncio
import os
import shutil
import re
import json

async def install_fvm():
    try:
        subprocess.run(['fvm', '--version'], check=True)
        print('fvm is already installed.')
    except subprocess.CalledProcessError:
        print('Installing fvm...')
        subprocess.run(['pub', 'global', 'activate', 'fvm'], check=True)
        print('fvm installed successfully.')

async def create_flutter_project(project_name):
    subprocess.run(['flutter', 'create', project_name], check=True)
    os.chdir(project_name)

async def run_fvm_use():
    subprocess.run(['fvm', 'use'], check=True)

async def modify_yaml_files():
    yaml_files = [file for file in os.listdir('.') if file.endswith('.yaml')]

    for yaml_file in yaml_files:
        with open(yaml_file, 'r') as file:
            lines = file.readlines()

        # Remove lines starting with '#' and empty lines
        lines = [line for line in lines if not re.match(r'^\s*#', line)]

        # Add 'generate: true' after 'uses-material-design: true'
        for i, line in enumerate(lines):
            if '  uses-material-design: true' in line:
                lines.insert(i + 1, '  generate: true\n')

        with open(yaml_file, 'w') as file:
            file.writelines(lines)

async def generate_file(content, path, name, generate_folder):
    if generate_folder:
        os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, name), 'w') as new_file:
        new_file.write(content)

def is_vscode_installed():
    try:
        subprocess.run(['code', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

async def main():
    script_path = os.path.dirname(os.path.abspath(__file__))
    strings_json_path = os.path.join(script_path, 'strings.json')
    makefile_path = os.path.join(script_path, 'makefile')

    project_name = input('Enter the name for the Flutter project: ')
 
    # create project and setup fvm
    await install_fvm()
    await create_flutter_project(project_name)
    await run_fvm_use()

    # generate localizations, auto_router, extensions.dart, makefile, and main file
    with open(strings_json_path, 'r') as json_file:
        files = json.load(json_file)

    for entry in files.get('files', []):
        print('\n###########################################\n Added ' + entry.get('name', '') + '\n###########################################\n')
        await generate_file(entry.get('content', ''), entry.get('path', ''), entry.get('name', ''), entry.get('create_folder', False))

    # remove comments from .yaml files
    await modify_yaml_files()

    # add + get dependencies, run code generation
    subprocess.run(['make', '-f', makefile_path, 'setup_fvm'], check=True)

    print('###########################################\n\nYour new Flutter project has been added to: ' + project_name + '\n\n###########################################')

    if is_vscode_installed():
        print(os.getcwd())
        subprocess.run(['code', '../' + project_name])

if __name__ == '__main__':
    asyncio.run(main())
