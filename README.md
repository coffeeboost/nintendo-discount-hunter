# About
This project aims to track discounted games from nintendo's website

# Program flow
- Use BS4 and Selenium to load dynamic content and scrape data from nintendo's website
- data is cleaned in python and pandas
- discounts are calculated and outputted to a CSV sorted by largest discounts first
- add cron job on MacOS to repeat daily


`./run.sh` to run program.

The program will first run a selenium script that scrapes all information on nintendo, then a python script will parse through the html and produce a table with discount information in it. The table is saved as a csv in `./output` that can be watched for changes in the future.
