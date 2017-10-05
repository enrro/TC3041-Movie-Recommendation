import pandas as pd
import numpy as np

# Read the dataset into a data table using Pandas
df = pd.read_csv("ratings.csv", dtype={'userId': np.int32, 'movieId': np.int32, 'rating': np.uint8})

# Convert the running list of user ratings into a matrix using the 'pivot table' function
ratings_df = pd.pivot_table(df, index='userId', columns='movieId', aggfunc=np.max)

# Create a csv file of the data for easy viewing
ratings_df.to_csv("review_matrix.csv", na_rep="")