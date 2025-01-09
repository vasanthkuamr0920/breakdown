import pandas as pd


def lines_read():
    df = pd.read_excel('itemnumbers.xlsx')
    
    df=df[['Line','Machines','Item No']]
    #print(df)
    return df


if __name__== "__name__":

    lines_read()
    