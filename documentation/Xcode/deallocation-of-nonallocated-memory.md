# Deallocation of nonallocated memory

**Framework**: Xcode

Detects attempts to free nonallocated memory.

#### Overview

Use this check to detect when you call `free` on memory that you don’t allocate using `malloc`. Attempting to deallocate nonallocated memory can result in a crash. Available in Xcode 7 and later.

##### Deallocation of a Stack Variable in C

In the following example, the `value` variable allocates on the stack, and deallocates when the function exits, so calling `free` on it is incorrect:

```occ
int value = 42;
free(&value); // Error: free called on stack allocated variable
```

###### Solution

Don’t call the `free` function on variables that you allocate on the stack.

## See Also

- [Use of deallocated memory](use-of-deallocated-memory.md)
  Detects the use of deallocated memory.
- [Deallocation of deallocated memory](deallocation-of-deallocated-memory.md)
  Detects attempts to free deallocated memory.
- [Use of stack memory after function return](use-of-stack-memory-after-function-return.md)
  Detects when you access stack variable memory after its declaring function returns.
- [Use of out-of-scope stack memory](use-of-out-of-scope-stack-memory.md)
  Detects access to variables outside of their declared scope.
- [Overflow and underflow of buffers](overflow-and-underflow-of-buffers.md)
  Detects when you access memory outside of a buffer’s boundaries.
- [Overflow of C++ containers](overflow-of-c-containers.md)
  Detects when you access a C++ container outside its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/deallocation-of-nonallocated-memory)*