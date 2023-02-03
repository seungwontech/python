while True:
    value = input()
    stack1 = []
    if value == '.':
        break
    for i in value:

        if i == '[' or i == '(':
            stack1.append(i)
        elif i == ']':
            if len(stack1) != 0 and stack1[-1] == '[':
                stack1.pop()
            else:
                stack1.append(i)
                break

        elif i == ')':
            if len(stack1) != 0 and stack1[-1] == '(':
                stack1.pop()
            else:
                stack1.append(i)
                break
    if len(stack1) == 0:
        print('yes')
    else:
        print('no')


# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .