# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
import numpy as np
import csv


col_names = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15','expensive']
col_cri_names = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
criterios = pd.read_csv("D:/workspace/chatbot_pe/criterios.csv",sep=",",header=0,names=col_cri_names)

accuracy_file = open("D:/workspace/chatbot_pe/precisoes","w")
row_output = []

chatbot_tree_col_names = ['ID','Pergunta','A','Nó A','B','Nó B']

for j in range(0,len(criterios)):

    chatbot_tree = open(str("D:/workspace/chatbot_pe/arvore_"+str(j)+".csv"),"w")
    chatbot_tree_writer = csv.writer(chatbot_tree, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    chatbot_tree_writer.writerow(chatbot_tree_col_names)

    # load dataset
    data = pd.read_csv("D:/workspace/chatbot_pe/nossas_casas_tratadas_"+str(j)+".csv", header=0, names=col_names)

    print(data)

    #split dataset in features and target variable
    feature_cols = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
    X = data[feature_cols] # Features
    y = data.expensive # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=1) # 95% training and 5% test


    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion="gini")

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    accuracy_file.write("Precisao para o "+str(j)+"o conjunto de criterios: "+str(metrics.accuracy_score(y_test, y_pred))+"\n")

    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True, feature_names = feature_cols,class_names=['barata','cara'],node_ids=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('D:/workspace/chatbot_pe/arvore_casas_'+str(j)+'.png')
    Image(graph.create_png())

    children_left_array = clf.tree_.children_left #array of left children
    children_right_array = clf.tree_.children_right #array of right children
    features_array = clf.tree_.feature #array of nodes splitting feature
    values_array = clf.tree_.value

    for x in range(0,len(children_left_array)):
        row_output.append(x)
        if children_left_array[x] < 0 and children_right_array[x] < 0:
            row_output.append("NÓ FOLHA")
            if not np.argmax(values_array[x]):
                row_output.append("Essa casa provavelmente é barata.")
            else:
                row_output.append("Essa casa provavelmente é cara.")
        else:
            row_output.append(str(col_cri_names[features_array[x]])+"<="+str(criterios.iloc[0][features_array[x]])+"?")   
            row_output.append("SIM")
            row_output.append(children_left_array[x])
            row_output.append("NÃO")
            row_output.append(children_right_array[x])
        
        chatbot_tree_writer.writerow(row_output)
        row_output = []
    
accuracy_file.close()