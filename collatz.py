def collatz(nr):
    if nr % 2 == 0:
        return nr//2
    else:
        return 3*nr+1


while True:
    nr = input()
    try:
        nr = int(nr)
        break
    except ValueError:
        print("Please enter a number!")
res = collatz(nr)
while res != 1:
    print(res)
    res = collatz(res)
print(res)
