![](https://3ct13547mfyd2vpy663a50bz-wpengine.netdna-ssl.com/wp-content/uploads/2018/10/blue-wave-header.jpg)
<small><i>Image author: **Ted Eytan**, Creative Common Licence</i> [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)</small>

## About this tutorial
[Open data](https://theodi.org/article/what-is-open-data-and-why-should-we-care/) is about transparency, accountability and empowerment. By making accessible the data they collect - those data points that can be shared without harming data subjects - organizations provide information to the public but also opportunities to build systems and applications that consume data, transform it, re-purpose it and eventually make it even more useful for society. Read more about Microsoft's contribution and our [Open Data Campaign](https://blogs.microsoft.com/on-the-issues/2020/04/21/open-data-campaign-divide/).

**Why using an API?** APIs allow to programmatically access remote data sources. When plugging a table, a chart or a web page to remote data sources, your data points are always up-to-date. APIs are often associated with databases too large to easily navigate them via a spreadsheet. If you don't want to download the entire database to access just a few data points, what you need is a query. You can then adapt to users' data needs by customizing your query and have this information rendered the most efficient and compelling way possible.

In this tutorial, I'm going to present one of the most insightful sources of data to understand racial inequality in the United States. I'll provide tips to leverage its [API](https://en.wikipedia.org/wiki/API) - i.e. way to programmatically query the database. I will also provide examples of data visualizations and simple applications we can build on the top of the database. I will provide snippets of [**Python**](https://www.python.org/) code and [**JavaScript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript). I will use [**Microsoft PowerBI**](https://powerbi.microsoft.com/), [**Highcharts**](https://www.highcharts.com/) and [**d3.js**](https://d3js.org/) to visualize this information and reveal some of the insights hidden in this very rich dataset.

To easily share JavaScript code, I'll use [JSfiddle](https://jsfiddle.net/). 

## About U.S. Census Bureau's [American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs/about.html)
As put by the U.S. Census Bureau, "the American Community Survey (ACS) is an ongoing survey that provides vital information on a yearly basis about our nation and its people. Information from the survey generates data that help determine how more than $675 billion in federal and state funds are distributed each year. Through the ACS, we know more about jobs and occupations, educational attainment, veterans, whether people own or rent their homes, and other topics. Public officials, planners, and entrepreneurs use this information to assess the past and plan the future"
[Read more about it on ACS web page.](https://www.census.gov/programs-surveys/acs/about.html)

## Resources
- Web page of the [American Community Survey](https://www.census.gov/programs-surveys/acs)
- [ACS API Handbook]( https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_api_handbook_2020.pdf), 2020, U.S. Census Bureau
- [Using the Census API with the American Community Survey](https://www.census.gov/data/academy/webinars/2019/api-acs.html)
- [Developper section of the American Community Survey web page](https://www.census.gov/data/developers.html)
- [Census Bureau API key registration page](https://api.census.gov/data/key_signup.html)
- [The Open Data Institute](https://theodi.org/)
- [Microsoft Open Data Initiative](https://www.microsoft.com/en-us/open-data-initiative)


## 1. American Community Survey API endpoint
An endpoint is simply the base url of an API. It contains the necessary information for the database to respond with the exact data points user want.

Let's start with a **data request example**:<br>
<a href="https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_308E&for=state:*">"https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_308E&for=state:*"</a>

The API will respond an array of arrays like this - nb. we truncated the response to save space: 

  <code>[["NAME","S0201_308E","state"],</code><br>
  <code>["Minnesota","86.8","27"],</code><br>
  <code>["Mississippi","76.3","28"],</code><br>
  <code>["Missouri","82.9","29"],</code><br>
  <code>["Montana","83.6","30"],</code><br>
  <code>["Nebraska","85.7","31"],</code><br>
  <code>["Nevada","85.9","32"],</code><br>
  <code>["New Hampshire","89.1","33"],</code><br>
  <code>...</code><br>
  <code>["Kentucky","81.7","21"],</code><br>
  <code>["Louisiana","78.1","22"],</code><br>
  <code>["Michigan","84.1","26"]]</code><br>
  

The first element of one of the nested arrays is the geography NAME (here the names of the States), the second is the value of the requested indicator (here S0201_308E which is the code for *Household with a broadband internet subscription*), finally the last element is the *State code* used by the census bureau. 

Let's look at **url parameters in details**:

- Here is the API endpoint: ``https://api.census.gov/``  - NB. API url with no parameter.
- In this example we request the 2018 ACS survey: ``data/2018/acs/acs1/``<br>

And now we can define our parameters (using ``spp?get=`` as a prefix): 
  - ``NAME`` will allow us to have the actual **name of the geography** displayed on the top of the geography code.
  - **indicator code** : ``S0201_308E`` (which correspond to "*COMPUTERS AND INTERNET USE!!Total households!!With a broadband Internet subscription*")
  - **geography**: all states ``state:*`` (Note that ``:*`` stands for "all" in "all states" )
  - Note that between each parameter the ``&`` operator is added. We can also use ``,`` to add several of the same entity for e.g.: ``S0201_307E,S0201_308E,S0201_246E``

In this tutorial we want to take advantage of the detailed data for population group ("Black and African American, White, Hispanic or Latino", etc.). 
The parameter ``POPGROUP`` allow querying by population groups. Here are some examples of population group codes:
- "001": "Total population"
- "002": "White alone"
- "400": "Hispanic or Latino (of any race) (200-299)"
- "004": "Black or African American alone"
- "012": "Asian alone (400-499)"<br>
- *More info about available population groups ("Race/Ethnic Group"): [here](https://api.census.gov/data/2019/acs/acs1/spp/variables/POPGROUP.json)*

Many indicators are available in the survey, here is a list for the 2019 ACS: [https://api.census.gov/data/2019/acs/acs1/spp/variables.html](https://api.census.gov/data/2019/acs/acs1/spp/variables.html).

Results are available for several geography levels (States, congressional district, county, metropolitan areas, etc.). Here is the list of [available geography level for the 2019 ACS](https://api.census.gov/data/2019/acs/acs1/spp/examples.html).To make it easier, you will find the [metropolitan areas available with their codes here](https://raw.githubusercontent.com/ThomasRoca/American-Community-Survey-Project/master/Metropolitan_area_code.json).

As an example, here is how to get the **total population for Alameda County (code 001) in the state of California (state code 06)** for the ACS 2019:
[https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=county:001&in=state:06](https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=county:001&in=state:06)


More information about codes for states, county, population groups etc. are available on the ACS web page, we encourage you to search for them.

Finally, if you want to make many requests to the API (More than 500 queries per IP address per day), you will need to get an [API key](https://api.census.gov/data/key_signup.html) - it's free. 
To use your API key, just add the parameter ``&key=``  - followed by your api key -  at the end of your query.


## 2. Example of query using Python

You now have a better understanding of the way the *American Community Survey's* API works. Let's put this into practice writting some code in Python.

In the following script I'll query the API, store the data into a [Pandas](https://pandas.pydata.org/) dataframe and finally present some findings in a bar chart using [Matplotlib](https://matplotlib.org/). The data point we will request is "Total households with a broadband subscription" (code ``S0201_308E``)

*NB. The code is commented so that non-coders can follow step by step.*

```python 
import pandas as pd
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
df.sort_values(["NAME"])
```
[https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_307E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&POPGROUP=*&key=](https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_307E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&POPGROUP=*&key=)

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>S0201_308E</th>
      <th>POPGROUP</th>
      <th>metropolitan statistical area/micropolitan statistical area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Akron, OH Metro Area</td>
      <td>86.0</td>
      <td>001</td>
      <td>10420</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Akron, OH Metro Area</td>
      <td>80.7</td>
      <td>004</td>
      <td>10420</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Akron, OH Metro Area</td>
      <td>86.9</td>
      <td>002</td>
      <td>10420</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albany-Schenectady-Troy, NY Metro Area</td>
      <td>86.9</td>
      <td>001</td>
      <td>10580</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Albany-Schenectady-Troy, NY Metro Area</td>
      <td>87.7</td>
      <td>002</td>
      <td>10580</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>212</th>
      <td>Worcester, MA-CT Metro Area</td>
      <td>87.6</td>
      <td>002</td>
      <td>49340</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Worcester, MA-CT Metro Area</td>
      <td>87.9</td>
      <td>001</td>
      <td>49340</td>
    </tr>
    <tr>
      <th>365</th>
      <td>Worcester, MA-CT Metro Area</td>
      <td>83.8</td>
      <td>400</td>
      <td>49340</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Youngstown-Warren-Boardman, OH-PA Metro Area</td>
      <td>81.8</td>
      <td>001</td>
      <td>49660</td>
    </tr>
    <tr>
      <th>213</th>
      <td>Youngstown-Warren-Boardman, OH-PA Metro Area</td>
      <td>82.1</td>
      <td>002</td>
      <td>49660</td>
    </tr>
  </tbody>
</table>
<br>

### i. Data-visualization with Matplotlib
We can now display the data in a bar chart with Matplotlib.

**Let's dig into Seattle-Tacoma-Bellevue metro area**
```python
# let's get data for Seattle-Tacoma-Bellevue metro area
Seattle=df.loc[df["NAME"]=="Seattle-Tacoma-Bellevue, WA Metro Area"].copy()

# code and label for population group 
pop_group_dict= {"001":"Total population", 
                 "002": "White alone", 
                 "400": "Hispanic or Latino",
                 "004": "Black or African American"}

Seattle["Population group"]=Seattle["POPGROUP"].map(pop_group_dict)
Seattle=Seattle.sort_values("S0201_308E")
Seattle
```

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>S0201_308E</th>
      <th>POPGROUP</th>
      <th>metropolitan statistical area/micropolitan statistical area</th>
      <th>Population group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>280</th>
      <td>Seattle-Tacoma-Bellevue, WA Metro Area</td>
      <td>85.4</td>
      <td>004</td>
      <td>42660</td>
      <td>Black or African American</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Seattle-Tacoma-Bellevue, WA Metro Area</td>
      <td>90.4</td>
      <td>400</td>
      <td>42660</td>
      <td>Hispanic or Latino</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Seattle-Tacoma-Bellevue, WA Metro Area</td>
      <td>91.7</td>
      <td>001</td>
      <td>42660</td>
      <td>Total population</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Seattle-Tacoma-Bellevue, WA Metro Area</td>
      <td>92.1</td>
      <td>002</td>
      <td>42660</td>
      <td>White alone</td>
    </tr>
  </tbody>
</table>

**Now we have the subset for Seattle-Tacoma-Bellevue metro area, we can draw a bar chart with matplotlib**

```python
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

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
```
<img src="https://raw.githubusercontent.com/ThomasRoca/American-Community-Survey-Project/gh-pages/assets/img/broadband_subscription_plot.png" width="80%">


### ii. Data visualization using Microsoft PowerBI

As another example of visualization, we showcase below what can be easily achieved by less advanced coders using [Microsoft PowerBI](https://powerbi.microsoft.com/). PowerBI allows to build dahsboards in minutes when you would need hours or days to code it from scratch. We used the same indicator as the python query example. The CSV file is stored in this GitHub repo and accessible [here](https://github.com/ThomasRoca/American-Community-Survey-Project/blob/master/ACS_broadband.csv). NB. The data source for this PowerBi visualization is the one hosted in this repo as PowerBI can easly connect to remote data sources.

<iframe width="100%" height="550" src="https://msit.powerbi.com/view?r=eyJrIjoiOTRkNzc2OGQtN2ExYi00NDgyLTk1ZTQtYTY3YTNmNTMyYThlIiwidCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0NyIsImMiOjV9" frameborder="0" allowFullScreen="true"></iframe>

<br>

## 3. Example of query using JavaScript
Let's continue our journey with JavaScript. If you want to build a web application the standard way is to use JavaScript and HTML/CSS. I will start with a simple query
asking the API for poverty rate (code: ``S0201_255E``) for "New York-Newark-Jersey City, NY-NJ-PA Metro Area" which code is ``35620`` (see [full list](https://github.com/ThomasRoca/American-Community-Survey-Project/blob/master/Metropolitan_area_code.json)) for ``Total population`` (code ``001``) AND for ``Black or African American`` (code ``004``) : 

Here is our new query: [https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_246E&POPGROUP=001&POPGROUP=004&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:35620](https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_246E&POPGROUP=001&POPGROUP=004&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:35620)

The API response is now: <br>
<code>[["NAME","S0201_246E","POPGROUP","metropolitan statistical area/micropolitan statistical area"],</code><br>
<code>["New York-Newark-Jersey City, NY-NJ-PA Metro Area","9.4","001","35620"],</code><br>
<code>["New York-Newark-Jersey City, NY-NJ-PA Metro Area","15.1","004","35620"]]</code><br>

We end up with an array of 3 arrays. The first one provides the meta data, the second one gives poverty rate for total population (i.e. 9.4%) and the third one for Black or African American (15,1%).

To retrieve and store this information in variables, we can use those elements' index - NB. index starts with 0 not 1. Array[0] will be the 1st array containing the meta data ``["NAME","S0201_246E","POPGROUP","metropolitan statistical area/micropolitan statistical area"]`` and array[0][0] will be its 1st element if this first array,  i.e. ``NAME``.

To find the value of the poverty rate for total population (nb. population code "001") you must dig into the 2nd array (i.e.[1]) and get its 2nd item ([1]): array[1][1] is the spot where poverty rate for total population is stored. 

Let's put that into practice and display this information on a web page:

``` Javascript
$(function() {
  // query the API
  $.ajax({
    url: "https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_246E&POPGROUP=001&POPGROUP=004&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:35620",
    complete: function(json) {
      
      // get the API response
      data = JSON.parse(json.responseText);
      
      // set some variable to host data:
      value_total = data[1][1]; // Poverty rate for total population
      value_b = data[2][1]; // Poverty rate for Black and African American
      metro = data[1][0]; // name of the metropolitan area
      
      // let's add some text to be displayed on the web page
      metro_text = "<b>Poverty rate in </b>" + metro
      total_text = "<b>Total population: </b>" + value_total
      black_african_american_text = "<b>Black or African American: </b>" + value_b
      
      // let's send this text to the actual web page
      document.getElementById("metropolitan").innerHTML = metro_text;
      document.getElementById("total_population").innerHTML = total_text;
      document.getElementById("black_african_american").innerHTML = black_african_american_text;
    }
  })
})
```
Complete code and results on JSfiddle: 
<iframe width="100%" height="450px" src="https://jsfiddle.net/ThomasRoca/jzq9f7uv/embedded/result,js,html/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

### i. Simple visualization with d3.js
d3 stands for Data-Driven Document, [d3.js](https://d3js.org/) is an open source data visualization library. It is not the easiest to implement but it provides full flexibility. Here is an example of a simple bar chart rendering the previous API query.

<iframe width="100%" height="450" src="https://jsfiddle.net/ThomasRoca/cmr4j1h7/embedded/result,js,html/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>



### ii. Your first application using Highcharts

When building a web application, what you try to achieve is to give users the freedom to choose what to display. Here, I will let the user select a metropolitan area and an indicator - NB. From a subset of those available in the survey. Those 2 parameters will be used to build the API query (i.e. the url). Finally, the job will consist in parsing the resulting data points and use them as input for the chart - here [Highchart](https://www.highcharts.com/)'s [Basic column chart](https://www.highcharts.com/demo/column-basic). 
In this example I use a dictionnary to store the values associated with their categories (i.e. population groups). I commented the code in the JavaScript tab of the JSfiddle below.

<iframe width="100%" height="575px" src="https://jsfiddle.net/ThomasRoca/t8d2v4p9/embedded/result,js,html/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>
<br>

