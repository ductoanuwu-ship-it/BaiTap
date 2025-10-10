#def sum(a,b):
#   print("sum=" + str(a+b))
#sum(2,3)

#def sum(a,b):
#    return a+b
#c=sum(3,5)
#print("tong a b la"+str(c))
#def say_hello():
#    a ="hello"
#    print(a)
#say_hello()
#a = "Hello Guy!" 
#def say(a):
#    a="vinhunivercity"
 #   print(a)
#say(a)
#print(a)
#a="hello guy"
#def say():
#    global a
#    a="vinh universesity"
#    print(a)
#say()
#print(a)
#def get_sum(*num):
#    tmp=0
#    for i in num:
#        tmp += i
#        return tmp
#c=get_sum(1,2,3,4,8)
#print(c)
#ham get sum tao ra mot tui dung chua nhieu cac phan tu nhu string hoac so,tmp=0, lap lai i ben trong nam tmp+=i roi cu the lap lai cong cac gia tri khi chung ta dung ham

#def chanle(n):
#    if n%2==0:
#        print("nla so chan")
#    else:
#        print("n la so le")
#print(chanle(3))

#import math
##def tinh(R):
  #  if(R<=0):
   #     print("khong hop le")
    #else:
     #   C=2*math.pi*R
      #  S=math.pi*R*R
       # print(f"chu vi hinh tron:{C}")
        #print(f"dien tich hinh tron:{S}")
#R= float(input("nhap ban kinh: "))
#tinh(R) 
def benefit(t,n,k):
    L=t*n*k
    T=t+L
    print(f"tien lai:{L}")
    print(f"tong tien lai: {T}")
t= float(input("tien goc: "))
n= float(input("lai xuat: "))
k= float(input("thoi gian: "))
benefit(t,n,k)