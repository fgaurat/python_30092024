

def get_data():

    for i in range(1000):
        yield i

def main():
    d = get_data()
    all = list(d)
    print(all[12])
    # i = next(d)
    # print(i)
    # i = next(d)
    # print(i)
    # for i in d:
    #     print(i)


if __name__=='__main__':
    main()
