# num = 5

# while num < 10:
#     print (f"The number {num} is less than 10")
#     num +=1

# num = input ("Enter the number : ")
# num_1 = int(num)
# while num_1 < 100:
#     print (f"The number {num_1} is less than 100")
#     num_1 +=1

num = input ("Enter the number : ")        # Enter the number
num_1 = int(num)                           # Convert the num variable from str to int as Str
while num_1 < 100:                         # while loop condition
    print (f"The number {num_1} is less than 100")
    if num_1 == 75:                        # condition to break the while loop
        break
    num_1 +=1