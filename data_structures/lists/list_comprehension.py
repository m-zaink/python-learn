# [______ for ______ in 'iterable']

answer = [name[0] for name in ['Elie', 'Tim', 'Matt']]
answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

answer = [i for i in [1, 2, 3, 4] if i in [3, 4, 5, 6]] # Intersection of the two lists.
answer2 = [name[::-1].lower() for name in ['Elie', 'Tim', 'Matt']]  # No reverse() method so manually reversing.

answer = [i for i in range(1, 101) if i % 12 == 0]

answer = [i for i in 'amazing' if i not in list('aeiou')]

answer = [print(val) for val in [1, 2, 3, 4]]
print(answer)

answer = [[i for i in range(3)] for  j in range(3)]

answer = [[i for i in range(10)] for j in range(10)]