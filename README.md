# PowerOf10-400m
Uses data from Power of 10 to check correlation of 100m and 200m personal best between 400m personal bests of the UKs all time top 400m athletes
To view data switch to Master branch

# Motivation
The 400m is a sprint albeit a very long one. It is known that a fast 100m and 200m time can allow an athlete to run a faster 400m as they have a higher speed reserve and so are able to move at fater speed without fatiguing in the 400m. 
I wanted to see if this was true for the best 400m sprinters of all time in the Uk. 
This is also relevant as the UK has not managed to put together a mens 4x400 team since 2012 and this could help shop why.

# Power of 10
Power of 10 is home to all athlete data for british athletes. 
There is 400m ranking page which includes links to athlete profiles and best perfomances of all events they have competed in so I was able to grab personal best acorss the 3 events

# libraries
I used Selenium for webscraping
pandas for reading and data maniuplation
matplot lib for plotting charts 

# Findings
There seemed to almost always be a negative correlation between 100m personal bests and 400m personal bests. This was also the case for 200m and 400m.
It was more negative the smaller the data set.
However the standard deviation was usually very small so although negative, different 100m and 200m times did not cause 400m times to vary much

# Intepretaion
It is known that some 400m athletes come down from 800m so may not be complete sprinters but fit enough to get to the 400m mark in a fast time. This could explain the negative correlation. 
Maybe we do not have enough complete sprinters actually attempting to be good at the 400m in the UK. 
Maybe there are not enouhg coaoches in the UK that emphasise speed training in 400m 

Note: some athletes may have run their 100m and 200m personal best early on in their career and have not gone back to racing one so may actually be faster as they have improved in the 400m. This may emphasise the need for frequent testing on 100m and 200m times on 400m athletes in the UK.

# Note:
data population up to athlete 45
# Sign off
Check out the plot file for the Data!!

Many thanks,
Uche
