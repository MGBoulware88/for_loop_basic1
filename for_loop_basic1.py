# # Basic - Print all integers from 0 to 150.
# for i in range(150):
#     print(i)

# # Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# for i in range(5,1000,5):
#     print(i)

# # Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# for i in range(100):
#     if i % 10 == 0:
#         print("Coding Dojo")
#     elif i % 5 == 0:
#         print("Coding")
#     else: print(i)

# # Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# sum = 0
# for i in range(500000):
#     if i % 2 == 0:
#         continue
#     sum+=i
# print(sum)

# #or
# odd_sums=0
# for i in range(1,500000,2):
#     odd_sums+=i
# print(odd_sums)

# # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# x = 2018
# while x > 0:
#     print(x)
#     x-=4
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
low_num = 2
high_num = 9
mult = 3
for num in range(low_num,high_num):
    if num % mult == 0:
        print(num)



