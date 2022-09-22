#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv[1:])
    if num_arg == 0:
        print("{}".format(num_arg))
    else:
        i = 1
        sum_arg = 0
        while(num_arg >= i):
            sum_arg += int(argv[i])
            i += 1
        print("{}".format(sum_arg))
