# Dynamic type violation

**Framework**: Xcode

Detects when an object has the wrong dynamic type.

#### Overview

Use this check to detect when an object has the wrong dynamic type. Dynamic type violations can cause unintended code execution. Available in Xcode 9 and later.

##### Member Call on Instance with Incorrect Type in C++

In the following code, `reinterpret_cast` creates a variable with the wrong dynamic type:

```occ
struct Animal {
    virtual const char *speak() = 0;
};
struct Cat : public Animal {
    const char *speak() override {
        return "meow";
    }
};
struct Dog : public Animal {
    const char *speak() override {
      return "woof";
    }
};
auto *dog = reinterpret_cast<Dog *>(new Cat); // Error: dog has incorrect dynamic type
dog->speak(); // Error: this call has undefined behavior
```

The method call `dog->speak()` is suspect. If the `speak` method in `Dog` is `final override`, `dog->speak()` may return `"woof"` because the optimizer can devirtualize the call; if not, it might return `"meow"`.

> **Note**: This UBSan check requires runtime type information, and is incompatible with the `-fno-rtti` compiler flag.

This UBSan check requires runtime type information, and is incompatible with the `-fno-rtti` compiler flag.

###### Solution

Use `reinterpret_cast` sparingly, and only when it’s possible to verify that the cast object is an instance of the destination type.

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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/dynamic-type-violation)*