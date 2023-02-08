import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
office = pd.read_csv("datasets/office_episodes.csv")
office.set_index("episode_number")
fig = plt.figure()

most_views = 0.0
for i in range(188):
    x = office.loc[i, "viewership_mil"]
    if x >= most_views:
        most_views = x
        top_star_mult = office.loc[i, "guest_stars"]

top_star = ""
for n in top_star_mult:
    if n != ",":
        top_star += n
    if n == ",":
        break

colorlist = []
for j in range(188):
    scaled_ratings = office.loc[j, "scaled_ratings"]
    curr_color = ""
    if scaled_ratings < 0.25 : curr_color = "red"
    if (scaled_ratings >= 0.25 and scaled_ratings < 0.50) : curr_color = "orange"
    if (scaled_ratings >= 0.50 and scaled_ratings < 0.75) : curr_color = "lightgreen"
    if scaled_ratings >= 0.75 : curr_color = "darkgreen"
    colorlist.append(curr_color)

sizes = []
for j in range(188):
    has_guests = office.loc[j, "has_guests"]
    if has_guests == True : sizes.append(250)
    if has_guests == False : sizes.append(25)

plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")

xax = office.loc[:, "episode_number"]
yax = office.loc[:, "viewership_mil"]

plt.rcParams['figure.figsize'] = [11, 7]

plt.scatter(xax, yax, s = sizes, c = colorlist)
plt.show(fig)

