import array

arr = array.array('i', [17, 12, 3, 6])
value = 17
isFound = False
result = list()

for i in arr:
    if i in result:
        isFound = True
        print("True")
    result.append(value - i)
if ~isFound:
    print("False")