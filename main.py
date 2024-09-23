from backend.services.nba_variance import *
from backend.services.all_nba_data import *
from backend.services.all_nba_functions import *
from backend.services.fantasy_points_data import *
import sqlite3 

#1. scrape 
#scrapes all the nba players career averages from all the seasons they played
#scrape_nba_players_averages()

#scrapes all the nba players gamelogs from last season
#scrape_nba_players_gamelog()



# gets all the fantasy pts for all players
#get_all_fantasy_points()

# gets all the fantasy pts for each game for each player
#get_all_fantasy_points_gamelog()


# calculates nba players points variance and points consistency
#nba_players_points_variance()

# calculates nba players fantasy pts consistency
#nba_players_fantasy_pts_variance()

#fixes the player list
#nba_players_list()


# creates fantasy pts gamelog
#fantasy_pts_gamelog()



# filters the career stats, removes extra rows in a season that a player got traded
#filtered_career_stats()

#gets all fantasy points
#get_all_fantasy_points_filtered()

#print(id_list)

# gets fpts for each player first and second szn
#first_second_szn()

# plots regression for first and second season 
#plot_first_second_yr_regression()


# gets fpts for each player second and third szn
#second_third_szn()

# plots regression comparing second and third szn fpts
#plot_second_third_yr_regression()

#fix_career_stats()


#fix_career_filtered_stats()

#get_2_seasons_data(12,13)

#plot_diff_in_yr_regression(12,13)

#get_2_seasons_data_age(25,26)

#plot_diff_in_age_regression(19,20)

#get_all_rookies()

avg_10_best_games()

#injury_risk_2()

#injury_risk_3()

#filter_raw_stats()

final_data()
#get_all_predictions()
