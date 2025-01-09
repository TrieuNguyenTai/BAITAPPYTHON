# dùng hàm có đảo ngược chuỗi reversed()
a = input("\nnhap vao mot sau:")
rev = ''.join(reversed(a))
print("sau dao nguoc la:", rev)

#chỉ dùng hàm không dùng vòng lặp
a = input("\nnhap vao mot sau: ")
def function(a):
    return a[::-1]
rev = function(a)
print("sau dao nguoc la:", rev)

#chỉ dùng vòng lặp không dùng hàm
a = input("\nnhap vao mot sau:")
rev = []
for i in range(len(a)-1, -1, -1):
    rev.append(a[i])
rev = ''.join(rev)
print("sau đao nguoc la:",rev)
