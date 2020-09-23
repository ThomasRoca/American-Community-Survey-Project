import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
from IPython.display import display
import numpy as np
import requests
import json
        
# API given by US census bureau
api_key=""

# here we chose "Total households with a broadband subscription which code is S0201_308E
indicator="S0201_308E"

# we want Total population, white, Black or African American and Hispanic or Latino
popgroup1="001"
popgroup2="002"
popgroup3="004"
popgroup4="400"

# here is the geography level : Metropolitan statistical area and micropolitan area
# reference: https://www.census.gov/programs-surveys/metro-micro/about.html
geo="metropolitan%20statistical%20area/micropolitan%20statistical%20area:*"

# endpoint of the API
url="https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,"+indicator+"&for="+geo+"&POPGROUP="+popgroup1+"&POPGROUP="+popgroup2+"&POPGROUP="+popgroup3+"&POPGROUP="+popgroup4+"&key="+api_key
print(url)

response = requests.get(url)
data = json.loads(response.text)

# Save a Pandas DataFrame
df=pd.DataFrame(data[1:], columns=data[0])
# values are stored as string, we need to convert them into numbers
df['S0201_308E']=df['S0201_308E'].astype(float)

#save as csv
df.to_csv('ACS_broadband.csv')

#display table sorted by metro area
display(df.sort_values(["NAME"]))


# let's get data for Seattle-Tacoma-Bellevue metro area
Seattle=df.loc[df["NAME"]=="Seattle-Tacoma-Bellevue, WA Metro Area"].copy()

# code and label for population group 
pop_group_dict= {"001":"Total population", 
                 "002": "White alone", 
                 "400": "Hispanic or Latino",
                 "004": "Black or African American"}

Seattle["Population group"]=Seattle["POPGROUP"].map(pop_group_dict)
Seattle=Seattle.sort_values("S0201_308E")
display(Seattle)

# Draw a bar char with matplotlit
plt.figure(figsize=(12,6))
pop_groups = Seattle["Population group"].tolist()
y_pos = np.arange(len(pop_groups))
broadband_home =Seattle["S0201_308E"].tolist()
plt.bar(y_pos, broadband_home, align='center', alpha=0.6)
plt.xticks(y_pos, pop_groups)
plt.ylabel('% household with broadband subscription at home')
plt.title('Broadband home by population Groups in Seattle-Tacoma-Bellevue, WA Metro Area ')
plt.ylim(75,100)
plt.show()