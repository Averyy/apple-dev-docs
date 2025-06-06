# Invalid Boolean value

**Framework**: Xcode

Detects when a program accesses a Boolean variable and its value isn’t true or false.

#### Overview

Use this check to detect accesses to a Boolean variable when its value isn’t true or false. This problem can occur when using an integer or pointer without an appropriate cast. The use of out-of-range Boolean values has undefined behavior, which can be difficult to debug. Available in Xcode 9 and later.

##### Invalid Boolean Variable Access in C

The intent of the following code is to call the `success` function when `result` is nonzero. However, because it uses a Boolean check, the compiler may, as an optimization, only emit instructions that check the least-significant bit of `predicate`, which is `0`, causing a logic error.

```occ
int result = 2;
bool *predicate = (bool *)&result;
if (*predicate) { // Error: variable is not a valid Boolean
    success();
}
```

###### Solution

Use integer comparison instead of a Boolean check.

```occ
int result = 2;
if (result != 0) { // Correct
  success();
}
```

## See Also

- [Misaligned pointer](misaligned-pointer.md)
  Detects when code accesses a misaligned pointer or creates a misaligned reference.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/invalid-boolean)*