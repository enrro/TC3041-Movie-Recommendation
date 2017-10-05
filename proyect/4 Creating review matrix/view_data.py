import pandas
import webbrowser
import os
import numpy as np

# dtype={'userId': np.int32, 'movieId': np.int32, 'rating': np.uint8}
# Read the dataset into a data table using Pandas
data_table = pandas.read_csv("review_matrix.csv", dtype={'userId': np.int32, 'movieId': np.int32, 'rating': np.uint8})

# clean the data
#data_table.drop('timestamp', axis=1, inplace=True)
#data_table.to_csv("ratings.csv", na_rep="")

# Create a web page view of the data for easy viewing
html = data_table.to_html()


# Save the html to a temporary file
with open("review_matrix.html", "w", encoding='utf-8') as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath("review_matrix.html")
webbrowser.open("file://{}".format(full_filename))