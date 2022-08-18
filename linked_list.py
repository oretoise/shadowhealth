import random
import time


class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None


def remove(head, data, all=False):
    """
    Remove one or all instances of a node from the linked list.

    Parameters
    ----------
        head : Node object
            Head of the linked list.
        data : int
            Value of the node to be removed.
        all : boolean
            Whether to remove all instances or just the first one found. Defaults to just the first instance.
    """
    
    # Start looking at the head.
    current = head

    # Walk the linked list, looking for nodes that match the given value for data.
    while current.next is not None:

        # If we have a match, 
        if current.data == data:
            
            # Move the next node's data up to the current node.
            current.data = current.next.data

            # Skip over the next node, as we just moved it up.
            current.next = current.next.next

            # If only the first instance, quit.
            if not all:
                return
        
        # If we had a match, moving up the next node means incrementing the loop variable is redundant.
        # So, if it's not a match, move forward.
        else:
            current = current.next


def insertionSort(head):
    """ Sort the list using Insertion Sort. """
    
    # Get the current head.
    current = head
    index = None
    
    # If the list is empty, quit.
    if not head:
        return

    # Otherwise, loop through the list.
    else:
        while current:
            # Look at the node next to the current node.
            index = current.next
            
            # For each node from index to the end of the list, swap nodes if it's bigger.
            while index:
                if current.data > index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                
                # Set index to the next node.
                index = index.next
            
            # If we're done looking from index to the end of the list and swapping, move on.
            current = current.next


def sortedMerge(a, b):
    """ Merge two halves of a list provided by mergeSort. """

    # Start building a new linked list of sorted nodes.
    result = None

    # If either list is empty, return the other.
    if not a:
        return b
    elif not b:
        return a
    
    # Choose A or B.
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    
    return result    


def mergeSort(head):
    """ Sort a linked list using MergeSort. """

    # If there are no nodes or one node, return the given head.
    if not head or not head.next:
        return head

    # Retrieve the middle node of the list and the one next to it.
    middle = getMiddle(head)
    middleNext = middle.next

    # Split the linked list into two.
    middle.next = None

    # Recursively call mergeSort on each side of the list.
    left = mergeSort(head)
    right = mergeSort(middleNext)

    return sortedMerge(left, right)


def getMiddle(head):
    """
    Return a pointer to the middle of a linked list using a Tortoise & Hare approach.
    
    Parameters
    ----------
        head : Node
            Head of the linked list.
    """

    # If the list is empty, quit.
    if head == None:
        return None
    
    # Slow will go forward one node at a time. Fast will go two at a time.
    slow = head
    fast = head

    # Traverse the list until fast runs out of nodes. Slow will therefore contain the middle point.
    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    
    return slow


def add(head, data):
    """
    Add a node to the end of the linked list.

    Parameters
    ----------
        data : int
            Value of the node object
    """

    # Create a new node using the provided data.
    new = Node(data)
    
    # Set the node's next link to the new node.
    head.next = new


def printList(head):
    """
    Print out the list, traversing it node by node.
    """

    # If the list is empty, say so.
    if not head:
        print("No nodes in list.")
        return
    
    current = head

    # Initalize an empty list.
    nodes = []

    # Fill the list with each node's value.
    while(current):
        
        # Append the current node's data to the list.
        nodes.append(current.data)

        # Go to the next node.
        current = current.next
    
    # Display the list representation.
    print(nodes)


if __name__ == "__main__":

    # List to hold some numbers.
    randoms = []

    # Generate random numbers to sort.
    for i in range(50):
        randoms.append(random.randint(0, 50))
    
    # Create a new linked list.
    linkedList = Node(randoms[0])
    
    # Add each random number as a Node in the linked list, building up the linked list.
    current = linkedList
    for number in randoms[1:]:
        add(current, number)
        current = current.next
        
    # Show the original list.
    print("Original:")
    printList(linkedList)

    # For fun, time the sorting call.
    tic = time.perf_counter()
    
    # Sort the list using MergeSort.
    mergeList = mergeSort(linkedList)

    # End the time call and print the delta.
    toc = time.perf_counter()

    print(f"Sorted the linked list using MergeSort in {toc - tic:0.5f} seconds")
    
    # Show the sorted list.
    print("Sorted (MergeSort):")
    printList(mergeList)
    
    print("Rebuilding initial linked list...")
    linkedList = Node(randoms[0])
    
    # Add each random number as a Node in the linked list, building up the linked list.
    current = linkedList
    for number in randoms:
        add(current, number)
        current = current.next

    # For fun, time the sorting call.
    tic = time.perf_counter()
    
    # Sort the list using MergeSort.
    insertionSort(linkedList)

    # End the time call and print the delta.
    toc = time.perf_counter()

    print(f"Sorted the linked list using InsertionSort in {toc - tic:0.5f} seconds")
    
    # Show the sorted list.
    print("Sorted:")
    printList(linkedList)

    # Delete the first Node in the randoms list.
    print("Removing first instance of", randoms[0])
    remove(linkedList, randoms[0])

    # Show the modified list.
    print("Modified:")
    printList(linkedList)

    # Delete the first Node in the randoms list.
    print("Removing all instances of", randoms[1])
    remove(linkedList, randoms[1], True)

    # Show the modified list.
    print("Modified:")
    printList(linkedList)