def remove_duplicate_element(word):
    # Function to remove duplicate characters
    unq_list = []

    for i in word:
        if i not in unq_list:
            unq_list.append(i)

    return ''.join(unq_list)


def merge_the_tools(string, k):
    n = len(string)  # get the length of the string
    cut = n / k  # number of slices the string needs to be cut into
    nop = n / cut
    '''
    Defines the length of each slice,
    length of each part = length of string / number of parts
    '''
    l = []
    for i in range(int(cut)):  # loop that cuts the string into parts
        # Variable stores the slice of the string
        slice = string[i * int(nop): i * int(nop) + int(nop)]
        l.append(slice)

    n = 0
    for i in range(len(l)):
        print(remove_duplicate_element(l[i]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
