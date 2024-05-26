import random  # O(1) - Importing the random module for generating random numbers.

class Node:
    def __init__(self, Data):  
        self.Data = Data  # O(1) - Assigns the data value to the node.
        self.Left = None  # O(1) - Initializes the left child node as None.
        self.Right = None  # O(1) - Initializes the right child node as None.

def CreateTopDownBSTInput(sorted_input, L, R):
    if L > R:  # O(1) - Checks if left index is greater than right index.
        return None  # O(1) - Returns None if left index is greater than right index.
    mid = (L + R) // 2  # O(1) - Calculates the index of the midpoint.
    root = Node(sorted_input[mid])  # O(1) - Creates a new node with the value at the midpoint.
    root.Left = CreateTopDownBSTInput(sorted_input, L, mid - 1)  # Recursion - O(log(n))
    root.Right = CreateTopDownBSTInput(sorted_input, mid + 1, R)  # Recursion - O(log(n))
    return root  # O(1) - Returns the root node of the BST.

def DisplayBST(Node, element="element", left="left", right="right"):
    def Display(root, element=element, left=left, right=right):
        if getattr(root, 'Right') is None and getattr(root, 'Left') is None:  # O(1) - Checks if the node has no children.
            line = '%s' % root.Data  # O(1) - Converts the node's data to string.
            width = len(line)  # O(1) - Calculates the width of the node's data.
            height = 1  # O(1) - Height of the node.
            middle = width // 2  # O(1) - Calculates the middle position of the node.
            return [line], width, height, middle  # O(1)

        if getattr(root, 'Right') is None:  # O(1) - Checks if the node has no right child.
            lines, n, p, x = Display(getattr(root, 'Left'))  # Recursion - O(n)
            s = '%s' % root.Data  # O(1) - Converts the node's data to string.
            u = len(s)  # O(1) - Length of the node's data.
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s  # O(n) - Constructs the first line of the node.
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '  # O(n) - Constructs the second line of the node.
            shifted_lines = [line + u * ' ' for line in lines]  # O(n) - Shifts the lines for left child.
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  # O(n)

        if getattr(root, 'Left') is None:  # O(1) - Checks if the node has no left child.
            lines, n, p, x = Display(getattr(root, 'Right'))  # Recursion - O(n)
            s = '%s' % root.Data  # O(1) - Converts the node's data to string.
            u = len(s)  # O(1) - Length of the node's data.
            first_line = s + x * '_' + (n - x) * ' '  # O(n) - Constructs the first line of the node.
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '  # O(n) - Constructs the second line of the node.
            shifted_lines = [u * ' ' + line for line in lines]  # O(n) - Shifts the lines for right child.
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2  # O(n)

        left, n, p, x = Display(getattr(root, 'Left'))  # Recursion - O(n)
        right, m, q, y = Display(getattr(root, 'Right'))  # Recursion - O(n)
        s = '%s' % root.Data  # O(1) - Converts the node's data to string.
        u = len(s)  # O(1) - Length of the node's data.
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '  # O(n) - Constructs the first line of the node.
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '  # O(n) - Constructs the second line of the node.
        if p < q:
            left += [n * ' '] * (q - p)  # O(n) - Adjusts the height for left child.
        elif q < p:
            right += [m * ' '] * (p - q)  # O(n) - Adjusts the height for right child.
        zipped_lines = zip(left, right)  # O(min(n, m))
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]  # O(n) - Combines the lines of left and right children.
        return lines, n + m + u, max(p, q) + 2, n + u // 2  # O(n) - Returns the combined lines and height of the node.

    lines = []  # O(1) - Initialize lines.
    if Node is not None:  # O(1) - Checks if the root node is not None.
        lines, *_ = Display(Node, element, left, right)  # O(n) - Calls the Display function.
    print("\t== Binary Tree: shape ==")  # O(1) - Prints the heading.
    print()  # O(1) - Prints a blank line.
    if lines == []:  # O(1) - Checks if there are no lines.
        print("\t  No tree found")  # O(1) - Prints no tree found message.
    for line in lines:  # O(n) - Iterates over each line.
        print("\t", line)  # O(1) - Prints each line.
    print()  # O(1) - Prints a blank line.

