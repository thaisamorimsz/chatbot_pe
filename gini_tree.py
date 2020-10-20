# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus


col_names = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15','expensive']
col_cri_names = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
criterios = pd.read_csv("criterios.csv",sep=",",header=0,names=col_cri_names)

accuracy_file = open("precisoes","w")

for i in range(0,len(criterios)):
    # load dataset
    data = pd.read_csv("nossas_casas_tratadas_"+str(i)+".csv", header=0, names=col_names)

    print(data)

    #split dataset in features and target variable
    feature_cols = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
    X = data[feature_cols] # Features
    y = data.expensive # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0) # 95% training and 5% test


    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion="gini")

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    accuracy_file.write("Precisao para o "+str(i)+"o conjunto de criterios: "+str(metrics.accuracy_score(y_test, y_pred))+"\n")

    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True, feature_names = feature_cols,class_names=['barato','caro'],node_ids=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('arvore_casas_'+str(i)+'.png')
    Image(graph.create_png())


accuracy_file.close()