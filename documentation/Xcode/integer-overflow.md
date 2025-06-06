# Integer overflow

**Framework**: Xcode

Detects overflow in arithmetic.

#### Overview

Overflows result in undefined behavior. Use this check to detect overflows in addition, subtraction, multiplication, and division. Available in Xcode 9 and later.

##### Signed Addition Overflow in C

In the following code, the `x` variable has the maximum `int32_t` value before the addition, and the result of the addition overflows `x`, which the optimizer may not handle in a predictable way:

```occ
int32_t x = (1U << 31) - 1;
x += 1; // Error: the add result can't fit in x
```

> **Note**: With the exception of the signed division check, enabling the `-fwrapv` compiler flag disables UBSan overflow checks.

With the exception of the signed division check, enabling the `-fwrapv` compiler flag disables UBSan overflow checks.

###### Solution

One way to address signed overflow is to use larger types.

If you don’t need to represent negative numbers, another option is to use unsigned types, which wrap on arithmetic overflow. Alternatively, pass the `-fwrapv` flag to the compiler to enable signed wraparound on overflow. However, this may adversely impact performance.

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
- [Invalid shift](invalid-shift.md)
  Detects invalid and overflowing shifts.
- [Invalid variable-length array](invalid-variable-length-array.md)
  Detects negative array bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/integer-overflow)*