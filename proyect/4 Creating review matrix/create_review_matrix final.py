import pandas as pd
import numpy as np
import os
import webbrowser

# Read the dataset into a data table using Pandas
df = pd.read_csv("ratings.csv", dtype={'userId': np.int32, 'movieId': np.int32, 'rating': np.uint8})

# Convert the running list of user ratings into a matrix using the 'pivot table' function
ratings_df = pd.pivot_table(df, index='userId', columns='movieId', aggfunc=np.max)

# Create a web page view of the data for easy viewing
html = ratings_df.to_html(na_rep="")

# Save the html to a temporary file
with open("review_matrix.html", "w", encoding='utf-8') as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath("review_matrix.html")
webbrowser.open("file://{}".format(full_filename))