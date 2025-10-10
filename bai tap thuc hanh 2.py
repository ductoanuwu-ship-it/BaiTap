#print("hello world")
#print("HoDucToan_MSSV:245752021610012_KTDKvaTDH")

#bai 1
#n1 = int(input("enter n1 value"))
#n2 = int(input("enter n2 value"))
#if n1 > n2:
 #   print("n1 is big")
#else:
#    print("n2 is big")

#bai 2
#def khoang_cach(x1, y1, x2, y2):
#    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#print(khoang_cach(5, 2, 4, 5))

#bai 3

# Kiểm tra số chẵn lẻ
#n = int(input("nhap gia tri cua n: "))

#if n % 2 == 0:
#    print("n la so chan")
#else:
#    print("n la so le")

#bai 4

# Hàm in nghịch đảo các số tự nhiên trong khoảng (a, b)
#def in_nghich_dao(a, b):
#    print(f"Nghịch đảo các số tự nhiên trong khoảng ({a}, {b}):")
 #   for i in range(a + 1, b):   
#        nghich_dao = 1 / i
#        print(nghich_dao)
#bai 5

#n = int(input("Nhập số tự nhiên n (>0): "))
if n > 0:
    for i in range(n, -1, -1):  
        print(i)
else:
    print("Vui lòng nhập số tự nhiên lớn hơn 0!")

#bai 6
dict=[]
for i in range(2000, 3201):
    if(i%7==0) and (i%5!=0):
        dict.append(str(i))
print(",".join(dict))

#bai 7

n = int(input("Nhập số nguyên n: "))

dict = {}
for i in range(1, n+1):
    dict[i] = i * i

print(dict)

#8
a, b = 1, 2
total = 0

while a < 4000000:
    print(a, end=" ")        
    if a % 2 == 0:
        total += a
    a, b = b, a + b
print()                      
print("numbers < 4000000:", total)

#9
s = input("Enter a String")
d = {}
for i in s:
    d[i] = s.count(i)
print(d)

#10 
a = "ke huy diet"
b = a.split()
print(b)
c = " ".join(b)
print(c)

#13
import math   


a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có 1 nghiệm: x =", x)
else:
   
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép: x =", x)
    else:
        print("Phương trình vô nghiệm (Δ < 0)")

#12
passwords = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ")
list_pw = passwords.split(",")
valid_pw = []
for pw in list_pw:
    if len(pw) < 6 or len(pw) > 12:
        continue  
    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu = False

    for ch in pw:
        if ch >= 'a' and ch <= 'z':
            co_chu_thuong = True
        elif ch >= 'A' and ch <= 'Z':
            co_chu_hoa = True
        elif ch >= '0' and ch <= '9':
            co_so = True
        elif ch in "$#@":
            co_ky_tu = True

    
    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu:
        valid_pw.append(pw)


print("Mật khẩu hợp lệ là:", ",".join(valid_pw))

#11
keys = ['Ten', 'Tuoi', 'Lop']
values = ['Toan', 20, '12A']
my_dict = dict(zip(keys, values))

print("Từ điển sau khi kết nối là:")
print(my_dict)
