#!/bin/bash

current_directory=$(pwd)

chmod +x "$current_directory/.create_flutter_project.sh"

# Add the script's directory to the PATH
export PATH="$current_directory:$PATH"

echo "Setup completed! You can now run the script by typing 'create_flutter' in the command prompt."
