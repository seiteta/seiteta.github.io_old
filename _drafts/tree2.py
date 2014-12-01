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

data_directory = r'C:\Users\Fred\Desktop\us_census_full'
train_data_file = os.path.join(data_directory, 'census_income_learn.csv')

# Create a header containing column name, import data from the csv files, remove weight column
census_header = ["age", "class of worker", "industry code", "occupation code", "education", "wage per hour", "enrolled in edu inst last wk", "marital status", "major industry code", "major occupation code", "race", "hispanic Origin", "sex", "member of a labor union", "reason for unemployment", "full or part time employment stat", "capital gains", "capital losses", "divdends from stocks", "tax filer status", "region of previous residence", "state of previous residence", "detailed household and family stat", "detailed household summary in household", "instance weight", "migration code-change in msa", "migration code-change in reg", "migration code-move within reg", "live in this house 1 year ago", "migration prev res in sunbelt", "num persons worked for employer", "family members under 18", "country of birth father", "country of birth mother", "country of birth self", "citizenship", "own business or self employed", "fill inc questionnaire for veteran's admin", "veterans benefits", "weeks worked in year", "year of census", "50K"]
train_census_data = pd.read_csv(train_data_file, names = census_header, header = None)
del train_census_data["instance weight"]
census_header.remove("instance weight")

# Change the type of the columns including categorical numeric values
continuous_col = ['industry code', 'occupation code', 'own business or self employed', 'veterans benefits', 'year of census']
for col in continuous_col:
    train_census_data[col] = train_census_data[col].astype(str)



# Create new DateFrames for the two classes
census_fifty_data = train_census_data[train_census_data['50K'] == " 50000+."]
census_not_fifty_data = train_census_data[train_census_data['50K'] == " - 50000."]


# The next two functions are used later, inside the for loop:

## Transform values into percentage 
def autoformat(lst):
    lst = [float(element) for element in lst]
    lst = [element * 100 / sum(lst) for element in lst]
    return lst

## Put bar plot labels at the right place
def autolabel(bars, bar_id, num_element):
    gap = 0
    if num_element > 8 and bar_id == 3:
        gap = 5
    elif num_element > 10:
        if bar_id == 3:
            gap = 5
        elif bar_id == 2:
            gap = 10
    else:
        gap = 0
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height + gap, '%.0f%%'%float(height), ha = 'center', va = 'bottom')


#### TO BE COMMENTED
small_difference = []
numerical_columns = []
categorical_columns = []
for column in census_header[:-1]:
    if train_census_data[column].dtype == 'int64':
        numerical_columns.append(column)
    else:
        categorical_columns.append(column) 

# Iterate through column
for column in census_header[:-1]:
        # Create new arrays containing only one column
        census_fifty = census_fifty_data[column]
        census_not_fifty = census_not_fifty_data[column]
        census_all = train_census_data[column]
     
        # Plot a bar or a histogram, depending on the column type
        if census_fifty.dtype != 'int64':
                
                # Count unique values
                counts_fifty = census_fifty.value_counts()
                counts_not_fifty = census_not_fifty.value_counts()
                counts_all = census_all.value_counts()
                
                # Make sure all the keys are in the same order
#                counts = pd.concat([counts_fifty, counts_not_fifty, counts_all],axis=1)
#                counts = counts.sort(2, ascending = False)
#                counts.fillna(0, inplace=True)
#                counts_fifty = counts[0]
#                counts_not_fifty = counts[1]
#                counts_all = counts[2]
#
                # Create x, y and labels for the bars
                x1 = sp.arange(len(counts_fifty))/3.
                x2 = sp.arange(len(counts_not_fifty))/3.
                x3 = sp.arange(len(counts_all))/3.
                y1 = autoformat(counts_fifty.values)
                y2 = autoformat(counts_not_fifty.values)
                y3 = autoformat(counts_all.values)              
                labels = counts_all.keys()
                
                #### TO BE COMMENTED
                for element in range(len(y1)):
                    if abs(y1[element] - y2[element]) < 3:
                        small_difference.append(column + "=" + labels[element]) 

