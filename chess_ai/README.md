# CS 4200 Final Project: Chess AI
## Eric Lykins, Jacob Seikel, and Remington Ward

This project attempts to solve the problem of creating an AI to play chess. This file explains how to run all our relevant code; for more project details, see the report.

### Search Tree Approach
To run the testing file, adjust the constants in testing.py as desired, then issue the command ```python testing.py```. The tests will then print to output files. This may take some time to run depending on your parameters.

### Machine Learning Approach
We are also trying a machine learning Approach. We create a convolutional nueral network (CNN) that ranks moves given a chess position. To create the CNN run all cells in code/machine_learning/cnn_training.ipynb. This creates the model that is used in machine_learning/ai_cnn.py


### How to Run the code
1. Clone this repository. 

2. Navigate to the code folder. 

3. Install all the requirements in requirements.txt.
    - run `pip install -r requirements.txt`

4. To adjust which AI you are playing, open main.py. There are constants for the following near the top of the file. Adjust them as you like.
    - CONSOLE_OUTPUT : If true the output for the game is displayed in the terminal
    - PYGAME_OUTPUT : If true the output for the game is displayed as a GUI.
    - WHITE : Sets the AI for white. If it is None, you play that color.
    - BLACK : Sets the AI for black. If it is None, you play that color.

6. run the program
    - run `python main.py`