# README

Credit to the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) for this template. 

## Project Intro/Objective
The purpose of this project is to implement a simple data engineering pipeline where we read in data and transform it for analysis. This project is meant to mimick a real life scenario where we would need to implement Object Oriented programming in order to handle data. This project can show the basics of the data engineering process and be used to build a more profound pipeline.

### Methods Used
* Object Oriented Programming
* Statistics
* etc.

### Technologies 
* Python
* Pandas, jupyter
* etc. 

## Project Description
The project begins with the StockData.py file which is used to create a StockData object that will be used to load in data from a file. We then implement the StockMetrics class in the StockMetrics.py file which is used to solve three problems relating to our data. The first problem we solve is finding the average value of each row, followed by our second problem of finding the median value of our rows and lastly the standard deviation of our rows. The implementation for each of these problems begins by reading in our data and then changing/cleaning the data types of our data in order to perform calculations. We end by finding the respective metric in each problem and returning our values. 