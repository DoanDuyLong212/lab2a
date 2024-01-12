def showEmployee(a,b):
    print('Name: ',a,'salary: ',b)
    
showEmployee("Ben ",12000)
showEmployee("Jessica ",12000)


def outer_fun(a,b):
    tong = tinhTong(a,b)
    kq = tong + 5
    return kq

def tinhTong(a,b):
    sum = a + b
    return sum

result = outer_fun(5,10)
print(result)


