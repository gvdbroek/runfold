import sys
def main():
    args = list(sys.argv)
    if '--loud' in args:
        print("MOOOOOOOO!")
    else:
        print("Moooooooo!")

if __name__ == '__main__':

    main()
