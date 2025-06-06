# Invalid object size

**Framework**: Xcode

Detects invalid pointer casts due to differences in the sizes of types.

#### Overview

Use this check to detect pointer casts when the size of the source type is less than the size of the destination type. Using the result of such a cast to access out-of-bounds data has undefined behavior. Available in Xcode 9 and later.

##### Downcast From Type with Insufficient Space in C++

In the following example, the cast from `Base *` to `Derived *` is suspect because `Base` isn’t large enough to contain an instance of `Derived`:

```occ
struct Base {
    int pad1;
};
struct Derived : Base {
    int pad2;
};
Derived *getDerived() {
    return static_cast<Derived *>(new Base); // Error: invalid downcast
}
```

The optimizer may remove an expression, such as `getDerived()->pad2`, because `getDerived()` returns a pointer to an object that isn’t large enough to contain a `pad2` field.

> **Note**: This UBSan check may not trigger at low optimization levels.

This UBSan check may not trigger at low optimization levels.

###### Solution

One way to fix this issue is to avoid the downcast, such as by using instances of the `Derived` object wherever you need them.

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
- [Invalid shift](invalid-shift.md)
  Detects invalid and overflowing shifts.
- [Integer overflow](integer-overflow.md)
  Detects overflow in arithmetic.
- [Invalid variable-length array](invalid-variable-length-array.md)
  Detects negative array bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/invalid-object-size)*