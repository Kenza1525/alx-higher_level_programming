#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv[1:])
    if num_arg == 0:
        print("{} arguments.".format(num_arg))
    elif num_arg == 1:
        print("{} argument:".format(num_arg))
        print("{}: {}".format(num_arg, argv[1]))
    else:
        print("{} arguments:".format(num_arg))
        i = 1
        while(num_arg >= i):
            print("{}: {}".format(i, argv[i]))
            i += 1
