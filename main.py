class A:
    shared_list = []
    def __init__(self,value):
        self.shared_list.append(value)

a1 = A(1)
a2 = A(2)
a3 = A(3)
print(A.shared_list)
