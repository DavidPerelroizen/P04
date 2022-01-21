# CHESS TOURNAMENT MANAGER

The chess tournament manager is a program aiming at helping the organization an management
of chess tournaments. The program enables the user to operate the following actions:
- Create a tournament
- Add players
- Register the matches results
- Update rankings
- Generate several reports

## Installation

Below the instructions will be given to properly proceed to the needed packages installing.

### Virtual environment configuration

**Install the virtual environment package**

```bash
pip install virtualenv
```

**Create the virtual environment**

```bash
virtualenv localdir
```

You must specify the local directory path

**Activate the virtual environment**

Mac OS/Linux
```bash 
source localdir/bin/activate
```

Windows
```bash
localdir/Scripts/activate
```

### Install the necessary packages

Tiny DB
```bash
pip install tinydb
```

Flake8
```bash
python -m pip install flake8
```

Flake8 html report
```bash
pip install flake8-html
```

## Usage

### Launch the program

Use your terminal to trigger the program by executing the main.py file
```bash
python main.py
```

### Main menu selection

From the main menu, select the desired function by pressing the appropriate key + enter
```bash
                CHESS APPLICATOR
            --------------------------------------------
                    MAIN MENU
            --------------------------------------------
            1. Tournament manager --> press T
            2. Complete a saved tournament with players
                and rounds --> press C
            3. Complete a saved tournament with rounds
                --> press S
            4. Complete a saved tournament with the
                missing rounds --> M
            5. Reports --> press R
            6. Update player rank --> U
            7. Exit program --> press X
            --------------------------------------------
            Press the appropriate key + ENTER :
```
Functions descriptions:
1. ***Tournament manager*** : enables the user to create and play a tournament
2. ***Complete a saved tournament with players and rounds*** : enables the user to get a tournament that was created
    with minimal data (date, name, time controller, etc...) from the database and continue the process by adding the 
    players and playing the rounds
3. ***Complete a saved tournament with rounds*** : enables the user to get a tournament that was created with the 
    players' data from the database and continue the process by playing the rounds
4. ***Complete a saved tournament with the missing rounds*** : enables the user to get a tournament that was created 
    with the players' data and some rounds from the database and continue the process by playing the missing rounds
5. ***Reports*** : access to the reporting menu
6. ***Update player rank*** : enables the user to update the ranking of a specific player directly in the database
7. ***Exit program*** : stops the main program


### Reporting menu selection

From the reporting menu, select the desired report by pressing the appropriate key + enter
```bash
                CHESS APPLICATOR
        --------------------------------------------
                      REPORTING MENU
        --------------------------------------------
        1. All players list --> press A
        2. Players of a tournament list --> press P
        3. All tournaments list --> press T
        4. Tournament all rounds list --> press R
        5. Tournament all matches list --> press M
        6. Back to main menu --> press B
        --------------------------------------------
            Press the appropriate key + ENTER :
```
Functions descriptions:
1. ***All players list*** : enables the user to display all the players existing in the database
2. ***Players of a tournament list*** : enables the user to display the player of a specific tournament (the tournament
exact name will be requested)
3. ***All tournaments list*** : enables the user to display all the existing tournaments
4. ***Tournament all rounds list*** : enables the user to display the rounds information of a specific tournament (the 
tournament exact name will be requested)
5. ***Tournament all matches list*** : enables the user to display the matches of a specific tournament (the tournament
exact name will be requested)
6. ***Back to main menu*** : enables the user to go back to the main menu


## Flake8 set-up and checks

### Flake 8 configuration

In the project directory, create a file as follows:
```bash
setup.cfg
```

In this file, write the following:
```bash
[flake8]
max-line-length = 119
exclude = venv, __init__.py, *.json, *.txt
```
We restrict the maximum number of characters per line at 119. So flake8 won't consider as errors a line as long as it
has fewer characters.
We exclude from the flake8 checks the followings:
- Our virtual environment libraries
- Our packages init files
- Our tiny databases
- Our requirement file


### Execute flake8 report

In case the user requests a regular flake8 check on the terminal, proceed as follows:
```bash
flake8 path/to/project/directory
```

In case a html reporting is preferred, proceed as follows:
```bash
flake8 --format=html --htmldir=flake-report
```