# PhonePe-pulse-visualization

## Table of Contents:
1. About The Project
2. Getting Started
   - Prerequisites
   - Installation
3. Usage
4. Steps
5. Run
6. Skills Covered
------------------

## 1. About The Project :

   This project is focused on cloning a github repository [Phone-pe-pulse](https://github.com/PhonePe/pulse) which contains a large amount of data related to
various metrics and statistics.We will be transforming the data in an useful manner and create a streamit dashboard to visualize the data.Creating a live geo map
## 2. Getting Started :

> Before starting we need to install certain **python** libraries.
-  ### PREREQUISITES :
   + json
   + pymysql
   + os
   + streamlit
   + plotly.express
   + warnings
   + streamlit_option_menu
   + pandas - are the Python libraries used in this project

- ### INSTALLATION :
  Run these command separately on your python environment to install.
  
        pip install json
        pip install os
        pip install plotly
        pip install streamlit
        pip install pandas
        pip install pymysql
        pip insatall streamlit_option_menu
   
## 3. USAGE :
   - In this Project, Wrote a python program to clone a git hub repository
   - Fetched required data using os library and preprocessed stored it into MySql Database using PyMySql 
   - Created different options that user can select and get insights from it
   - created Live geo Map, Analysing the data and visualizing it in 5 different charts based on the option which user selects 

## 4. STEPS :
   1. Import all the libraries that are used in this project.
   2. Created 6 functions which returns aggregated,map and top data for all states on year wise upto 2023 Quarter 4.
   3. Cretaed a function to link mysql and migrate data into SQL Database
   4. Created Dashboard on Streamlit and gave optionmenu to navigate through map, analysis, visualize
   5. created different selectbox and buttons to make our project work alongside what the user opts

   > - Used pd.read_sql_query() to get tables from mysql and it turns the table into dataframe so we can easily visualize

## 5. RUN :
   > - To Run this project we need to go to terminal and change its path to file_loacted_directory
   > - Then run streamlit code to execute,

           streamlit run file_name.py
   - replace file_name with created python file name
   - To run this project use,

           streamlit run phonepe.py 
# 6. Skills Covered ✅ ⬇️

    Python (Scripting)
    Data Collection
    MySQL
    Plotly
    Pandas Dataframe
    Github cloning
    streamlit
    IDE:  Jupyter, PyCharm Community Version, VS Code

