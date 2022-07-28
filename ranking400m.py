import pandas as pd


''' 

This file reads power of 10 400m all time ranking list the collects the athletes and their personal bests in two sepereate lists:
    *athlete_name list
    *pb400m

head value on line 21 determines the number athletes to read to. 

'''

#Reads all tables on 400m ranking list page
page_tables = pd.read_html("https://www.thepowerof10.info/rankings/rankinglist.aspx?event=400&agegroup=ALL&sex=M&alltime=y")

#There are 5 tables on webpages so selects table which contains data to be used
#To get top 25 must get first 26 rows are firt two table rows in html are tittles 
#drops 0 as first row is completely irrelevant information
ranking_table = page_tables[3]
ranking_table = ranking_table.head(8)
ranking_table = ranking_table.drop(0)

#Gets athlete column and pb column
athlete_names = ranking_table[6]
pbs = ranking_table[1]

#get athlete names into list
athlete_name_list = list(athlete_names)[1:]


#get 400m personal bests and puts them into a list
pb400m = []
for name, pb4 in zip(athlete_names[1:], pbs[1:]):
    pb400m.append(float(pb4))




