import pandas as pd

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_titles.csv')

# Display the first few rows of the dataset
print(netflix_data.head())

# Get some basic information about the dataset
print(netflix_data.info())

# Perform some basic analysis, like counting the number of movies and TV shows
print("Number of movies:", netflix_data[netflix_data['type'] == 'Movie'].shape[0])
print("Number of TV shows:", netflix_data[netflix_data['type'] == 'TV Show'].shape[0])

# Visualize some data, for example, the distribution of release years
import matplotlib.pyplot as plt

plt.hist(netflix_data['release_year'], bins=30, edgecolor='black')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.title('Distribution of Netflix Content by Release Year')
plt.show()
