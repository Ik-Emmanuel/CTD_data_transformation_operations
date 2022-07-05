# Data Manipulation and Analysis With Python 
----
This code repository involves analysis of data of CTD measurements from The Western Channel Observatory (WCO)  marine biodiversity reference site.


## Overview
- Extract the data for operational use which might include detailed analysis and  querying and filtering use cases
- The goal is to build data systems to allow data subsets and further analysis:  
    - `An Ipython notebook` is used along with python's data manipulation library `PANDAS` to achieve data exploration and manipulation.
    -  Also build a system to allow for data querying: A `Python Flask Restful API` is built to achieve this.

## Key Dependencies 
- Python 
- Pandas
- Matplotlib
- Flask 

## Process and Methods

- A data experiment notebook `analysis.ipynb` is set up for data analysis using the given data which allows for data transformation, slicing and analysis
- A `Python Flask Restful` API is set up to allow for data query and filtering from external systems such as web applications for easy consumption. 


----
# About the API  
```
- The data is extracted and loaded into a database for storage and ease of manipulation from external systems
- The Flask API is designed with documentation and swaggerUI to run tests for querying data.  
```
  
## Running the API
- create a virtual enviroment 
- install all dependencies in  `requirements.txt`
- run main file `app.py`
- wait until the data is processed and loaded into sqlite database. look out for   `"✅✅ Data load complete ✅✅"` in terminal
- open running application at `localhost:5000` to test with inbuilt swagger UI or test with other API testing tools


# Example Queries

```
- GET  http://localhost:5000/ctd_data?page=1 

-  POST 
    {
         "from_date": "2021-05-05T20:19:09.730Z",
        "to_date": "2021-07-05T20:19:09.730Z"
    }


```

# Endpoints 

| METHOD | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- | 
| *GET* | ```/ctd_data?page=1 ``` | __Returns paginated data results to user__ |
| *POST* | ```/ctd_data ``` | __Queries data for a specific period and retuns results to user__ |
