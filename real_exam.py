# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'real_exam.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice=''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the NBA TOP 20 players database, according to google\n\n'
                        'Type the letter for the information you want out of my database: \n'
                        'A: All players detail\n'
                        'B: Players who are Centres (abbreviated as "C")\n'
                        'C: Players who are Power Forwards (abbreviated as "PF")\n'
                        'D: Players who are Point Guard (abbreviated as "PG")\n'
                        'E: Players who are Small Forward (abbreviated as "SF")\n'
                        'F: PLayers who are Shooting Guard (abbreviated as "SG")\n'
                        'G: Players who have not won any championship or non-new Nba fans call it "Ring"\n'
                        'H: Players who have won a championship and their point per game\n'
                        'I: This is the stats for all players\n'
                        'J: This is the players who averaged 20 points per game or nba fans call it ppg\n'
                        'K: Players with 4 or more NBA championship\n'
                        'L: Players with over 5,000 career assist, with championship and over 10,000 career points\n'
                        'M: The team that the player is in when hes playing his best\n'
                        'N: Top_scorer players\n'
                        'O: players who have 30000 or over career_points\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all datas')
    elif menu_choice == 'B':
        print_query('C_players')
    elif menu_choice == 'C':
        print_query('PF_players')
    elif menu_choice == 'D':
        print_query('PG_players')
    elif menu_choice == 'E':
        print_query('SF_players')
    elif menu_choice == 'F':
        print_query('SG_players')
    elif menu_choice == 'G':
        print_query('no_championship')
    elif menu_choice == 'H':
        print_query('player_championship')
    elif menu_choice == 'I':
        print_query('player_stats')
    elif menu_choice == 'J':
        print_query('players_20ppg')
    elif menu_choice == 'K':
        print_query('players_4championship')
    elif menu_choice == 'L':
        print_query('players_assist_points_champion')
    elif menu_choice == 'M':
        print_query('players_team')
    elif menu_choice == 'O':
        print_query('30000_points')
