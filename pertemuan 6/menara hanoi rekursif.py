Cakram = int(input("Masukan Jumlah Cakram : "))

def hanoiRecur(num, src, helper, goal):
    if num == 1:
        print("Pindahkan cakram 1 dari " + src + " ke " + goal)
    else:
        hanoiRecur(num - 1, src, goal, helper)
        print("Pindahkan cakram " + str(num) + " dari " + src + " ke " + goal)
        hanoiRecur(num - 1, helper, src, goal)

    
hanoiRecur(Cakram, 'A', 'B', 'C')