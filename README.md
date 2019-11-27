# ptdlt6
'''Mỗi bộ phim được phân loại vào nhiều thể loại phim.
Làm sao có để biết các thể loại phim nào hay xuất hiện cùng nhau trong 1 bộ phim?

Ví dụ: Toy Story và Jumanji có chung thể loại [Adventure, Children, Fantasy] 
Toy Story với 'Tom and Huck' chung thể loại [Adventure, Children]
Hãy sử dụng phương pháp tính correlation để tìm ra xác suất xuất hiện đồng thời của 2 thể loại phim bất kỳ.
'''

*Bước 1 : import các thư viện cần thiết , với pandas để xử lý & tổ chức dữ liệu , scipy để tạo hàm tính toán thống kê

<img src="https://i.imgur.com/LKXEjxW.png">

*Bước 2 : <p> _ Tiến hành load dataset "movies.csv" thành một Dataframe<br></p>
          <p> _ Tạo ra Pandas Series "genres_list" , dùng hàm lambda áp dụng cho Dataframe "df" nhằm loại bỏ ký tự "|"<br></p>
          <p> _ Tạo ra "flat_list" để biến "genres_list" thành một list chung ,
          nhằm thuận tiện cho việc lọc ra tên các thể loại phim<br></p>
          <p>_ Sử dụng hàm built-in Counter của python để thống kê tần suất của các thể loại 
          & lưu lại tên các thể loại vào "list_check"<br></p>
          
<img src="https://i.imgur.com/4AcVGHV.png">

*Bước 3 : <p> _ Tạo Dataframe "frame" mới tổ chức lại "df" ở trên & nhằm tạo ra các cột dữ liệu mới cho từng thể loại phim<br></p>

<img src="https://i.imgur.com/Q82AOuC.png">

*Bước 4 : <p> _ Tạo một vòng lặp for lặp qua toàn bộ các thể loại phim được lưu trữ trong "list_check" ở bước 2<br></p>
          <p> _ Sử dụng kỹ thuật List Comprehension để đưa vào các giá trị 0 & 1 với điều kiện cụ thể : giá trị 1 nếu thể loại phim xuất hiện tương ứng trong "rows" là các hàng của "frame" mới tạo ở trên<br></p>
          <p> Thu được kết quả như hình : </p>
          
<img src="https://i.imgur.com/ENVHQtx.png">

*Bước 5 : <p> _ Tạo hàm correlation để tính toán hệ số tương quan & xem xét mức độ tương đồng ( affinity ) giữa các đối tượng
          ở đây cụ thể là các thể loại phim </p>

<img src="https://i.imgur.com/vjHeHl4.png">
