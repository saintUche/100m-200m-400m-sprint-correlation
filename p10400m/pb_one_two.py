from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

from ranking400m import athlete_name_list
from ranking400m import pb400m




chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.thepowerof10.info/rankings/rankinglist.aspx?event=400&agegroup=ALL&sex=M&alltime=y")


'''
Function takes athlete name and opens their profile on power 10 and returns their 100m and 200m personal bests.
some 400m athletes do not have 100m or 200m personal best so in this case the value returned is 0
'''
def add_100m_and_200m_pb(athlete_name, driver):
    
    link = driver.find_element(By.LINK_TEXT, athlete_name)
    profile = link.get_attribute('href')
    
    num_of_tables = len(pd.read_html(profile))

    #no of tables on athlete page vary from 22-24  in each case the correct table is selected
    target_table = 11
    
    if num_of_tables == 23:
        target_table = 12
    if num_of_tables == 24:    
        target_table = 13

    pb_table = pd.read_html(profile)[target_table]
    
    event_col = pb_table[0]
    result_col = pb_table[1]

    pb100m = 0
    pb200m = 0

    #removes windy personal and indoor personal bests, removes i and w from indoor and windy personal bests respectively
    for event , result in  zip(event_col, result_col):
        if event == "100":
            result = list(result.split("/"))[0]

            if result.endswith("w"):
                result = result.rstrip("w")
            
            if result.endswith("i"):
                result = result.rstrip("i")
   
            pb100m = float(result)

        if event == "200":
            result = list(result.split("/"))[0]

            if result.endswith("w"):
                result = result.rstrip("w")            
            
            if result.endswith("i"):
                result = result.rstrip("i")
            
            
            pb200m = float(result)

    return pb200m, pb100m





pb100m = []
pb200m = []

# for each athlete add their 100m and 200m personal best to the corresponding position of their 400m personal best
for athlete in athlete_name_list:
   print(athlete)
   result = add_100m_and_200m_pb(athlete, driver)
   pb200m.append(result[0])
   pb100m.append(result[1])    


#If an athlete does not have a 100m or 200m personal best then remove their 400m pb and 100m and 200m to prevent skewing the data
zeros = [] 
for x, y in zip(pb100m, pb200m):
        if (x == 0) or (y == 0):
            pos = pb100m.index(x)
            zeros.append(pos)

for zero in zeros:
    pb100m.pop(zero)
    pb200m.pop(zero)
    pb400m.pop(zero)




