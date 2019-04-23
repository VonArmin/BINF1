def main():
    x1 = 0
    x2 = 50
    while True:
        if x1 < x2:
            print(x1*'0')
        x1 += 1
        if x1 > 50:
            print(x2*'0')
            x2 -= 1
            if x2 == 0:
                x2 = 50
                x1 = 0


main()
