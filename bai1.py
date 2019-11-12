'''1. Phân tích dữ liệu các bộ phim Hollywood
1.1.Hãy liệt kê tất cả các thể loại phim theo tần suất xuất hiện

1.2.Hãy vẽ biểu đồ bar chart, mỗi cột ứng với thể loại phim

1.3.Hãy vẽ biểu đồ line chart mô tả tăng giảm của thể loại drama qua các năm

1.4.Hãy vẽ biểu đô line chart mô tả tăng giảm của 3 thể loại phim phổ biến nhất qua các năm'''
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import itertools
from collections import OrderedDict

df = pd.read_csv("movies.csv")

'''Câu 1+ 2'''

df["year"] = df["title"].apply(lambda x: x[-5:-1]) #tạo column year dùng hàm lambda tách ra khỏi cột title
#print(df["year"])

genres_list = df["genres"].apply(lambda x: x.split('|'))


'''Tạo list comprehension chứa tất cả phần tử thuộc genres'''
flat_list = [item for sublist in genres_list for item in sublist]
s = Counter(flat_list)
M = s.most_common(7)
G = dict(M)
print("Đáp án câu 1:")
print(s) #đáp án câu 1
print("_____*_____")

#--đthi câu 2-----
plt.bar(G.keys(), G.values())
plt.xlabel("Genres")
plt.ylabel("Frequency")
plt.title("2.Biểu đồ cột")
plt.show()
#________________câu 3______________________
df_drama = df[df["genres"] == 'Drama'] #Tạo cột drama mới

flat_list3 = [i for i in df_drama["year"]]


digit = []
#Check numeric
for z in flat_list3:
    if z.isdigit():
        digit.append(z)
X = Counter(digit)

#Chọn 1 số phần tử ngẫu nhiên trong dict
T = dict(itertools.islice(X.items(), 7))
T1 = OrderedDict(sorted(T.items()))
X1 = list(T1.keys())
X2 = list(T1.values())

plt.plot(X1, X2, color='orange')
plt.xlabel("years")
plt.ylabel("Frequency")
plt.title("3.Thể loại Drama qua các năm")
plt.show()
#__________________câu 4_____________________
df_comedy = df[df["genres"] == "Comedy"] #tạo cột comedy
df_thriller = df[df["genres"] == "Thriller"] #tạo cột thriller
flat_list4 = [j for j in df_comedy["year"]]
flat_list5 = [k for k in df_thriller["year"]]
digit2 = []
digit3 = []
for z2 in flat_list4:
    if z2.isdigit():
        digit2.append(z2)

for z3 in flat_list5:
    if z3.isdigit():
        digit3.append(z3)

Y = Counter(digit2)
Z = Counter(digit3)

print("X la :", X)
print("Y la :", Y)
print("Z la :", Z)
R1 = OrderedDict(sorted(X.items()))
R2 = OrderedDict(sorted(Y.items()))
R3 = OrderedDict(sorted(Z.items()))
print("R1 : ", R1)
print("R2 : ", R2)
print("R3 : ", R3)

Listsum = []
for a in X:
    for b in Y:
        for c in Z:
            if int(a) == int(b) == int(c):
                Listsum.append(a)
print(sorted(Listsum))
years = sorted(Listsum)[40:48]
print(years)
count_drama = [61,70,83,95,93,100,107,116]
count_comedy = [39, 52, 40, 66, 53, 42, 64, 57]
count_thriller = [6, 5, 6, 4, 5, 9, 7, 7]

plt.plot(years, count_drama, color='red')
plt.plot(years, count_comedy, color='green')
plt.plot(years, count_thriller, color='orange')
plt.xlabel("3 Genres")
plt.ylabel("Frequency")
plt.title("4.Tăng giảm 3 thể loại phổ biến nhất")
plt.show()