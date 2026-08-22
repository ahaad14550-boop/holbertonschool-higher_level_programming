# Python - Everything is object
## Task 1 - Where are you?

- `id()` returns the unique identifier of an object.
- In CPython, this identifier represents the object's memory address.
## Task 2 - Right count

- Two variables can point to different objects even if both are integers.
- Here, `a = 89` and `b = 100`, so they do not point to the same object.
## Task 3 - Right count =

- In CPython, small integers are cached and reused.
- Since both `a` and `b` are assigned the value `89`, they point to the same object.
## Task 4 - Right count =

- `b = a` makes `b` reference the same object as `a`.
- Assignment does not create a new copy of the object.
## Task 5 - Right count =+

- `b = a + 1` creates a result with a different value.
- `a` points to `89`, while `b` points to `90`, so they do not reference the same object.

## Task 6 - Is equal

- `==` checks whether two objects have the same value.
- Here, `s1` and `s2` contain the same string, so `s1 == s2` is `True`.
## Task 7 - Is the same

- `is` checks whether two variables reference the exact same object.
- Since `s2 = s1`, both variables point to the same object, so the result is `True`.
## Task 8 - Is really equal

- `==` compares values, not object identity.
- Both strings have the same value, so the result is `True`.
## Task 9 - Is really the same

- `is` checks object identity, not value equality.
- `s1` and `s2` have the same value, but they are not the same object in this example.
- Use `==` when comparing string values, not `is`.
## Task 10 - And with a list, is it equal

- `==` compares the contents of lists.
- Both lists contain the same elements in the same order, so the result is `True`.
## Task 11 - And with a list, is it the same

- `is` checks whether two variables reference the exact same object.
- `l1` and `l2` have the same contents, but they are two different list objects.
- Therefore, `l1 is l2` is `False`.
## Task 12 - And with a list, is it really equal

- `l2 = l1` makes both variables reference the same list.
- Since `==` compares list contents, `l1 == l2` is `True`.
## Task 13 - And with a list, is it really the same

- `l2 = l1` makes both variables reference the exact same list object.
- `is` checks object identity, so `l1 is l2` is `True`.
## Task 14 - List append

- Lists are mutable objects.
- `l2 = l1` makes both variables reference the same list.
- `append()` modifies that same list in place.
- Therefore, changing `l1` also changes what `l2` sees.
## Task 15 - List add

- `l1 + [4]` creates a new list instead of modifying the existing list.
- `l1` is reassigned to the new list `[1, 2, 3, 4]`.
- `l2` still references the original list `[1, 2, 3]`.
- Unlike `append()`, `+` does not mutate the original list.

## Task 16 - Integer incrementation

- Integers are immutable objects.
- `n += 1` creates a new integer object inside the function.
- The original variable `a` is not changed, so `print(a)` outputs `1`.
## Task 17 - List incrementation

- Lists are mutable objects.
- The parameter `n` references the same list object as `l`.
- `append(4)` modifies that list in place.
- Therefore, the original list becomes `[1, 2, 3, 4]`.
## Task 18 - List assignation

- `n = v` only changes what the local variable `n` references inside the function.
- It does not modify the original list object.
- Therefore, `l1` remains `[1, 2, 3]`.
## Task 19 - Copy a list object

- `a_list[:]` creates a shallow copy of the list.
- The new list has the same contents, so `new_list == a_list` is `True`.
- It is a different object, so `new_list is a_list` is `False`.
## Task 20 - Tuple or not?

- `()` creates an empty tuple.
- Therefore, `a` is a tuple.
## Task 21 - Tuple or not?

- `(1, 2)` creates a tuple with two elements.
- Therefore, `a` is a tuple.
## Task 22 - Tuple or not?

- `(1)` is not a tuple; it is just the integer `1` inside parentheses.
- A one-element tuple needs a comma: `(1,)`.
## Task 23 - Tuple or not?

- `(1,)` is a tuple with one element.
- The comma is what makes a one-element tuple.
## Task 24 - Who I am?

- `(1)` is an integer, not a tuple.
- Small integers are reused by CPython.
- Therefore, `a is b` is `True`.
## Task 25 - Tuple or not

- `(1, 2)` creates a tuple.
- `a` and `b` have the same value, but they are different tuple objects.
- Therefore, `a is b` is `False`.
## Task 26 - Empty is not empty

- `()` creates an empty tuple.
- CPython reuses the same empty tuple object.
- Therefore, `a is b` is `True`.
## Task 27 - Still the same?

- `a + [5]` creates a new list object.
- `a` is reassigned to that new list.
- Therefore, the object's `id` changes.
## Task 28 - Same or not?

- For lists, `+=` modifies the existing list in place.
- The list object remains the same, so its `id` does not change.
- Therefore, the answer is `Yes`.