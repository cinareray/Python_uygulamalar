l1 = [(x+1, x+2, x+3, x+4) for x in range(4)]
print(l1)

def f(x):
    return x+1

def main():
    l2 = list(map(lambda x:x+1 , range(4)))
    print(l2)
    l3 = list(map(f,l2))
    print(l3)
    l4=list(map(f,l3))
    print(l4)
    l5 = list(map(f,l4))
    print(l5)
    l6=list(map(f, l5))
    print(l6)

if __name__ == '__main__':
    main()