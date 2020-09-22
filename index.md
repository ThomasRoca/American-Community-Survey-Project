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
An endpoint is simply the url of the API. It contains the necessary information for the database to respond with the exact data points user want.

Let's take an example: 
[https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_308E&for=state:*](https://api.census.gov/data/2018/acs/acs1/spp?get=NAME,S0201_308E&for=state:*)

The API will respond this (we truncated the response to save space here): 

  <code>[["NAME","S0201_308E","state"],</code><br>
  <code>["Minnesota","86.8","27"],</code><br>
  ["Mississippi","76.3","28"],
  ["Missouri","82.9","29"],
  ["Montana","83.6","30"],
  ["Nebraska","85.7","31"],
  ["Nevada","85.9","32"],
  ["New Hampshire","89.1","33"],
  ...
  ["Kentucky","81.7","21"],
  ["Louisiana","78.1","22"],
  ["Michigan","84.1","26"]]``

- Here is the API endpoint: ``https://api.census.gov/``  - NB. it has no parameter.
- In this example we request the 2018 ACS survey: ``data/2018/acs/acs1/``
And now we can define our parameters: 
  - indicator NAME - i.e. code : ``S0201_308E`` (which correspond to *COMPUTERS AND INTERNET USE!!Total households!!With a broadband Internet subscription*)
  - geography all states: ``state:*``
  - Note that between each parameter the ``&`` parameter is added. We can also use ``,`` to add several of the same entity for e.g.: ``S0201_307E,S0201_308E,S0201_246E``


## 2. Example of query using Python

### i. Data-visualization with Matplotlib

### ii. Data visualization using Microsoft PowerBI

## 3. Example of query using JavaScript

### i. Simple visualization with d3.js

### ii. Your first application using Highcharts

<iframe width="100%" height="575px" src="https://jsfiddle.net/ThomasRoca/xfhsgc5w/embedded/result,js,html/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>
<br>

