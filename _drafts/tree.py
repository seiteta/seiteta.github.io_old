import pandas as pd
import os
import pydot 
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals.six import StringIO  


data_directory = r'C:\Users\Fred\Desktop\us_census_full'

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




X=census_data.ix[:,("sex", "race")]
X = X.T.to_dict().values()
vectorizer = DictVectorizer( sparse = False )
X = vectorizer.fit_transform(X)
X_names = vectorizer.get_feature_names()


Y = census_data['50K']


clf = tree.DecisionTreeClassifier(min_samples_leaf=1000)

clf = clf.fit(X, Y)




dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data, feature_names = X_names) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris2.pdf")



Useful links:
http://statcompute.wordpress.com/2012/12/05/learning-decision-tree-in-scikit-learn-package/
http://statcompute.wordpress.com/2012/12/05/decision-tree-with-python/
http://fastml.com/converting-categorical-data-into-numbers-with-pandas-and-scikit-learn/
https://github.com/zygmuntz/kaggle-happiness/blob/master/vectorize_validation.py
