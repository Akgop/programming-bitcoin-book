from ecc import FieldElement

if __name__ == '__main__':
    a = FieldElement(7, 13)
    b = FieldElement(6, 13)
    print(a == b)
    print(a != b)
    print((a + b).num)
    print((a - b).num)
    print((a * b).num)
    print((a / b).num)