
def print_del(pr1, pr2):
    print(int(int(pr1) / int(pr2)))


def print_umn(pr1, pr2):
    print(int(pr1) * int(pr2))


def print_min(pr1, pr2):
    print(int(pr1) - int(pr2))


def print_plus(pr1, pr2):
    print(int(pr1) + int(pr2))


b = input()
a = input()
c = input()
if a=='/':
    print_del(b,c)
elif a=='*':
    print_umn(b,c)
elif a=='-':
    print_min(b,c)
elif a=='+':
    print_plus(b,c)
else:
    print("не верный символ")











