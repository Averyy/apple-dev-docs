# Nonnull variable assignment violation

**Framework**: Xcode

Detects when you incorrectly assign null to a variable.

#### Overview

Use this check to detect when you assign `null` to a variable with the `_Nonnull` annotation. Available in Xcode 9 and later.

> **Note**: The nonnull violation check for variable assignment is off by default. You can turn it on by enabling the `-fsanitize=nullability-assign` compiler flag.

##### Violation of Nonnull Annotation with Variable Assignment in C

In the following example, the call to `assigns_a_value` breaks the `_Nonnull` annotation of the variable `q`:

```occ
void assigns_a_value(int *p) {     
    int *_Nonnull q = p; // Warning: null can be assigned
}
assigns_a_value(NULL); // Error: _Nonnull variable violation
```

###### Solution

Correct logic errors, or remove the `_Nonnull` annotation.

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

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/nonnull-variable-assignment-violation)*