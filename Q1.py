str2=""
with open("onelinefile.txt") as f:
    contents = f.read() 
    for i in range(len(contents)):
        if contents[i].isnumeric() or (not contents[i].isalnum()):
            if contents[i-1].isalpha():
                str2=str2+" "+contents[i]
            else:
                str2=str2+contents[i]
        if contents[i].isalpha():
            if contents[i-1].isnumeric():
                str2=str2+" "+contents[i]
            else:
                str2=str2+contents[i]
    li=str2.split()
    l2=fi=[]
    m=0
    while m<len(li):
        l2=[]
        for j in range(4):
            l2.append(li[m])
            m+=1
        fi.append(l2)
    import csv
    with open("Filename2.csv",'w',newline='') as w:
        writer=csv.writer(w,delimiter=',')
        for n in fi:
            writer.writerow(n)