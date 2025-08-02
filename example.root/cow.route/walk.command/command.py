import sys
def main():
    args = list(sys.argv)
    if '--loud' in args:
        print("I AM A COW AND I LIKE LOUDLY WALKING")
    else:
        print("I am a cow and I like walking")

if __name__ == '__main__':

    main()
