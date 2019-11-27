# ptdlt6
'''Mỗi bộ phim được phân loại vào nhiều thể loại phim.
Làm sao có để biết các thể loại phim nào hay xuất hiện cùng nhau trong 1 bộ phim?

Ví dụ: Toy Story và Jumanji có chung thể loại [Adventure, Children, Fantasy] 
Toy Story với 'Tom and Huck' chung thể loại [Adventure, Children]
Hãy sử dụng phương pháp tính correlation để tìm ra xác suất xuất hiện đồng thời của 2 thể loại phim bất kỳ.
'''
<img src="https://i.imgur.com/LKXEjxW.png">

*Bước 1 : import các thư viện cần thiết , với pandas để xử lý & tổ chức dữ liệu , scipy để tạo hàm tính toán thống kê

<img src="https://i.imgur.com/4AcVGHV.png">

*Bước 2 : <p> _ Tiến hành load dataset "movies.csv" thành một Dataframe<br></p>
          <p> _ Tạo ra Pandas Series "genres_list" , dùng hàm lambda áp dụng cho Dataframe "df" nhằm loại bỏ ký tự "|"<br></p>
          <p> _ Tạo ra "flat_list" để biến "genres_list" thành một list chung ,
          nhằm thuận tiện cho việc lọc ra tên các thể loại phim<br></p>
          <p>_ Sử dụng hàm built-in Counter của python để thống kê tần suất của các thể loại 
          & lưu lại tên các thể loại vào "list_check"<br></p>

<img src="https://i.imgur.com/Q82AOuC.png">

*Bước 3 :

