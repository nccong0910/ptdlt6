import pandas as pd
from scipy.stats import pearsonr
from collections import Counter


df = pd.read_csv("movies.csv")
genres_list = df["genres"].apply(lambda x: x.split('|'))

flat_list = [item for sublist in genres_list for item in sublist]


s = Counter(flat_list)
list_check = list(s.keys())
print(list_check)
pd.set_option('display.max_columns', 25)
pd.set_option('display.width', 3000)
frame = pd.DataFrame({'ID':df['movieId'],
                      'Genres':genres_list})

for i in list_check:
    frame[i] = [1 if i in rows else 0 for rows in frame['Genres']]
print(frame)


def correlation(x, y):
    return pearsonr(frame[x], frame[y])

x = input("Type x : ")
y = input("Type y : ")
C = correlation(x, y)
print(" - Correlation coefficient between {0} and {1} is : ".format(x, y), C)



