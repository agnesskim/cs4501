def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n - 1)

def factorial2(n):
    counter = 1
    for n in range(0,n):
        x = n
        numb
        factorial1(n)
        return n
        n = n - 1

def test_fact1():
    assert factorial1(0) == 1., "Answer should be 1"
    assert factorial1(1) == 1., "Answer should be 1"
    assert factorial1(5) == 120., "Answer should be 120"

if __name__ == "__main__":
 test_fact1()

