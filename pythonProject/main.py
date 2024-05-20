import pandas as pd
import matplotlib.pyplot as plt

# Create a file path for CSV file
file_path = 'netflix_data.csv'

# Load CSV file
netflix_df = pd.read_csv(file_path, index_col= 0)

# Filter data to remove TV shows
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# Only show certain columns from netflix_subset
netflix_movies = netflix_subset.loc[:, ["title", "country", "genre", "release_year", "duration"]]

# Filter movie to shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Assign colors to genre group
colors = []

for lab, row in short_movies.iterrows():
    if "Children" in row['genre']:
        colors.append("blue")
    elif "Documentaries" in row['genre']:
        colors.append('yellow')
    elif "Stand-Up" in row['genre']:
        colors.append('green')
    else:
        colors.append('red')

# Matplotlib figure object
fig = plt.scatter(short_movies['release_year'], short_movies['duration'], c=colors)

# Add labels
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")

# Set display options to show more columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
answer = "yes"