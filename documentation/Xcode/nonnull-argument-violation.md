# Nonnull argument violation

**Framework**: Xcode

Detects when an argument incorrectly receives a null value.

#### Overview

Use this check to detect when a function that has an argument with the `nonnull` attribute or the `_Nonnull` annotation receives a null value. Available in Xcode 9 and later.

> **Note**: The nonnull violation check for arguments with the `_Nonnull` annotation is off by default. You can turn it on by enabling the `-fsanitize=nullability-arg` compiler flag.

The nonnull violation check for arguments with the `_Nonnull` annotation is off by default. You can turn it on by enabling the `-fsanitize=nullability-arg` compiler flag.

##### Violation of the Nonnull Parameter Attribute in C

In the following example, the call to the `has_nonnull_argument` function breaks the `nonnull` attribute of the parameter `p`:

```occ
void has_nonnull_argument(__attribute__((nonnull)) int *p) { 
     // ... 
}
has_nonnull_argument(NULL); // Error: nonnull parameter attribute violation
```

###### Solution

Correct logic errors, or remove the `nonnull` attribute and rework the called function’s logic accordingly.

##### Violation of the Nonnull Annotation for an Argument in C

In the following example, the call to the `has_nonnull_argument` function breaks the `_Nonnull` annotation of the parameter `p`:

```occ
void has_nonnull_argument(int * _Nonnull p) { 
     // ... 
}
has_nonnull_argument(NULL); // Error: _Nonnull annotation violation
```

###### Solution

Correct logic errors, or remove the `_Nonnull` attribute and rework the called function’s logic accordingly.

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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/nonnull-argument-violation)*