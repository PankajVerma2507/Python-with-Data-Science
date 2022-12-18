# from random import randint
# def hello():
#     print("hola")
#     print("AMIGOS")
#     print("👌👌👌")

# def roll_dice():
#     dices = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
#     print(" => ",dices[randint(0,5)])

# # CALL
# hello()
# hello()
# hello()

# roll_dice()
# roll_dice()
# roll_dice()

# # return keyword
# def get_salary():
#     val = int(input("enter amount"))
#     fine = .09
#     sal = val * fine
#     return sal
# print(get_salary)
# ans = get_salary()
# print("salary",ans)

# final_salary = get_salary() + 1000
# print('salary', final_salary)

# def amount():
#     p = int(input('principle:'))
#     r = .34(input('rate:'))
#     t = int(input('time:'))

#     si =p*r*t/100
#     amt = si + p
#     return amt, si

# amt, si = amount()
# print(f'the Amount will we {amt} on simple interest {si}')
 
# # or this way
# print(f'the Amount will be {amount()[0]}')

# function 3

def word_count(msg):
    words = msg.split()
    
word_count("this is time to go")
return len(words)