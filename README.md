# giant-bomb-cli
Python CLI for searching the giant bomb public API and show DLC for returned games, sorted by release date

## Clone this repository to your machine

1. `git clone git@github.com:prasanna12510/giant-bomb-cli.git`

## Set up virtual environment

1. `cd giant-bomb-cli`

2. `virtualenv venv`

3. `source ./venv/bin/activate` nix systesm `\venv\bin\activate` windows

4. `pip install -r requirements.txt`

## Run script

    python giant_bomb_cli.py --search=[keyword in game title] --file=[path to save results file]

    python giant_bomb_cli.py --gid=[game_id retrieved from search] --showdlc=[true/false, display dlc of returned game]


#### AWS CLI-Architecture

![Alt text](https://github.com/prasanna12510/giant-bomb-cli/blob/main/doc/lambdafunction.png?raw=true "AWSArchitecture")
