def swappingFile():
    text1 = input("enter files name:- ")
    text2 = input("enter files name:- ")

    with open(text1,'r')as a:
        data_a= a.read
    with open(text2,'r')as b:
        data_b= b.read   

    with open(text1,'w') as a:
        a.write(data_b)
    with open(text2,'w') as b:
        b.write(data_a)

        swappingFile()