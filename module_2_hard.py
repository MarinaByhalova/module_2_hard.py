numbers = [3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]
i = 0
def get_pair():
    global i,line
    number_1 = start
    number_2 = i+1
    if number%(number_1+number_2) == 0:
        line = f'{line}{number_1}{number_2}'
        return line

number = 19
line = ''
i = 0
i = i+1
start = 1
while start < number:
    while i < number:
        result = get_pair()
        if result:
            a = result
        i = i+1
    start = start +1
    i = start

print(number,a)


