'''Hãy phân tích trong tất cả các tiêu đề phim. Loại trừ ra các English stop word như: [a, an, the, to, and, this, that, but...],
hãy liệt kê 10 từ xuất hiện nhiều nhất trong tiêu đề phim'''
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
import re

df = pd.read_csv("movies.csv")
df["title2"] = df["title"].apply(lambda x: x[0:-6]) # ten phim duoc tach ra voi nam trong title
word_list = df["title2"].apply(lambda x: x.split(' ')) #tach tu` thanh` 1 phan tu? ngan cach boi space
xx_1 = [item for sublist in word_list for item in sublist] #list cac tu` trong title

#ham remove stopwords
def rm_stop_words(data, mode="nltk",silent=1):
    if silent==0:
        assert 0
    if mode == "nltk":
        stop_words = set(stopwords.words('english'))#list stopwords
    else:
        assert 0

    if isinstance(data,list):
        data = [i for i in data if i.lower() not in stop_words]#ca ki tu viet hoa cua stopwords
        return data
    else:#loai bo stopwords khoi list ban dau
        for word in stop_words:
            if word in data:
                del data[word]
item1 = []
for line in xx_1:
    line = ''.join(re.findall(r'[a-zA-Z]', line))#lay cac tu la chu cai a-z bo cac ki tu dac biet
    item1.append(line)

print(Counter(rm_stop_words(item1)))