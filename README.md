# PowerOf10-400m
Uses data from Power of 10 to check correlation of 100m and 200m personal best between 400m personal bests of the UKs all time top 400m athletes


# Motivation
The 400m is a sprint, albeit a very long one. It is known that a fast 100m and 200m time can allow an athlete to run a faster 400m as they have a higher speed reserve and so are able to move at faster speed without fatiguing in the 400m. 
I wanted to see if this was true for the best 400m sprinters of all time in the Uk. 
This is also relevant as the UK has not managed to put together a mens 4x400 team for the olympics since 2012 and this could help show why.

# Power of 10
Power of 10 is home to all athlete data for british athletes. 
There is a 400m ranking page which includes links to athlete profiles and best perfomances of all events they have competed in so I was able to grab personal best across the 3 events.
Used to get the all time best list of 400m athlete performances in the UK.

# libraries
Selenium for webscraping.
pandas for data reading and data maniuplation.
matplotlib for plotting charts.
Seaborn for correlation matrix

# Findings
There seemed to almost always be a negative correlation between 100m personal bests and 400m personal bests. This was also the case for 200m and 400m.
It was more negative the smaller the data set.
However the standard deviation was usually very small so although negative, different 100m and 200m times did not cause 400m times to vary much

# Intepretaion
When athletes finally specialise in the 400m's, they stop competing in the 100m and 200m events so even though they might have gotten faster, their last personal best in those events is not a representation of their current shape.
It is known that some 400m athletes come down from 800m so some may not be complete sprinters but fit enough to get to the 400m mark in a fast time. This could explain the negative correlation. 
Maybe we do not have enough 'complete' sprinters actually attempting to specialise in the 400m in the UK. 
Maybe there are not enough coaoches in the UK that emphasise speed training in 400m.


Note: some athletes may have run their 100m and 200m personal best early on in their career and have not gone back to racing one so may actually be faster as they have improved in the 400m. This may emphasise the need for frequent testing on 100m and 200m times on 400m athletes in the UK.

#ranking400m.py
Gets all time 400m bests in the uk and puts them into a list.

#pb_one_two.py
Uses selenium to select on each individual athlete in the all time 400m
list and get their 100m and 200m personal bests. Populates them into a list.

#correlation.py
Plots correlation matrix using 100m, 200m and 400m lists and saves it as a png.




# Note:
data population up to athlete 45
# Sign off
Check out the plot file for the Data!!

Many thanks,
Uche
