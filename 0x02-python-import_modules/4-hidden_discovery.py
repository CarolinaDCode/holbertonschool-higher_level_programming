#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as lista
    modules = dir(lista)
    for i in range(0, len(modules)):
        if (modules[i][0] != '__'):
            print(modules[i])
