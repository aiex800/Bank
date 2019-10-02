ef main():
    f = open('bankpengar.txt','r')
    if f.mode == "r":
        contents = f.read()
        print(contents)

if __name__== "__main__":
    main()
main()d