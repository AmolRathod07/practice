i= (1,5,9,12,25,17,37)
print(i)

# for num in i :
#     if num>10 :
#         print("greater")
#     else:
#         print("less")
great_than=[]
less_than=[]
for num in i :
    if num>10 :
        great_than.append(num)
    else:
        less_than.append(num)

print("numbers greater than 10 are:",great_than)
print("numbers Less than 10 are:",less_than)

