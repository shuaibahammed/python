def check_scope():
    def do_local():
        test="local test"
    def non_local():
        nonlocal test
        test="non local test"
    def do_global():
        global test
        test="global test"

    test="default"
    do_local()
    print("do local is " +test)
    non_local()
    print("non local is " +test)
    do_global()
check_scope()
print("main" +test)
