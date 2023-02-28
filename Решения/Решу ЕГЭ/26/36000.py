def bin_search(element, array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == element:
        return mid
    if array[mid] > element:
        return bin_search(element, array, start, mid - 1)
    if array[mid] < element:
        return bin_search(element, array, mid + 1, end)

f = open('files/36000.txt')
N = int(f.readline())
data = []
for line in f:
    data.append(int(line))
data.sort()
counter = 0
maximum = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] % 2 != data[j] % 2 and bin_search(data[i] + data[j], data, j + 1, N - 1) != -1:
            counter += 1
            maximum = max(data[i] + data[j], maximum)
print(counter, maximum)