#!/bin/bash

# Make the main script executable
chmod +x create_flutter.sh

# Create a symbolic link to the main script with the desired command name
ln -s "$(pwd)/create_flutter.sh" /usr/local/bin/create_flutter

echo "Setup completed! You can now run the script by typing 'create_flutter' in the command prompt."
