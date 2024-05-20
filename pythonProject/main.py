# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Create a file path for CSV file
file_path = 'netflix_data.csv'

# Load CSV file
netflix_df = pd.read_csv(file_path, index_col= 0)

# Filter data to remove TV shows
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Only show certain columns from netflix_subset
netflix_movies = netflix_subset.loc[:, ["title", "country", "genre", "release_year", "duration"]]

# Filter movie to shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Assign colors to genre group
colors = []

for lab, row in netflix_movies.iterrows():
    if row['genre'] == "Children":
        colors.append("blue")
    elif row['genre'] == "Documentaries":
        colors.append('yellow')
    elif row['genre'] == "Stand-Up":
        colors.append('green')
    else:
        colors.append('red')

# Matplotlib figure object
fig = plt.figure(figsize=(12, 8))

# Create scatter plot
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

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
answer = "no"