# Create a matplotlib scatter plot of the data that contains the following attributes:

import matplotlib as plt
import numpy as np
import pandas as pd


# read csv into a dataframe so i can see data
office = pd.read_csv("datasets/office.csv")

#         A title, reading "Popularity, Quality, and Guest Appearances on the Office"
plt.title("Popularity, Quality, and Guest Appearances on the Office")

#         An x-axis label reading "Episode Number"
plt.xlabel("Episode Number")
#         A y-axis label reading "Viewership (Millions)"
plt.ylabel("Viewership (Millions)")

#     Provide name of one of the guest stars (there were multiple) who was in most watched Office ep.
#     Save it as a string in the variable top_star (e.g. top_star = "Will Ferrell")


#         A color scheme reflecting the scaled ratings (not the regular ratings) of each episode, such that:
#             Ratings < 0.25 are colored "red"
#             Ratings >= 0.25 and < 0.50 are colored "orange"
#             Ratings >= 0.50 and < 0.75 are colored "lightgreen"
#             Ratings >= 0.75 are colored "darkgreen"
colorlist = []



#         A sizing system, such that episodes with guest appearances have a marker size of 250 and episodes without are sized 25


#         Each episode's episode number plotted along the x-axis
#         Each episode's viewership (in millions) plotted along the y-axis
ep_number = []
ep_viewership = []
plt.scatter(ep_number, ep_viewership, c = colorlist)

