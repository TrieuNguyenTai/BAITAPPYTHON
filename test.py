x=int(input("\nnhap so can tinh giai thua:"))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print("ket qua la:",fact(x))