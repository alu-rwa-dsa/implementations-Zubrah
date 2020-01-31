
def repeating_int(num):
    for num in range(num + 1):
        for i in range(num):
            print(num, end= " ")

repeating_int(4) 
