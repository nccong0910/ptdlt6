'''Mỗi bộ phim được phân loại vào nhiều thể loại phim. Làm sao có để biết các thể loại phim nào hay xuất hiện cùng nhau trong 1 bộ phim?

Ví dụ: Toy Story và Jumanji có chung thể loại [Adventure, Children, Fantasy] Toy Story với 'Tom and Huck' chung thể loại [Adventure, Children]
Hãy sử dụng phương pháp tính correlation để tìm ra xác suất xuất hiện đồng thời của 2 thể loại phim bất kỳ.

Gợi ý: Cần tạo ra data frame mới bổ xung các cột, mỗi cột tương ứng với một thể loại phim.
Thể loại nào có trong phim nhận giá trị 1, còn không có nhận giá trị 0.'''
import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv("movies.csv")
genres_list = df["genres"].apply(lambda x: x.split('|'))

#Tạo list comprehension chứa tất cả phần tử thuộc genres
flat_list = [item for sublist in genres_list for item in sublist]

pd.set_option('display.max_columns', 25)
pd.set_option('display.width', 3000)

# Tạo dataframe mới bổ sung các cột, mỗi cột ứng với một thể loại phim ( 20 thể loại )
frame = pd.DataFrame({
    'ID': df["movieId"],
    'Genres': genres_list,
    'no genres listed': [1 if 'no genres listed' in rows else 0 for rows in genres_list],
    'Action': [1 if 'Action' in rows else 0 for rows in genres_list],
    'Adventure': [1 if 'Adventure' in rows else 0 for rows in genres_list],
    'Animation': [1 if 'Animation' in rows else 0 for rows in genres_list],
    'Children': [1 if 'Children' in rows else 0 for rows in genres_list],
    'Comedy': [1 if 'Comedy' in rows else 0 for rows in genres_list],
    'Crime': [1 if 'Crime' in rows else 0 for rows in genres_list],
    'Documentary': [1 if 'Documentary' in rows else 0 for rows in genres_list],
    'Drama': [1 if 'Drama' in rows else 0 for rows in genres_list],
    'Fantasy': [1 if 'Fantasy' in rows else 0 for rows in genres_list],
    'Film-Noir': [1 if 'Film-Noir' in rows else 0 for rows in genres_list],
    'Horror': [1 if 'Horror' in rows else 0 for rows in genres_list],
    'IMAX': [1 if 'IMAX' in rows else 0 for rows in genres_list],
    'Musical': [1 if 'Musical' in rows else 0 for rows in genres_list],
    'Mystery': [1 if 'Mystery' in rows else 0 for rows in genres_list],
    'Romance': [1 if 'Romance' in rows else 0 for rows in genres_list],
    'Sci-Fi': [1 if 'Sci-Fi' in rows else 0 for rows in genres_list],
    'Thriller': [1 if 'Thriller' in rows else 0 for rows in genres_list],
    'War': [1 if 'War' in rows else 0 for rows in genres_list],
    'Western': [1 if 'Western' in rows else 0 for rows in genres_list]
})
print(frame)
print(type(frame))

# Hàm tính correlation 2 thể loại phim
def correlation(x, y):
    return pearsonr(frame[x], frame[y])

x = input("Type x : ")
y = input("Type y : ")
C = correlation(x, y)
print("Correlation coefficient between {0} and {1} is: ".format(x,y),C)