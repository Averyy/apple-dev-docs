# Invalid enumeration value

**Framework**: Xcode

Detects when an enumeration variable has an invalid value.

#### Overview

In Xcode 9 and later, you can use this check to detect accesses of an enumeration variable when its value isn’t within the valid range for the type. This can occur for uninitialized enumeration values, or when using an integer as an enumeration value without an appropriate cast. The use of out-of-range enumeration values has undefined behavior, and may indicate the existence of logic errors in a program.

##### Invalid Enumeration Variable Access in C++

In the following example, the cast to the `E` type is invalid because `2` isn’t within the enumeration’s range:

```occ
enum E {
    a = 1
};
int value = 2;
enum E *e = (enum E *)&value;
return *e; // Error: 2 is out of the valid range for E
```

###### Solution

Ensure that enumeration variables only use values within their defined ranges.

## See Also

- [Misaligned pointer](misaligned-pointer.md)
  Detects when code accesses a misaligned pointer or creates a misaligned reference.
- [Invalid Boolean value](invalid-boolean.md)
  Detects when a program accesses a Boolean variable and its value isn’t true or false.
- [Out-of-bounds array access](out-of-bounds-array-access.md)
  Detects out-of-bounds access of arrays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/invalid-enumeration-value)*