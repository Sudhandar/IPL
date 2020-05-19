import pandas as pd

matches = pd.read_csv('matches.csv')
balls = pd.read_csv('deliveries.csv')
matches.columns
matches = matches[['id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',
       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',
       'win_by_wickets', 'player_of_match', 'venue']]


rcb = matches[(matches['team1']=='Royal Challengers Bangalore')|(matches['team2']=='Royal Challengers Bangalore')]
csk = matches[(matches['team1']=='Chennai Super Kings')|(matches['team2']=='Chennai Super Kings')]

rcb_win = rcb[rcb['winner'] == 'Royal Challengers Bangalore']
rcb_lost = rcb[rcb['winner'] != 'Royal Challengers Bangalore']
#
csk_win = csk[csk['winner'] == 'Chennai Super Kings']
csk_lost = csk[csk['winner'] != 'Chennai Super Kings'] 

rcb_los_mom = pd.DataFrame(rcb_lost['player_of_match'].value_counts(ascending=False))
csk_win_mom = pd.DataFrame(csk_win['player_of_match'].value_counts(ascending=False))

rcb_los_toss = pd.DataFrame(rcb_lost['toss_winner'].value_counts(ascending=False))
csk_los_toss = pd.DataFrame(csk_lost['toss_winner'].value_counts(ascending=False))

rcb_loss 



