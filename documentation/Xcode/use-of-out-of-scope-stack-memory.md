# Use of out-of-scope stack memory

**Framework**: Xcode

Detects access to variables outside of their declared scope.

#### Overview

Use this check to detect when you access a variable outside of its scope. Attempting to access out-of-scope memory can result in unpredictable behavior. Available in Xcode 9 and later.

##### Use of Out of Scope Stack Memory in C

In the following example, the code conditionally assigns the `pointer` variable to the return value of the `integer_returning_function` function, which it then accesses out of its declaration scope:

```occ
int *pointer = NULL;
if (bool_returning_function()) {
    int value = integer_returning_function();
    pointer = &value;
}
*pointer = 42; // Error: invalid access of stack memory out of declaration scope
```

###### Solution

Ensure you don’t access variables outside of their declared scope, or allocate memory using the `malloc` function.

## See Also

- [Use of deallocated memory](use-of-deallocated-memory.md)
  Detects the use of deallocated memory.
- [Deallocation of deallocated memory](deallocation-of-deallocated-memory.md)
  Detects attempts to free deallocated memory.
- [Deallocation of nonallocated memory](deallocation-of-nonallocated-memory.md)
  Detects attempts to free nonallocated memory.
- [Use of stack memory after function return](use-of-stack-memory-after-function-return.md)
  Detects when you access stack variable memory after its declaring function returns.
- [Overflow and underflow of buffers](overflow-and-underflow-of-buffers.md)
  Detects when you access memory outside of a buffer’s boundaries.
- [Overflow of C++ containers](overflow-of-c-containers.md)
  Detects when you access a C++ container outside its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/use-of-out-of-scope-stack-memory)*