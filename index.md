![](https://3ct13547mfyd2vpy663a50bz-wpengine.netdna-ssl.com/wp-content/uploads/2018/10/blue-wave-header.jpg)
<small><i>Image author: **Ted Eytan**, Creative Common Licence</i> [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)</small>

## About this tutorial
[Open data](https://theodi.org/article/what-is-open-data-and-why-should-we-care/) is about transparency, accountability and empowerement. By making accessible the data they collect - those data points that can be shared without harming data subjects - organizations provide information to the public but also opportunities to build systems and applications that consume data, transform it, repurpose it and eventually make it even more useful for society. Read about Microsoft [Open data Initiative](https://www.microsoft.com/en-us/open-data-initiative)

In this tutorial, I'm going to present one of the most insightful sources of data to understand racial inequality in the United States. I'll provide tips to leverage its [API](https://en.wikipedia.org/wiki/API) - i.e. way to programmatically query the database. I will also provide examples of data visualizations and simple applications we can build on the top of the database. I will provide snipets of [**Python**](https://www.python.org/) code and [**JavaScript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript). I will use [**Microsoft PowerBI**](https://powerbi.microsoft.com/), [**Highcharts**](https://www.highcharts.com/) and [**d3.js**](https://d3js.org/) to visualize this information and reveal some of the insights hidden in this very rich dataset.

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
An endpoint is simply the base url of the API. It contains the necessary information for the database to respond with the exact data points user want.

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
  

The first element of one of the nested arrays is the geography NAME (here names of the States), the second is the value of the requested indicator (here S0201_308E which is the code for household with a broaband internet subscription), finaly the last element is the State code used by the census bureau. 

Let's look at **url parameters in details**:

- Here is the API endpoint: ``https://api.census.gov/``  - NB. API url with no parameter.
- In this example we request the 2018 ACS survey: ``data/2018/acs/acs1/``<br>

And now we can define our parameters (using ``spp?get=`` as a prefix): 
  - ``NAME`` will allow us to have the actual **name of the geography** displayed on the top of the geography code.
  - **indicator code** : ``S0201_308E`` (which correspond to *COMPUTERS AND INTERNET USE!!Total households!!With a broadband Internet subscription*)
  - **geography**: all states ``state:*`` (Note that ``:*`` stands for "all" in "all states" )
  - Note that between each parameter the ``&`` parameter is added. We can also use ``,`` to add several of the same entity for e.g.: ``S0201_307E,S0201_308E,S0201_246E``

In this tutorial we want to take advantage of the detailed data for population group ("Black and African American, White, Hispanic or Latino", etc.). 
The parameter ``POPGROUP`` allow querying by population groups. Here are som examples of code of population groups :
- "001": "Total population"
- "002": "White alone"
- "400": "Hispanic or Latino (of any race) (200-299)"
- "004": "Black or African American alone"
- "012": "Asian alone (400-499)"<br>
- *More info about available population groups ("Race/Ethnic Group"): [here](https://api.census.gov/data/2019/acs/acs1/spp/variables/POPGROUP.json)*

Many indicators are available in the survey, here is a list of the one you can find in the 2019 ACS: [https://api.census.gov/data/2019/acs/acs1/spp/variables.html](https://api.census.gov/data/2019/acs/acs1/spp/variables.html).
Results are available for several geography levels (States, congressional district, county, metropolitan areas, etc.). Here is the list of [available geography level for the 2019 ACS](https://api.census.gov/data/2019/acs/acs1/spp/examples.html).

As an example, here is how to get the **total population for Alameda County (code 001) in the state of California (state code 06)** for the ACS 2019:
["https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=county:001&in=state:06"]("https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=county:001&in=state:06")

More information about codes for states, county, population groups etc. are available on the survey web page, we encourage you to search for them.

Finally, if you want to make many requests to the API (More than 500 queries per IP address per day), you will need to get an [API key](https://api.census.gov/data/key_signup.html) - free. The use an API key, add the parameter ``&key=`` with your api key at the end of your query.

## 2. Example of query using Python

### i. Data-visualization with Matplotlib

### ii. Data visualization using Microsoft PowerBI

## 3. Example of query using JavaScript

### i. Simple visualization with d3.js

### ii. Your first application using Highcharts

<iframe width="100%" height="575px" src="https://jsfiddle.net/ThomasRoca/xfhsgc5w/embedded/result,js,html/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>
<br>

