def pyramid_print(layers):
    top_size = layers
    for i in range(layers):
        top_size += 1
        for j in range(top_size):
            if j > (top_size - 3) - i * 2:
                print("-", end='')
            else:
                print(" ", end='')
        print()


pyramid_print(100)