import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=[0], parse_dates=True)

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(df, color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['Years'] = [x.year for x in df_bar['date']]
    df_bar['Months'] = [x.strftime('%B') for x in df_bar['date']]
    group = df_bar.groupby(["Years", "Months"], sort=False)
    df_bar = pd.DataFrame(round(group["value"].mean()).astype(int))
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    df_bar = df_bar.reset_index()
    df_bar = pd.concat([pd.DataFrame({"Years": [2016, 2016, 2016, 2016],"Months": ['January', 'February', 'March', 'April'],"Average Page Views": [0, 0, 0, 0]}), df_bar])

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,12))
    sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10", legend=False, ax=ax)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    ax.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [x.year for x in df_box['date']]
    df_box['Month'] = [x.strftime('%b') for x in df_box['date']]
    df_box = df_box.rename(columns={"value": "Page Views"})

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(24, 12))

    # Yearly boxplot
    sns.boxplot(data=df_box, x="Year", y="Page Views", ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")

    # Monthly boxplot
    sns.boxplot(data=df_box, x="Month", y="Page Views", order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=ax[1])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
