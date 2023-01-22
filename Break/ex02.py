while True:
    f = int(input("Quer ver a tabuada de qual valor?"))
    if f  < 0:
        break
    for i in range(1, 10):
        print(f"{f} * {i} = {f * i}")
    