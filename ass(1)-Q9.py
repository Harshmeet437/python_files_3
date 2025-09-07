start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

for i in range(start_num, end_num + 1):
    for j in range(1, 11):
        print(i,"X",j ,"=", i * j)
    print("")