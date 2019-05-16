

def main():
    # Write your code here. Do not change any other parts of the code
    import pandas as pd
    import matplotlib.pyplot as plt
    
    #dataset = pd.read_csv('LRdata.csv', sep=";",index_col=0, decimal=",")
    #print(dataset)
    
    #dataset = pd.DataFrame(dataset,columns=['Age', 'Salary (k$)', 'Purchased'])
    #dataset = dataset.notnull()
    #dataset = dataset.astype('int64')
    
    #print(dataset)
    dataset = pd.read_csv('Purchase-Data.csv')
    
    x_columns = 2
    x = dataset.iloc[:, 0:x_columns].values
    y = dataset.iloc[:, x_columns].values
   
    #splitting the data into train and test data
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
   
    #feature scale for data set
    
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    
    
    from matplotlib.colors import ListedColormap
    color_map = ListedColormap(('red', 'green'))
    
    for i in [0,1]:
        plt.scatter(x[y == i, 0], x[y == i, 1], c=color_map(i))
    plt.xlabel('Age')
    plt.ylabel('Salary (k$)')
    
   
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(random_state=0)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    from sklearn.metrics import confusion_matrix
    confusion_matrix = confusion_matrix(y_test, y_pred)
    
    print(dataset)
    return model, confusion_matrix
main()
    










