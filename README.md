# Sprint 

## Update 8/21/2023 

- Re-created easy to read/follow Dashboards in Streamlit.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
## An Analysis on sprinting times in track and field

> The goal of this project is to to analyze how sprinting times have improved over the years using progression and regression analysis


## Project Description
This project aims to analyze the progression of sprinting times over the years. 

By extracting data from the World Atheltics website using BeautifulSoup, the project creates a dataframe to enable detailed analysis and visualization of the collected sprinting records.

## Features
- Web scraping: Utilizes the BeautifulSoup library to scrape data from a webpage containing sprinting records.
- Data extraction: Extracts relevant information such as rank, mark (time), wind, name, and the nationality of the sprinters.
- DataFrame creation: Organizes the extracted data into a structured dataframe for further analysis.

- Visualization: Provides data visualization capabilities to better understand the trends and patterns in sprinting performance.


## Future Enhancements
- Historical analysis: Extend the analysis to cover multiple years or historical data to observe long-term trends in sprinting times.
- Statistical analysis: Conduct statistical tests and calculations to identify significant improvements and assess the significance of various factors influencing sprinting performance.
- Comparative analysis: Compare the performance of different countries, athletes, or age groups to identify patterns and outliers.
- Interactive dashboard: Develop an interactive dashboard or web application to allow users to explore the data and visualize the progression of sprinting times.

## Technologies Used

- Python: Programming language used for data extraction, analysis, and visualization.
 - BeautifulSoup: Library for web scraping and HTML parsing.
 - Pandas: Library for data manipulation and analysis, including dataframe creation.
- Matplotlib / Plotly: Libraries for data visualization and creating meaningful plots and charts.
 - GitHub: Version control repository for collaborative development and project management.
 - Streamlit: To display dashboards and other data frames.

TODO: 
- Add  women's 100, 200, and 400M.
- Create Dashboards for all events
- Combine Dashboards into one .html file
- 


## 100 M Men's

To start the project, I gathered data from the World Athletics website for the men's 100 meter dash using BeautifulSoup and put them into a data frame.




This graph represents the times ran, ranging from 9.83 to 10.13.



![times](https://github.com/lyokoth/Performance-progression-in-track-and-field-/assets/97857899/bece1bd0-74ef-4c91-b25a-5766d8437bac)



The second graph shows that tailwinds have a positive effect on time ran.

![sprint vs mark](https://github.com/lyokoth/Performance-progression-in-track-and-field-/assets/97857899/af2482ac-d224-4753-90b4-5a8ecdfa8780)


I then created a Dashboard in plotly that shows the athlete's names, time ran, and wind. The two Y axis represent the time ran and the wind aid if there was any. 

![100m dash mens](https://github.com/lyokoth/sprint/blob/master/Images/100M%20dashboard%20stream.gif)
## 200 M Data

For the 200 meter men's, the fastest time recorded was 19.67 with + 0.3 wind aid. The slowest was 20.49 with +0.4 wind aid.

There were 36 competitors from the USA.

On the World Athletics website, the men are ranked based on their times, from ranks 1 - 90. 

![]



