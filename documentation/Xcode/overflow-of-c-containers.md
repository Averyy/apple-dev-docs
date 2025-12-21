# Overflow of C++ containers

**Framework**: Xcode

Detects when you access a C++ container outside its bounds.

#### Overview

Use this check to detect when you access a libc++ container beyond the region `[container.begin(), container.end()]`, even when the accessed memory is in a heap-allocated buffer the container uses internally. Available in Xcode 7 and later.

> **Note**: This check is enabled by default. In Xcode versions prior to version 26, it was disabled by default. See [`Disabling Container Overflow Checks`](overflow-of-c-containers#Disabling-Container-Overflow-Checks.md) to disable it.

##### Vector Overflow in C++

In the following example, the `vector` variable has valid indexes in the range `[0,2]`, but the accessed index is `3`, which causes an overflow:

```occ
std::vector<int> vector;
vector.push_back(0);
vector.push_back(1);
vector.push_back(2);
auto *pointer = &vector[0];
return pointer[3]; // Error: out of bounds access for vector
```

###### Solution

Add a bounds check before attempting to access a container at a specific index.

##### Disabling Container Overflow Checks

> **Note**: The [`Enable C++ Container Overflow Checks`](build-settings-reference#Enable-C++-Container-Overflow-Checks.md) build setting no longer has any effect in Xcode 26 onwards.

You may encounter a false-positive ‘Container overflow’ error when code that isn’t compiled with Address Sanitizer modifies a container. For container overflow checks to work correctly, you need to compile all code with Address Sanitizer. If you can’t do this, turn off container overflow checks using one of the following methods:

```occ
#ifdef __cplusplus
extern "C" {
#endif
#include <sanitizer/asan_interface.h>

const char *__asan_default_options() {
    return "detect_container_overflow=0";
}
#ifdef __cplusplus
}
#endif
```

If you set the `detect_container_overflow` option in both the `__asan_default_options` function, and the `ASAN_OPTIONS` environment variable, the system uses the value in the environment variable.

## See Also

- [Use of deallocated memory](use-of-deallocated-memory.md)
  Detects the use of deallocated memory.
- [Deallocation of deallocated memory](deallocation-of-deallocated-memory.md)
  Detects attempts to free deallocated memory.
- [Deallocation of nonallocated memory](deallocation-of-nonallocated-memory.md)
  Detects attempts to free nonallocated memory.
- [Use of stack memory after function return](use-of-stack-memory-after-function-return.md)
  Detects when you access stack variable memory after its declaring function returns.
- [Use of out-of-scope stack memory](use-of-out-of-scope-stack-memory.md)
  Detects access to variables outside of their declared scope.
- [Overflow and underflow of buffers](overflow-and-underflow-of-buffers.md)
  Detects when you access memory outside of a buffer’s boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/overflow-of-c-containers)*