import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,12))
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    res = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    import numpy as np
    x=np.arange(df['Year'].min(),2051)
    plt.plot(x,res.intercept + res.slope*x, 'r', label='All data')

    # Create second line of best fit
    res2 = linregress(x=df.loc[df['Year']>=2000,'Year'],y=df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level'])
    x2=np.arange(2000,2051)
    plt.plot(x2,res2.intercept + res2.slope*x2, 'g', label='Data from 2000')

    # Add labels and title
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()