def maxmin(list):
    min = list [0];
    max = list[0];

    for i in list:
        if len(list) == 0:
        return 0
    for elm in list[1:]:
        if elem < min:
            min = elem
            return str(min)
        if elem > max:
            max = elem
            return str(max)

def common_items(list1, list2):
    output = []
    for elm in list1:
        if elm in list2:
            output.append(elm)
    return output

def testfunctions():
    assert common_items([1,2,3],[3,4,5]) == 3., "Wrong answer"
    assert maxmin([1,2,3,4,5]) == [1,5], "Wrong answer"

if __name__ == "__main__":
    testfunctions()


