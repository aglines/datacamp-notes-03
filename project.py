# Create a matplotlib scatter plot of the data that contains the following attributes:
import matplotlib as plt
import numpy as np
import pandas as pd
########################### DATA STRUCTURES PREP

##initalize a matplotlib.pyplot fig object, which you can do using the code fig = plt.figure()
fig = plt.figure()
##A title, reading "Popularity, Quality, and Guest Appearances on the Office"
plt.title("Popularity, Quality, and Guest Appearances on the Office")
##An x-axis label reading "Episode Number"
plt.xlabel("Episode Number")
##A y-axis label reading "Viewership (Millions)"
plt.ylabel("Viewership (Millions)")

##Find  ONE of the guest stars (there were many) in MOST watched Office ep, Save it as  top_star
# find most watched ep,

max
#   find names of guest stars in that ep, pick one randomly
top_star = ""

##A color scheme reflecting the scaled ratings (not the regular ratings) of each episode, such that:
##Ratings < 0.25 are colored "red" ,  Ratings >= 0.25 and < 0.50 are colored "orange"
##Ratings >= 0.50 and < 0.75 are colored "lightgreen"  Ratings >= 0.75 are colored "darkgreen"

# color list is a dict, so I could ...define it for each dtpt AS i genearte it OR ... ADD COLUMN to orig dt ,,,?

colorlist = {}


##Sizing system, such that episodes with guest appearances have a marker size of 250 and episodes without are sized 25

#size argument is an nparray when given in the plot call, but .. how to seu it

#         Each episode's episode number plotted along the x-axis
#         Each episode's viewership (in millions) plotted along the y-axis
ep_number = []
ep_viewership = []


###################### MAIN
# read csv into a dataframe so i can see data
office = pd.read_csv("datasets/office.csv")


plt.scatter(ep_number, ep_viewership, c = colorlist)

plt.show()