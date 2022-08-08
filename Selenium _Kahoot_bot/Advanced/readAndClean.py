import pandas as pd

# Global variables
code = 101516

# Here it start the function


def kahootstart(username):
    # Qui parte la funzione di python
    # qui dentro devo usare il code
    if(username == "Charles"):
        print(username)

# Here I create the array with all the names i need


def dataScraping():
    # Creating the list i need
    df = pd.read_csv("baby-names.csv")
    df = df.iloc[:, 1:2]
    df = df.drop_duplicates()
    df = df.iloc[0:100, :]

    a = df.loc[[3]].values
    print(a)
    for i in range(0, df.size):
        # Qui lancio il loop
        #kahootstart(df.iloc[i, 1:2])
        #print(df.iloc[i, 1:2])
        a = df.loc[[i]].values.astype(str)
        kahootstart(a)


if __name__ == "__main__":
    dataScraping()
