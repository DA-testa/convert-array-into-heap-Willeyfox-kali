# python3


def build_heap(data):
    swaps = []
    size = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(size - 1, -1, -1):
        while 2 * i + 1 < size:
            j = 2 * i + 1
            if j + 1 < size and data[j+1] < data[j]:
                J = j + 1
            if data[i] < data[j]:
                break
            swaps.append((i, j))
            data[i], data[j] = data[j], data[i]
            i = j
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    n = input().strip()
    # input from keyboard
    if n == 'I':
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    # checks if lenght of data is the same as the said lenght
    

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
