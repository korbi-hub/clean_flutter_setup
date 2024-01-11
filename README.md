# Create Flutter Projects Without the Default Boilerplate Code
At some point, Google decided that the default command for creating a new Flutter application contains an already working app but doesn't offer any options of **not** doing so. Therefore, everyone who creates a new Flutter project has to go through the tedious process of removing the boilerplate code by hand. Don't get me wrong - boilerplate code can be useful - but the default Flutter boilerplate code sadly is not.

Because deleting every unnecessary line of code and comment in the `pubspec.yaml`, `main.dart`, and `analysis_options.yaml` seemed unnecessary and redundant to me, I decided to write a shell script containing *actually useful* boilerplate code.

Note: This script has only been tested on a Mac. Linux should probably also work, but for Windows, a different solution is needed. If I feel like it at some point, I will code some scripts for Windows.

# Contained Files, Code, and Dependencies
This repository contains three main components: `setup.sh`, `create_flutter.sh`, `create_flutter.py`, a `makefile`, and `strings.json`.

## `setup.sh`
The setup script serves the purpose of adding an executable command for the creation script to PATH and adding the necessary rights to `create_flutter.sh`.

## `create_flutter.sh`
Simply executes a Python script.

## `strings.json`
Here you can specify your desired content for your new Flutter application. Simply add/edit objects by using the following JSON scheme:

```json
{
    "name": "file_name.dart",
    "path": "./path/from/project/root",
    "create_folder": true, 
    "content": "file content"
}
```

The bool "create_folder" should be set to true if you want to create a new file within subfolders (e.g., ./lib/screens/auth_guard.dart). If you simply want to edit a file already contained in the generated Flutter code, simply pass false.

## `makefile`
Run flutter commands after all files have been added.

## `create_flutter.py`
This script is the main component, which contains almost all of the magic going on behind the scenes. Its steps are the following:

1. Ask the user to provide a project name for the new Flutter project.
2. Check for an existing instance of [FVM](https://fvm.app/) and initiates the installation process, if it is not already installed. 
3. Create a Flutter project at the specified location.
4. Iterate over all entries contained in `strings.json` and create the respective files at the specified locations.
5. Install dependencies for 
    5.1. [flutter_bloc](https://pub.dev/packages/flutter_bloc)
    5.2. [intl](https://pub.dev/packages/intl) (Note: The version is currently hardcoded to be 0.18.1, because of dependency issues)
    5.3. [auto_route](https://pub.dev/packages/auto_route)
    5.4. [flutter_localizations](https://pub.dev/packages/flutter_localization)
    5.5. [auto_route_generator](https://pub.dev/packages/auto_route_generator)
    5.6. [build_runner](https://pub.dev/packages/build_runner)
    5.7. [json_serializable](https://pub.dev/packages/json_serializable)
6. Run `fvm flutter pub get`
7. Generate the localizations and the `auto_route` code.

# Setup and Execution
To use create_flutter directly from the command line, place the repository's content in a folder at your desired location and run bash setup.sh. This will make create_flutter.sh an executable and provide the command create_flutter for you to use anywhere on your machine. After executing setup.sh, restart your terminal and you are ready to go.

From now on you can create a new Flutter project, you can simply navigate to the location where you want to create your new Flutter project, type create_flutter in your command prompt, provide a project name, select your desired version of FVM, and you're ready to go.

# Additional Comments
This script creates files which I subjectively assume to be useful. If you e.g. prefer Riverpod to Bloc, you can simply edit the makefile below the TODO comment. Furthermore, you can add new files to be generated/remove files that are being generated in strings.json using the scheme I provided above.

I hope you find this to be useful. Happy coding!
