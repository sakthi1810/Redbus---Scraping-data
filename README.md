# Redbus---Scraping-data
# Introduction:
The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

# Domain:
TRANSPORTATION

# SKILL-TAKEAWAY:
Python,Selenium,Data Collection,Data Scraping,Data Management using SQL,Streamlit
# TECHNOLOGY USED:
Python 3.13
Selenium
DB Browser (SQLCipher)
Streamlit


# FEATURES OF APPLICATION:
# Retrive the Bus Information:

Selenium is a powerful tool for automating web browsers, which is especially useful for web scraping. If we want to retrieve bus details from RedBus, 
 we can use Selenium to automate the process of searching for buses and extracting the relevant information. This involves interacting with web elements 
 like input fields and buttons, waiting for the page to load, and extracting the desired details from the search results.
 
# Store data in database:
The collected bus details data was transformed into pandas dataframes. Before that, a new database and tables were created using the MySQL connector. With the help of MySQL, the data was inserted into the respective tables. The database accessed and managed in the MySQL.

# Web Page - streamlit:
With the help of Streamlit, we can create an interactive application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices

# PACKAGES AND LIBRARIES
pandas as pd
mysql.connector
import time
import pymysql
import warnings
streamlit as slt
from selenium import webdriver
