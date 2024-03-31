import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label= "Scatter Plot", color = "blue")
    
    # # Create first line of best fit
    lr= linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), lr.slope * range(1880, 2051, 1) + lr.intercept)
    
    
    # Create second line of best fit
    lr_2000 = linregress(data.query('Year >= 2000')['Year'], 
                              data.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), lr_2000.slope * range(2000, 2051, 1) + lr_2000.intercept)
    
   
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sea_level_plot.png")  

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()

