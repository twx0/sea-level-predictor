import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = list(range(1880, 2051))
    y = [slope*i + intercept for i in x]
    plt.plot(x, y, 'r')

# Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    x2 = list(range(2000, 2051))
    y2 = [slope2*i + intercept2 for i in x2]
    plt.plot(x2, y2, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()