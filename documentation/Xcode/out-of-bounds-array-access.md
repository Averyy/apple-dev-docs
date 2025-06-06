# Out-of-bounds array access

**Framework**: Xcode

Detects out-of-bounds access of arrays.

#### Overview

Use this check to detect attempts to access indexes that exceed the array’s bounds. Out-of-bounds array accesses have undefined behavior, and can result in crashes or incorrect program output. Available in Xcode 9 and later.

> **Note**: This check doesn’t detect out-of-bounds accesses into heap-allocated arrays.

This check doesn’t detect out-of-bounds accesses into heap-allocated arrays.

##### Out of Bounds Array Access in C

In the following example, out-of-bounds access of `array` occurs on the last iteration of the loop:

```occ
int array[5];
for (int i = 0; i <= 5; ++i) {
    array[i] += 1; // Error: out-of-bounds access on the last iteration
}
```

###### Solution

Ensure that accessed indexes don’t exceed the array’s bounds.

## See Also

- [Misaligned pointer](misaligned-pointer.md)
  Detects when code accesses a misaligned pointer or creates a misaligned reference.
- [Invalid Boolean value](invalid-boolean.md)
  Detects when a program accesses a Boolean variable and its value isn’t true or false.
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
- [Null reference creation and null pointer dereference](null-reference-creation-and-null-pointer-dereference.md)
  Detects the creation of null references and null pointer dereferences.
- [Invalid object size](invalid-object-size.md)
  Detects invalid pointer casts due to differences in the sizes of types.
- [Invalid shift](invalid-shift.md)
  Detects invalid and overflowing shifts.
- [Integer overflow](integer-overflow.md)
  Detects overflow in arithmetic.
- [Invalid variable-length array](invalid-variable-length-array.md)
  Detects negative array bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/out-of-bounds-array-access)*