#!/bin/bash

current_directory=$(pwd)

chmod +x "$current_directory/create_flutter.py"

echo "export PATH=\$PATH:$current_directory" >> ~/.zshrc

# python3 $(which create_flutter.py)