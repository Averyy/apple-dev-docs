# Invalid shift

**Framework**: Xcode

Detects invalid and overflowing shifts.

#### Overview

Use this check to detect bitwise shifts with invalid shift amounts and shifts that might overflow. These shifts have undefined behavior and the optimizer may omit them. Available in Xcode 9 and later.

##### Invalid Shift Amount in C

The following code shows a shift with an invalid shift amount because the destination type can’t represent the result:

```occ
int32_t x = 1;
x <<= 32; // Error: (1 << 32) can't be represented in an int32_t
```

If the optimizer can prove that a shift amount may be invalid, it may replace the result of the shift with an arbitrary value.

###### Solution

Use a larger destination type, such as an `int64_t`.

##### Shift Overflow in C

In the following code, the second shift overflows `x` because `int32_t` can’t represent `((1U << 31) - 1) << 2`:

```occ
int32_t x = (1U << 31) - 1;
x <<= 2; // Error: the shift result can't fit in x
```

###### Solution

Use a larger destination type, such as an `int64_t`.

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
- [Null reference creation and null pointer dereference](null-reference-creation-and-null-pointer-dereference.md)
  Detects the creation of null references and null pointer dereferences.
- [Invalid object size](invalid-object-size.md)
  Detects invalid pointer casts due to differences in the sizes of types.
- [Integer overflow](integer-overflow.md)
  Detects overflow in arithmetic.
- [Invalid variable-length array](invalid-variable-length-array.md)
  Detects negative array bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/invalid-shift)*