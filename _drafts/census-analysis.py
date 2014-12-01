import pandas as pd
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import scipy as sp
import os
import numpy as np
import pydot 
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals.six import StringIO

###########################
#####      TO DO     #####
###########################

## Clean the code
## Check if the column are in correct order
## Have a look at empty value
## Use the tree on the test sample


data_directory = r'/Users/fred/Documents/Perso/Data Science Test/'

data_file = os.path.join(data_directory, 'census_income_learn.csv')

# Create a header containing column name and import the date from the csv file
census_header = ["age", "class of worker", "industry code", "occupation code", "education", "wage per hour", "enrolled in edu inst last wk", "marital status", "major industry code", "major occupation code", "race", "hispanic Origin", "sex", "member of a labor union", "reason for unemployment", "full or part time employment stat", "capital gains", "capital losses", "divdends from stocks", "tax filer status", "region of previous residence", "state of previous residence", "detailed household and family stat", "detailed household summary in household", "instance weight", "migration code-change in msa", "migration code-change in reg", "migration code-move within reg", "live in this house 1 year ago", "migration prev res in sunbelt", "num persons worked for employer", "family members under 18", "country of birth father", "country of birth mother", "country of birth self", "citizenship", "own business or self employed", "fill inc questionnaire for veteran's admin", "veterans benefits", "weeks worked in year", "year of census", "50K"]
census_data = pd.read_csv(data_file, names = census_header, header = None)
del census_data["instance weight"]
census_header.remove("instance weight")

# Change the type of the columns including categorical numeric values
continuous_col = ['industry code', 'occupation code', 'own business or self employed', 'veterans benefits', 'year of census']
for col in continuous_col:
	census_data[col] = census_data[col].astype(str)

# Create new DateFrames for the two classes
census_fifty_data = census_data[census_data['50K'] == " 50000+."]
census_not_fifty_data = census_data[census_data['50K'] == " - 50000."]


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

small_difference = []

numerical_columns = []
categorical_columns = []

for column in census_header[:-1]:
    if census_data[column].dtype == 'int64':
        numerical_columns.append(column)
    else:
        categorical_columns.append(column) 

# Iterate through column
for column in census_header[:-1]:
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

                # Create x, y and labels for the bars
                x1 = sp.arange(len(counts_fifty))
                x2 = sp.arange(len(counts_not_fifty))
                x3 = sp.arange(len(counts_all))
                y1 = autoformat(counts_fifty.values)
                y2 = autoformat(counts_not_fifty.values)
                y3 = autoformat(counts_all.values)
               
                labels = counts_all.keys()

                for element in range(len(y1)):
                    if abs(y1[element] - y2[element]) < 3:
                        small_difference.append(column + "=" + labels[element])                  

##                # Create the plots
##                fig, ax = plt.subplots()
##                width = 0.35
##                width2 = 0.05
##                bar1 = ppl.bar(ax, x1, y1, width, color = ppl.colors.set2[0])
##                bar2 = ppl.bar(ax, x2 + width, y2, width, color = ppl.colors.set2[2])
##                bar3 = ppl.bar(ax, x3 + width - width2/2, y3, width2, color = ppl.colors.set2[1])
##
##                # Set plots parameters
##                ax.set_xticks(x3 + width)
##                ax.set_xticklabels(counts_all.keys())
##                ax.set_xlim([-width,max(x3)+1])
##                ax.set_yticks(range(0, 110, 10))
##                ax.set_ylim([0,100])
##                ax.legend((bar1[0], bar2[0], bar3[0]), ('50000+', '- 50000', 'all') )
##                autolabel(bar1)
##                autolabel(bar2)
##                autolabel(bar3)
####                ax.text(0.5, 1, census_all.describe(), ha='center', va='center', bbox={'facecolor':'white'})
##                ax.annotate(census_all.describe(), xy=(0.5, 0.9), xycoords='axes fraction', ha = 'center', va = 'top', bbox={'facecolor':'white'})
##                plt.title(column)
##                if len(x3) > 7:
##                        plt.xticks(rotation = 'vertical')
##                fig.tight_layout()
##                # Display the figure
##                plt.show()
##                
##        else:
##                fig, ax = plt.subplots(3, sharex=True)
##                ax[0].annotate(census_all.describe(), xy=(0.5, 0.9), xycoords='axes fraction', ha = 'center', va = 'top', bbox={'facecolor':'white'})
##                ax[0].axis('off')
##                ax[1].hist(census_all, color = ppl.colors.set2[0], bins = 100, normed = True, edgecolor = "white", label = 'all')
##                ax[1].legend()
##                ax[2].hist((census_fifty, census_not_fifty), color = ppl.colors.set2[1:3], normed = True, edgecolor = "white", label = ['50000+', '- 50000'])
##                ax[2].legend()
##                plt.show()                
                





X=census_data.ix[:, categorical_columns]
X = X.T.to_dict().values()
vectorizer = DictVectorizer( sparse = False )
X = vectorizer.fit_transform(X)
X_names = vectorizer.get_feature_names()


##small_difference = ['race= Asian or Pacific Islander', 'race= Other', 'race= Amer Indian Aleut or Eskimo']

to_del = []

for index, element in enumerate(X_names):
    if X_names[index] in small_difference:
        to_del.append(index)

X = np.delete(X, to_del, axis=1)

for offset, index in enumerate(to_del):
    index -= offset
    del X_names[index]

num_X = census_data.ix[:, numerical_columns]

X = np.hstack((X, num_X))



X_names.extend(numerical_columns)


Y = census_data['50K']


clf = tree.DecisionTreeClassifier(min_samples_leaf=1000)

clf = clf.fit(X, Y)


dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data, feature_names = X_names) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("50K-tree.pdf")
