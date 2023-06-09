import numpy as np

def doc_input (ten_file):  
    # doc file input.txt
    inp = open(ten_file, "r")
    # doc du lieu cua x va y
    x = inp.readline()
    y = inp.readline()
    c = int(inp.readline())
    # xu ly du lieu cua x va y
    x = x.strip().split()
    x = np.array(x, dtype=float)
    y = y.strip().split()
    y = np.array(y, dtype=float)
    inp.close()
    return x, y, c

def kiem_tra_input (x, y):
    #tra ve 1 khi input hop le va 0 khi input khong hop le
    # kiem tra kich thuoc du lieu
    if (x.shape[0] != y.shape[0]):
        print("kich thuoc khong hop le")
        return 0
    # kiem tra du lieu trung
    for i in x:
        if (np.where(x == i)[0].shape[0] > 1):
            print("du lieu cua x o cac vi tri ", np.where(x == i)[0], " trung nhau")
            return 0
    # kiem tra du lieu trung voi c
    if (np.where(x == c)[0].shape[0] > 0):
        print("gia tri c bi trung voi x o cac vi tri ", np.where(x == c)[0])
        return 0
    # input hop le
    print("input hop le")
    return 1

def hoocne_quatient(a, x):
    # chia gia tri cua da thuc P(x) cho (x - x_0)
    # tra ve b và b_0 trong do:
    # b la he so cua da thuc sau khi chia
    # b_0 la phan du va la ket qua cua P(x_0)
    y = list()
    y.append(a[0])
    for i in range(len(a) - 1):
        y.append(y[i] * x + a[i + 1])
    b = np.array(y[:-1])
    b_0 = np.array(y[-1])
    return b, b_0

def hoocne_product(x):
    #tich cua cac nghiem
    # a la he so sau khi nhan tat ca ca nghiem
    a = list()
    a.append(np.array([1, 0]))
    for i in x:
        b = a[-1]
        c = list()
        c.append(1)
        for j in range(len(b) - 1):
            c.append(b[j + 1]- b[j] * i)
        c.append(0)
        a.append(np.array(c))
    return np.delete(a[-1], -1)

def D_i(x, i):
    # tinh tich cua x_i - x_j khi i != j, j = 0, n
    d = 1.0
    for j in range(x.shape[0]):
        if j != i:
            d *= x[i] - x[j]
    return d

def aiken(x, y, c):
    n = x.shape[0]
    Pn_c = 0
    omega = hoocne_product(x)
    omega_c = hoocne_quatient(omega, c)[1]
    for i in range(n):
        Ei = (c - x[i]) * D_i(x, i)
        Pn_c += omega_c * (y[i] / Ei)
    return Pn_c

x, y, c = doc_input("input.txt")
if (kiem_tra_input(x, y)):
    Pn_c = aiken(x, y, c)
    print("gia tri cua Pn({}) = {}".format(c, Pn_c))