#                # Create the plots
#                fig, ax = plt.subplots()
#                width = 0.1
#                width2 = 0.02
#                num_element = len(x3)
#                if num_element > 10:
#                    linewidth = 0.5
#                    width2 = 0.05
#                else:
#                    linewidth = 1
#                    width2 = 0.02
#                bar1 = ppl.bar(ax, x1, y1, width, color = ppl.colors.set2[0], linewidth = linewidth)
#                bar2 = ppl.bar(ax, x2 + width, y2, width, color = ppl.colors.set2[2], linewidth = linewidth)
#                bar3 = ppl.bar(ax, x3 + width - width2/2, y3, width2, color = ppl.colors.set2[1], linewidth = linewidth)
#
#                # Set plots parameters
#                ax.set_xticks(x3 + width)
#                ax.set_xticklabels(counts_all.keys())
#                ax.set_xlim([-width,max(x3)+ 1])
#                ax.set_yticks(range(0, 110, 10))
#                ax.set_ylim([0,100])
#                ax.legend((bar3[0], bar1[0], bar2[0]), ('all', '50000+', '- 50000') )
#                autolabel(bar1,1,num_element)
#                autolabel(bar2,2,num_element)
#                autolabel(bar3,3,num_element)
#                ax.annotate(census_all.describe(), xy=(0.5, 0.9), xycoords='axes fraction', ha = 'center', va = 'top', bbox={'facecolor':'white'})
#                plt.title(column, fontsize = 15)
#                if len(x3) > 5 or column == "citizenship":
#                        plt.xticks(rotation = 'vertical')
#                fig.set_size_inches(12, 6)               
#                fig.tight_layout()
#                
#                # Display the figure
#                plt.show()
##                print "\n" * 10
#                
#        else:
#                fig, ax = plt.subplots(3, sharex = True)
#                fig.suptitle(column, fontsize = 15)
#                ax[0].annotate(census_all.describe(), xy=(0.5, 0.9), xycoords='axes fraction', ha = 'center', va = 'top', bbox={'facecolor':'white'})
#                ax[0].axis('off')
#                ax[1].hist(census_all, color = ppl.colors.set2[1], normed = True, edgecolor = "white", label = 'all')
#                ax[1].legend()
#                ppl.utils.remove_chartjunk(ax[1], ['top', 'right'])
#                ax[2].hist((census_fifty, census_not_fifty), color = [ppl.colors.set2[0], ppl.colors.set2[2]], normed = True, edgecolor = "white", label = ['50000+', '- 50000'])
#                ppl.utils.remove_chartjunk(ax[2], ['top', 'right'])                
#                ax[2].legend()
#                fig.set_size_inches(14, 10)
#                plt.show()
#                print "\n" * 10                

# Create the training sample array

# Step 1: Transform categorical data into dummy variables
train_X=train_census_data.ix[:, categorical_columns]
train_X = train_X.T.to_dict().values()
vectorizer = DictVectorizer( sparse = False )
train_X = vectorizer.fit_transform(train_X)
train_X_names = vectorizer.get_feature_names()

## Step 2: Remove the columns that don't explain much
to_del = []
for index, element in enumerate(train_X_names):
    if train_X_names[index] in small_difference:
        to_del.append(index)

train_X = np.delete(train_X, to_del, axis=1)

for offset, index in enumerate(to_del):
    index -= offset
    del train_X_names[index]
 
## Step 3:  Join numerical and categorical array   
train_X = np.hstack((train_X, train_census_data.ix[:, numerical_columns]))
train_X_names.extend(numerical_columns)

# Create the training sample array of the classes
train_Y = train_census_data['50K']

# Classify
clf = tree.DecisionTreeClassifier(min_samples_leaf=1000)
clf = clf.fit(train_X, train_Y)

# Create a pdf of the tree
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names = train_X_names)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("50K-tree.pdf")

del train_X
del train_Y
del train_census_data


test_data_file = os.path.join(data_directory, 'census_income_test.csv')
census_header = ["age", "class of worker", "industry code", "occupation code", "education", "wage per hour", "enrolled in edu inst last wk", "marital status", "major industry code", "major occupation code", "race", "hispanic Origin", "sex", "member of a labor union", "reason for unemployment", "full or part time employment stat", "capital gains", "capital losses", "divdends from stocks", "tax filer status", "region of previous residence", "state of previous residence", "detailed household and family stat", "detailed household summary in household", "instance weight", "migration code-change in msa", "migration code-change in reg", "migration code-move within reg", "live in this house 1 year ago", "migration prev res in sunbelt", "num persons worked for employer", "family members under 18", "country of birth father", "country of birth mother", "country of birth self", "citizenship", "own business or self employed", "fill inc questionnaire for veteran's admin", "veterans benefits", "weeks worked in year", "year of census", "50K"]
test_census_data = pd.read_csv(test_data_file, names = census_header, header = None)
del test_census_data["instance weight"]
census_header.remove("instance weight")
continuous_col = ['industry code', 'occupation code', 'own business or self employed', 'veterans benefits', 'year of census']
for col in continuous_col:
    test_census_data[col] = test_census_data[col].astype(str)
# Create the testing sample array

## Step 1: Transform categorical data into dummy variables
test_X=test_census_data.ix[:, categorical_columns]
test_X = test_X.T.to_dict().values()
vectorizer = DictVectorizer( sparse = False )
test_X = vectorizer.fit_transform(test_X)
test_X_names = vectorizer.get_feature_names()

## Step 2: Remove the columns that don't explain much
test_X = np.delete(test_X, to_del, axis=1)

for offset, index in enumerate(to_del):
    index -= offset
    del test_X_names[index]
 
## Step 3:  Join numerical and categorical array   
test_X = np.hstack((test_X, test_census_data.ix[:, numerical_columns]))
test_X_names.extend(numerical_columns)

# Create the testing sample array of the classes
test_Y = test_census_data['50K']

print test_X
trained_Y = clf.predict(test_X)

print trained_Y
