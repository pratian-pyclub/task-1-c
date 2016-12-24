# task-1-c
Solution to https://gist.github.com/swaathi/3356d2d2a1476be21f6938b77d61f82d

This contains the core solution to Task #1C. I've included the solution to only #1C.1 and #1C.2 since #1C.3 is only a repetition on the core logic. 

I want you to pay attention to a few contructs used,

### Using constants to control logic

If there's any strings that are floating around in your codebase, that's immediately a red flag. Strings are dangerous since they can be manipulated and when the string changes, you need to change it at every location. Instead store them in constants that can be used throughout your package. This way you retain a single point of control and it makes change easier.

### Reduce direct dependencies to logic

Your logic should always be flexible to allow change. Though the task says `?` is the wildcard character, that might not be the case in the future. Always remove parts of logic that constraint flexibility. Here the wildcard character reference and corresponding regex is stored as a constant.

### Using preconditions to reduce further processing

Find preconditions that need to be satisfied by the input values to be able proceed into your logic. Here the precondition,

```
if len(self.word) > len(self.tile):
            return False
```

checks if the length of the word is longer than the tile. If so, there is no chance that the word can be formed. This increases the efficiency and decreases computation time. 

Of course if your precondition takes longer than your logic, you're going in the wrong direction!

### Function name conventions

Always try to find function names that automatically relay the purpose of your code. Another programmer should be able to understand your logic just by looking at your function names.
