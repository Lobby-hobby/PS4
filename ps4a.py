# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    if len(sequence)<=1:
        return [sequence]
    else:
        a = sequence[0]
        sequence = sequence[1:]
        l = []
        for le in get_permutations(sequence):
            for i in range(len(le)+1):
                l.append(le[:i]+a+le[i:])
        return l
print(get_permutations('abcd'))


