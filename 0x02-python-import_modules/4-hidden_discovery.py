#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in range(0, len(dir(hidden_4))):
        names = dir(hidden_4)[i]
        if (names[0] != '_'):
            print(names)
