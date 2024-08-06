# Yahtzee
## Project Overview
This project is a text-based implementation of Yahtzee. The game consists of repeatedly rolling dice, then trying to match the combination of dice to different score types. You should be able to follow the in-game prompts if you aren't familiar with Yahtzee. The source code contains a "yahtzee.cpp" file which contains the main method for the project. It also contains the header and implementation files for several classes. The group for this project consists of Jacob Seikel, Noah Lewicz, and Lee Gerken.
## Building
This project is built using CMake, using standard settings. There is a testing build set up in the "tests" directory, as well as a project build set up in the root directory.
## Testing
The unit testing for this project was implemented using Catch2. To run it, build the testing build as described below. It was not very difficult to integrate after we decided on using the amalgamated setup.
## Build Instructions
In order to build this game, you will need the CMake GUI, at version 3.26 or later. You will also need Visual Studio, preferably Visual Studio 17 2022. When the CMake GUI asks for the location of the source code, enter the directory which contains all of the program files, including CMakeLists.txt. For the build directory, we recommend creating a build folder in the same directory. After this is set up, press "Configure", then change "CMAKE_INSTALL_PREFIX" to wherever you want the installation build to go. After this, press "Open Project". Once this is done, you should be able to build the project by pressing the run button in Visual Studio. If you want to run the installation, right-click "INSTALL" in the solution explorer and select "Build". If this doesn't work, you may have to clean the build first.

The process to build the testing build is almost the same as what is listed above. The only difference is that when you are prompted for the location of the source code, you should instead select the "tests" directory.