def CountingSort(Data):
    UnsortedArray = Data  # O(1) - Assigns the input array to UnsortedArray.
    FinalArray = [0] * len(UnsortedArray)  # O(n) - Creates an array of zeros with the same length as UnsortedArray.

    max_element = max(UnsortedArray)  # O(n) - Finds the maximum element in UnsortedArray.
    min_element = min(UnsortedArray)  # O(n) - Finds the minimum element in UnsortedArray.

    range_of_numbers = max_element - min_element + 1  # O(1) - Calculates the range of numbers in UnsortedArray.

    count = [0] * range_of_numbers  # O(n) - Creates a count array initialized with zeros.

    for num in UnsortedArray:  # O(n) - Iterates through UnsortedArray.
        count[num - min_element] += 1  # O(1) - Increments the count of the corresponding element in the count array.

    for i in range(1, len(count)):  # O(n) - Iterates through the count array.
        count[i] += count[i - 1]  # O(1) - Updates each element of the count array with cumulative counts.

    for num in reversed(UnsortedArray):  # O(n) - Iterates through UnsortedArray in reverse.
        FinalArray[count[num - min_element] - 1] = num  # O(1) - Places each element in its correct position in the sorted array.
        count[num - min_element] -= 1  # O(1) - Decrements the count of the corresponding element in the count array.

    return FinalArray  # O(n) - Returns the sorted array.

def GetBSTData(root):
    # O(n) - n is the number of nodes in the BST
    data = []  # Initialize an empty list to store data
    if root:
        # O(n) - Recursive calls can potentially visit all nodes in the BST
        # If root is not None, add its data to the list
        data.append(root.Data)
        # Recursively collect data from left and right subtrees
        data.extend(GetBSTData(root.Left))  # Recursion - O(n)
        data.extend(GetBSTData(root.Right))  # Recursion - O(n)
    return data

#Test 1
#Input = [45, -8, 21, 34, 55, 65, 9, 14, 0, 18, 90, 46, 49, 82, 84, 99, 80, 132, 57, 66]  # O(1) - Initializes an input array.
#Input = [58, 84, 68, 23, 38, 82, 26, 17, 24, 106, 95, 48, 88, 54, 50, 51, 53, 49, -6, -46]
Input = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]

print("--------------------------------")  # O(1) - Prints the spacer.
print("Original Data Sequence:")  # O(1) - Prints the heading.
print(Input)  # O(1) - Prints the input array.

print("\nRe-arranged Data Items:")  # O(1) - Prints the heading.
sorted_input = CountingSort(Input)  # O(n*log(n)) - Sorts the input array.
print(sorted_input)  # O(n) - Prints the sorted array.

print("\nBST Input Data:") # O(1) - Prints the heading.
Root = CreateTopDownBSTInput(sorted_input, 0, len(sorted_input) - 1)  # O(log(n)) - Creates a balanced BST.
print(GetBSTData(Root))

print("\nBST Tree Shape:")  # O(1) - Prints the heading.
print("\n")
DisplayBST(Root)  # O(n) - Displays the shape of the binary tree.

#Test 2
NewInput = []  # O(1) - Initializes an empty list for new input.

for Count in range(1, 50):  # O(1) - Loops 50 times.
    NewInput.append(random.randint(0, 100))  # O(1) - Appends a random integer to the new input list.

print("--------------------------------")  # O(1) - Prints the spacer.
print("Original Data Sequence:")  # O(1) - Prints the heading.
print(NewInput)  # O(1) - Prints the new input array.

print("\nRe-arranged Data Items:")  # O(1) - Prints the heading.
sorted_input_new = CountingSort(NewInput)  # O(n*log(n)) - Sorts the new input array.
print(sorted_input_new)  # O(n) - Prints the sorted new input array.

print("\nBST Input Data:") # O(1) - Prints the heading.
Root_new = CreateTopDownBSTInput(sorted_input_new, 0, len(sorted_input_new) - 1)  # O(log(n)) - Creates a balanced BST for the new input.
print(GetBSTData(Root_new))

print("\nBST Tree Shape:")  # O(1) - Prints the heading.
print("\n")
DisplayBST(Root_new)  # O(n) - Displays the shape of the binary tree for the new input.

print("--------------------------------")  # O(1) - Prints the spacer.
