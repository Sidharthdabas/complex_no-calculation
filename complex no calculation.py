class complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(num1,num2):
        new_real = num1.real + num2.real
        new_img = num1.img + num2.img
        return complex(new_real,new_img)
    
    def __sub__(num1,num2):
        new_real = num1.real - num2.real
        new_img = num1.img - num2.img
        return complex(new_real,new_img)
    
    def __mul__(num1,num2):
        new_real = num1.real * num2.real
        new_img = num1.img * num2.img
        return complex(new_real,new_img)
    
    def __truediv__(num1,num2):
        new_real = num1.real / num2.real
        new_img = num1.img / num2.img
        return complex(new_real,new_img)

print("first complex number is :")
num1 = complex(2,3)
num1.shownumber()
print("second complex number is :")
num2 = complex(4,5)
num2.shownumber()

print("answer after add is :")
num3 = num1 + num2
num3.shownumber()

print("answer after sub is :")
num4 = num1 - num2
num4.shownumber()

print("answer after mul is :")
num5 = num1 * num2
num5.shownumber()

print("answer after div is :")
num6 = num1 / num2
num6.shownumber()
