# Airline Landing Stats App

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This code imports the pandas and matplotlib libraries along with the seaborn and PyQt5.QtWidgets libraries for data analysis and visualization purposes. It then reads a CSV file named 'data.csv' and performs data cleaning operations such as dropping rows with missing values, dropping duplicate rows, and renaming columns. It also converts the data type of some columns and calculates some summary statistics.

The code then defines a GUI using the PyQt5 library and creates three tabs, each containing a different type of data visualization based on the cleaned and processed data from the CSV file. The first tab shows a bar chart of the total number of landings by airline, the second tab displays a pie chart of the proportion of landings by aircraft body type, and the third tab shows a box plot of the distribution of total landed weight by country. Finally, the GUI is displayed and runs until the user closes it.

## Getting Started <a name = "getting_started"></a>

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
git clone https://github.com/Ewynman/Airline-Stats-App.git
```

And install the needed libraries
Matpltlib:

```
pip install matpltlib
```
Seaborn
```
pip install seaborn
```
PyQt5
```
pip install PyQt5
```
Pandas
```
pip install pandas
```
End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

In the command promopt of the working directory run
```
AirplaneData.py
```
