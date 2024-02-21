import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

# Function to visualize the top goal scorers
def visualize_top_scorers(players, top_n=10):
    # Sorting players by goals to get the top scorers
    top_scorers = sorted(players, key=lambda x: x.goals, reverse=True)[:top_n]
    player_names = [player.player_name for player in top_scorers]
    goals = [player.goals for player in top_scorers]

    # Creating a bar plot for the top scorers
    plt.figure(figsize=(10, 6))
    plt.barh(player_names, goals, color='skyblue')
    plt.xlabel('Goals')
    plt.ylabel('Player Names')
    plt.title('Top Goal Scorers')
    plt.gca().invert_yaxis()  # This is to display the top scorer at the top of the bar chart
    plt.tight_layout()

    # Checking if the 'figures' directory exists, if not, create it
    if not os.path.exists('figures'):
        os.makedirs('figures')

    # Saving the figure
    plt.savefig(os.path.join('figures', 'top_scorers.png'))
    plt.close()

# Function to visualize shots vs goals by league
def visualize_shots_vs_goals(players):
    # Creating a DataFrame from the players list
    df = pd.DataFrame([vars(player) for player in players])

    # Summarizing shots and goals by league
    league_stats = df.groupby('league', as_index=False).agg({'shots': 'sum', 'goals': 'sum'})

    # Creating a scatter plot for shots vs goals using Plotly
    fig = px.scatter(league_stats, x='shots', y='goals', color='league', title='Shots vs Goals by League', size='goals', hover_name='league')

    # Checking if the 'figures' directory exists, if not, create it
    if not os.path.exists('figures'):
        os.makedirs('figures')

    # Saving the interactive plot as an HTML file
    fig.write_html(os.path.join('figures', 'shots_vs_goals_by_league.html'))

    # Displaying the plot
    fig.show()


