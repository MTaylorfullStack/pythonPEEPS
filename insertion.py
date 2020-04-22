# sort values from lowest to highest
    # as we move through the list (forward)
        # compare current value with all values before
            # if current value < value before
                # swap values
            # else
                # done with sort

def insertion(some):
    for i in range(len(some)):
        print(f'current value sorting {some[i]}')
        print(f'current state of some: {some}')
        for j in range(i, -1, -1):
            if some[i] < some[j]:
                temp = some[i]
                some[i] = some[j]
                some[j] = temp
                i -= 1
                print(f'some after swap: {some}')
    return some

print(insertion([3,5,6,2,1,9,8]))

# printed all values from a list




x =[ [5,2,3], [10,8,9] ]

y = [2,3,4,5,6]

print(y)
y[0] = 15
print(y)

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

