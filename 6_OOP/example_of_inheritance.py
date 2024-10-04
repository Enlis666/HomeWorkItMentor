class A:
    def __init__(self):
        print("A.__init__ called")
        super().__init__()


class B(A):
    def __init__(self):
        print("B.__init__ called")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__ called")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D.__init__ called")
        super().__init__()