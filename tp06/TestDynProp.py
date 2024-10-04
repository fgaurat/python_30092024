


class TestDynProp:
    __slots__ = ("a")

    def __init__(self,a) -> None:
        self.a=a


def main():
    t = TestDynProp(2)
    print(t.a)
    print(t.__dict__)


if __name__=='__main__':
    main()
