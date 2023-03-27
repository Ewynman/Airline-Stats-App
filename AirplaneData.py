import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout


df = pd.read_csv('data.csv')

print("Missing values per column:\n", df.isnull().sum(), "\n")

original_rows = len(df)
df.dropna(inplace=True)
new_rows = len(df)
print(f"Dropped {original_rows - new_rows} rows with missing values. Remaining rows: {new_rows}.\n")

df['Landing Count'] = df['Landing Count'].astype('int')
df['Total Landed Weight'] = pd.to_numeric(df['Total Landed Weight'], errors='coerce')
print("Converted data types for 'Landing Count' and 'Total Landed Weight' columns.\n")

original_rows = len(df)
df.drop_duplicates(inplace=True)
new_rows = len(df)
print(f"Dropped {original_rows - new_rows} duplicate rows. Remaining rows: {new_rows}.\n")

df.rename(columns={'Operating Airline': 'Airline', 'Operating Airline IATA Code': 'Airline IATA Code'}, inplace=True)
print("Renamed columns 'Operating Airline' to 'Airline' and 'Operating Airline IATA Code' to 'Airline IATA Code'.\n")

print("Summary statistics for numeric columns:\n", df.describe(), "\n")

mean_landings = df['Landing Count'].mean()
print(f"Mean number of landings: {mean_landings:.2f}\n")

median_weight = df['Total Landed Weight'].median()
print(f"Median total landed weight: {median_weight:.2f}\n")

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Visualizations")
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.create_tabs()

    def create_tabs(self):
        # create three tabs for the three designs
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        # Design 1: Bar chart showing the total number of landings by airline
        plt.figure(figsize=(10, 5))
        ax = sns.barplot(data=df, x='Airline', y='Landing Count')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center')
        plt.title("Total Number of Landings by Airline")
        plt.xlabel("Airline")
        plt.ylabel("Number of Landings")
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(plt.gcf().canvas)
        plt.close()

        # Design 2: Pie chart showing the proportion of landings by aircraft body type
        plt.figure(figsize=(8, 8))
        df_pie = df.groupby(['Aircraft Body Type'])['Landing Count'].sum().reset_index()
        df_pie.sort_values('Landing Count', ascending=False, inplace=True)
        ax = plt.subplot(111, aspect='equal')
        ax.pie(df_pie['Landing Count'], labels=df_pie['Aircraft Body Type'], autopct='%1.1f%%', startangle=90)
        plt.title("Proportion of Landings by Aircraft Body Type")
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(plt.gcf().canvas)
        plt.close()

        # Design 3: Box plot showing the distribution of total landed weight by country
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=df, x='GEO Region', y='Total Landed Weight')
        ax = sns.stripplot(data=df, x='GEO Region', y='Total Landed Weight', color=".3", alpha=.5)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center')
        plt.title("Distribution of Total Landed Weight by Country")
        plt.xlabel("Country")
        plt.ylabel("Total Landed Weight")
        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(plt.gcf().canvas)
        plt.close()

        # add the tabs to the tab widget
        self.tab_widget.addTab(tab1, "Total Landings by Airline")
        self.tab_widget.addTab(tab2, "Proportion of Landings by Aircraft Body Type")
        self.tab_widget.addTab(tab3, "Distribution of Total Landed Weight by Country")

# create the GUI and show it
app = QApplication([])
main_window = MyMainWindow()
main_window.show()
app.exec_()