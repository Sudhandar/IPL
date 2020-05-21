import pandas as pd

matches = pd.read_csv('matches.csv')
balls = pd.read_csv('deliveries.csv')
matches.columns
matches = matches[['id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',
       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',
       'win_by_wickets', 'player_of_match', 'venue']]


test = balls[:1000]

runs = balls.groupby('batsman')['batsman_runs'].transform('sum')
runs = pd.merge(balls,runs,left_index = True, right_index = True, how = 'inner')
runs = runs[['batsman','batsman_runs_y']].drop_duplicates()
runs.columns = ['batsman','runs']

balls_faced = balls.groupby('batsman')['batsman'].transform('count')
balls_faced = pd.merge(balls,balls_faced,left_index = True, right_index = True, how = 'inner')
balls_faced = balls_faced[['batsman_x','batsman_y']].drop_duplicates()
balls_faced.columns = ['batsman','balls_faced']


batsman = pd.merge(runs,balls_faced,on='batsman',how='inner')
batsman['strike_rate'] = (batsman['runs']/batsman['balls_faced'])*100
