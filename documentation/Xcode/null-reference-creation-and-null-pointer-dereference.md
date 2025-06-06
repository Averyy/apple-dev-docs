# Null reference creation and null pointer dereference

**Framework**: Xcode

Detects the creation of null references and null pointer dereferences.

#### Overview

In Xcode 9 and later, you can use this check to detect the creation of null references and null pointer dereferences. Dereferencing a null pointer always results in undefined behavior and can cause crashes. If the compiler finds a pointer dereference, it treats that pointer as nonnull. As a result, the optimizer may remove null equality checks for dereferenced pointers.

##### Creating a Null Reference in C++

The following example demonstrates how to create a null reference. References in C++ must be nonnull:

```occ
int &x = *(int *)nullptr; // Error: null reference
```

###### Solution

Use a pointer instead.

```occ
int *x = nullptr; // Correct
```

##### Member Access Through a Null Pointer in C++

The following code makes a member call on an object with a null address. The compiler may remove the null check on the `this` pointer because it requires the pointer to be `nonnull`.

```occ
struct A {
    int x;
    int getX() {
        if (!this) { // Warning: redundant null check may be removed
            return 0;
        }
        return x; // Warning: 'this' pointer is null, but is dereferenced here
    }
};
A *a = nullptr;
int x = a->getX(); // Error: member access through null pointer
```

> ❗ **Important**: Always avoid null checks on the `this` pointer.

Always avoid null checks on the `this` pointer.

###### Solution

Avoid calling methods on null objects.

## See Also

- [Misaligned pointer](misaligned-pointer.md)
  Detects when code accesses a misaligned pointer or creates a misaligned reference.
- [Invalid Boolean value](invalid-boolean.md)
  Detects when a program accesses a Boolean variable and its value isn’t true or false.
- [Out-of-bounds array access](out-of-bounds-array-access.md)
  Detects out-of-bounds access of arrays.
- [Invalid enumeration value](invalid-enumeration-value.md)
  Detects when an enumeration variable has an invalid value.
- [Reaching of unreachable point](reaching-of-unreachable-point.md)
  Detects when a program reaches an unreachable point.
- [Dynamic type violation](dynamic-type-violation.md)
  Detects when an object has the wrong dynamic type.
- [Invalid float cast](invalid-float-cast.md)
  Detects out-of-range casts to, from, or between floating-point types.
- [Division by zero](division-by-zero.md)
  Detects division where the divisor is zero.
- [Nonnull argument violation](nonnull-argument-violation.md)
  Detects when an argument incorrectly receives a null value.
- [Nonnull return value violation](nonnull-return-value-violation.md)
  Detects when a function incorrectly returns null.
- [Nonnull variable assignment violation](nonnull-variable-assignment-violation.md)
  Detects when you incorrectly assign null to a variable.
- [Invalid object size](invalid-object-size.md)
  Detects invalid pointer casts due to differences in the sizes of types.
- [Invalid shift](invalid-shift.md)
  Detects invalid and overflowing shifts.
- [Integer overflow](integer-overflow.md)
  Detects overflow in arithmetic.
- [Invalid variable-length array](invalid-variable-length-array.md)
  Detects negative array bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/null-reference-creation-and-null-pointer-dereference)*