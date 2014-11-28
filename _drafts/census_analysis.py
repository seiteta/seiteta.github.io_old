import pandas as pd
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import scipy as sp
import os

data_directory = r'/Users/fred/Documents/Perso/Data Science Test/'

data_file = os.path.join(data_directory, 'census_income_learn.csv')

# Create a header containing column name and import the date from the csv file
census_header = ("AAGE", "ACLSWKR", "ADTIND", "ADTOCC", "AHGA", "AHRSPAY", "AHSCOL", "AMARITL", "AMJIND", "AMJOCC", "ARACE", "AREORGN", "ASEX", "AUNMEM", "AUNTYPE", "AWKSTAT", "CAPGAIN", "CAPLOSS", "DIVVAL", "FILESTAT", "GRINREG", "GRINST", "HHDFMX", "HHDREL", "MARSUPWT", "MIGMTR1", "MIGMTR3", "MIGMTR4", "MIGSAME", "MIGSUN", "NOEMP", "PARENT", "PEFNTVTY", "PEMNTVTY", "PENATVTY", "PRCITSHP", "SEOTR", "VETQVA", "VETYN", "WKSWORK", "YOC", "FFTYK")
census_data = pd.read_csv(data_file, names = census_header, header = None)

# Change the type of the columns including categorical numeric values
continuous_col = ['ADTIND', 'ADTOCC', 'SEOTR', 'VETYN', 'YOC']
for col in continuous_col:
	census_data[col] = census_data[col].astype(str)

# Create new DateFrames for the two classes
census_fifty_data = census_data[census_data['FFTYK'] == " 50000+."]
census_not_fifty_data = census_data[census_data['FFTYK'] == " - 50000."]


# The next two functions are used later, inside the for loop

# Transform values into percentage 
def autoformat(lst):
    lst = [float(element) for element in lst]
    lst = [element * 100 / sum(lst) for element in lst]
    return lst

# Put bar plot labels at the right place
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height, '%.0f%%'%float(height), ha = 'center', va = 'bottom')

def niu_remove(dict):
        if " Not in universe" in dict:
                del dict[" Not in universe"]
        return dict

# Iterate through column
for column in census_header:
        # Create new arrays containing only one column
        census_fifty = census_fifty_data[column]
        census_not_fifty = census_not_fifty_data[column]
        census_all = census_data[column]
     
        # Plot a bar or a histogram, depending on the column type
        if census_fifty.dtype != 'int64':
                
                # Count unique values
                counts_fifty=census_fifty.value_counts()
                counts_not_fifty=census_not_fifty.value_counts()
                counts_all=census_all.value_counts()

                counts_fifty=niu_remove(counts_fifty)
                counts_not_fifty=niu_remove(counts_not_fifty)
                counts_all=niu_remove(counts_all)              

                # Create x, y and labels for the bars
                x1 = sp.arange(len(counts_fifty))
                x2 = sp.arange(len(counts_not_fifty))
                x3 = sp.arange(len(counts_all))
                y1 = autoformat(counts_fifty.values)
                y2 = autoformat(counts_not_fifty.values)
                y3 = autoformat(counts_all.values)              
                labels = counts_all.keys()

                # Create the plots
                fig, ax = plt.subplots()
                width = 0.35
                width2 = 0.05
                bar1 = ppl.bar(ax, x1, y1, width, color = ppl.colors.set2[0])
                bar2 = ppl.bar(ax, x2 + width, y2, width, color = ppl.colors.set2[2])
                bar3 = ppl.bar(ax, x3 + width - width2/2, y3, width2, color = ppl.colors.set2[1])

                # Set plots parameters
                ax.set_xticks(x3 + width)
                ax.set_xticklabels(counts_all.keys())
                ax.set_xlim([-width,max(x3)+1])
                ax.set_yticks(range(0, 110, 10))
                ax.set_ylim([0,100])
                ax.legend((bar1[0], bar2[0], bar3[0]), ('50000+', '- 50000', 'all') )
                autolabel(bar1)
                autolabel(bar2)
                autolabel(bar3)
                plt.title(column)
                if len(x3) > 7:
                        plt.xticks(rotation = 'vertical')
                fig.tight_layout()
                # Display the figure
                plt.show()


# Add describe(), a pandas function that generates various summary statistics
# Have a look at empty values
