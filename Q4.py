import numpy as np     
li=[]
while 1:
    ch=int(input("1.enter data 2.exit: "))
    if ch==1:
        n=int(input('enter the number of rows :'))
        for i in range(n):
            name=input("enter the name: ")
            price=input("enter the price: ")
            rating=int(input("enter the rating(out of 5): "))
            l=(name,price,rating)
            li.append(l)
        data_type = [('name', 'S15'), ('price', float), ('rating', int)]
        food = np.array(li, dtype=data_type) 
        print(np.sort(food, order='rating')) 
    if ch==2:
        break