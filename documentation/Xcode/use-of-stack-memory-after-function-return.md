# Use of stack memory after function return

**Framework**: Xcode

Detects when you access stack variable memory after its declaring function returns.

#### Overview

Use this check to detect access to a stack variable that a function declares after that function returns. Attempting to access stack memory in this manner can lead to crashes, or result in unpredictable behavior. Available in Xcode 9 and later.

> **Note**: This check is in a disabled state by default. You can enable it under the Address Sanitizer option in the Edit Scheme dialogue.

##### Use of Stack Memory After Return in C

In the following example, the `integer_pointer_returning_function` function returns a pointer to a stack variable, and there’s an attempt to access the memory of the returned pointer:

```occ
int *integer_pointer_returning_function() {
    int value = 42;
    return &value;
}

int *integer_pointer = integer_returning_function();
*integer_pointer = 43; // Error: invalid access of returned stack memory
```

###### Solution

Use pointer arguments to allow a function to return values by reference.

## See Also

- [Use of deallocated memory](use-of-deallocated-memory.md)
  Detects the use of deallocated memory.
- [Deallocation of deallocated memory](deallocation-of-deallocated-memory.md)
  Detects attempts to free deallocated memory.
- [Deallocation of nonallocated memory](deallocation-of-nonallocated-memory.md)
  Detects attempts to free nonallocated memory.
- [Use of out-of-scope stack memory](use-of-out-of-scope-stack-memory.md)
  Detects access to variables outside of their declared scope.
- [Overflow and underflow of buffers](overflow-and-underflow-of-buffers.md)
  Detects when you access memory outside of a buffer’s boundaries.
- [Overflow of C++ containers](overflow-of-c-containers.md)
  Detects when you access a C++ container outside its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/use-of-stack-memory-after-function-return)*