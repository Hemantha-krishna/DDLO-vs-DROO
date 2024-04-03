import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_csv('transactions.csv')
    return df

def exercise_1(df):
    column_names = df.columns.tolist()
    print(column_names)


def exercise_2(df, k):
    k = int(input("Enter the value of k:"))
    first_k_rows = df.head(k)
    print(first_k_rows)


def exercise_3(df, k):
    k = int(input("Enter the value of k:"))
    random_sample = df.sample(k)
    print(random_sample)


def exercise_4(df):
    unique_types = df['type'].unique().tolist()
    print(unique_types)


def exercise_5(df):
    top_destinations = df['nameDest'].value_counts().head(10)
    print(top_destinations)


def exercise_6(df):
    fraud_rows = df[df['isFraud'] == True]
    print(fraud_rows)


def exercise_7(df):
    pass

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass

df = exercise_0('transactions.csv')
exercise_1(df)
exercise_2(df,5)
exercise_3(df,3)
exercise_4(df)
exercise_5(df)
exercise_6(df)