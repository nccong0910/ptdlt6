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

'''tạo column year dùng hàm lambda tách ra khỏi cột title'''
df["year"] = df["title"].apply(lambda x: x[-5:-1])

'''tạo genres_list '''
genres_list = df["genres"].apply(lambda x: x.split('|'))


'''Tạo list comprehension chứa tất cả phần tử thuộc genres'''
flat_list = [item for sublist in genres_list for item in sublist]
'''Sử dụng built-in function Counter để tính tần suất xuất hiện các thể loại phim'''
s = Counter(flat_list)
M = s.most_common(7) #đưa ra
G = dict(M)
print("Đáp án câu 1: ", s)

print("_____*_____")

'''Tạo không gian chứa các biểu đồ bằng hàm figure() & subplot() của thư viện Matplotlib'''
plt.figure(figsize=(20, 15))
plt.subplot(2, 2, 1)
plt.bar(list(G.keys()), list(G.values()))
plt.title("Biểu đồ so sánh độ phổ biến của các thể loại phim")

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
plt.subplot(2, 2, 2)
plt.plot(X1, X2, color='orange')
plt.xlabel("years")
plt.ylabel("Frequency")
plt.title("Thể loại Drama qua các năm")


#__________________câu 4_____________________
df_comedy = df[df["genres"] == "Comedy"] #tạo cột comedy
df_thriller = df[df["genres"] == "Thriller"] #tạo cột thriller
'''Tạo 2 list chứa các giá trị là các năm 2 thể loại Comedy & Thriller xuất hiện'''
flat_list4 = [j for j in df_comedy["year"]]
flat_list5 = [k for k in df_thriller["year"]]
digit2 = []
digit3 = []
'''Lọc các giá trị số năm nhiễu, sai lệch'''
for z2 in flat_list4:
    if z2.isdigit():
        digit2.append(z2)

for z3 in flat_list5:
    if z3.isdigit():
        digit3.append(z3)
'''Lưu các số liệu đã xử lý vào 2 list digit mới rồi thống kê tần số qua các năm'''

Y = Counter(digit2)
Z = Counter(digit3)

'''Dùng vòng lặp qua 3 danh sách để lấy những năm cùng nhau trong 3 thể loại tiện cho việc so sánh'''
Listsum = []
for a in X:
    for b in Y:
        for c in Z:
            if int(a) == int(b) == int(c):
                Listsum.append(a)
print(sorted(Listsum))
years = sorted(Listsum)[40:48]
print(years)
'''Đưa các giá trị lấy được qua các năm tương ứng nhau của 3 thể loại vào 3 list đếm 
dùng làm tham số cho hàm plot'''
count_drama = [61, 70, 83, 95, 93, 100, 107, 116]
count_comedy = [39, 52, 40, 66, 53, 42, 64, 57]
count_thriller = [6, 5, 6, 4, 5, 9, 7, 7]
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)
plt.plot(years, count_drama, color='red')
plt.plot(years, count_comedy, color='green')
plt.plot(years, count_thriller, color='orange')
plt.xlabel("3 Genres")
plt.ylabel("Frequency")
plt.title("4.Tăng giảm 3 thể loại phổ biến nhất")
plt.show()

<img src="https://i.imgur.com/fhQfX55.png">
