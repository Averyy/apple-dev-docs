# Misaligned pointer

**Framework**: Xcode

Detects when code accesses a misaligned pointer or creates a misaligned reference.

#### Overview

In Xcode 9 and later, you can use this check to detect reads from, or writes to, a misaligned pointer, or when you create a misaligned reference. A pointer misaligns if its address isn’t a multiple of its type’s alignment. Dereferencing a misaligned pointer has undefined behavior, and may result in a crash or degraded performance.

Alignment violations occur frequently in code that serializes or deserializes data. Avoid this issue by using a serialization format that preserves data alignment.

##### Misaligned Integer Pointer Assignment in C

In the following example, the `pointer` variable must have 4-byte alignment, but has only 1-byte alignment:

```occ
int8_t *buffer = malloc(64);
int32_t *pointer = (int32_t *)(buffer + 1);
*pointer = 42; // Error: misaligned integer pointer assignment
```

###### Solution

Use an assignment function like `memcpy`, which can work with unaligned inputs.

```occ
int8_t *buffer = malloc(64);
int32_t value = 42;
memcpy(buffer + 1, &value, sizeof(int32_t)); // Correct
```

> **Note**: The compiler can often safely optimize calls to `memcpy`, even for unaligned arguments.

The compiler can often safely optimize calls to `memcpy`, even for unaligned arguments.

##### Misaligned Structure Pointer Assignment in C

In the following example, the `pointer` variable must have 8-byte alignment, but has only 1-byte alignment:

```swift
struct A {
    int32_t i32;
    int64_t i64;
};
int8_t *buffer = malloc(32);
struct A *pointer = (struct A *)(buffer + 1);
pointer->i32 = 7; // Error: pointer is misaligned
```

###### Solution

One solution is to pack the structure. In the following example, the packed `A` structure prevents the compiler from adding padding between members:

```occ
struct A { ... } __attribute__((packed));
```

> ❗ **Important**: Packing a structure may adversely impact performance.

Packing a structure may adversely impact performance.

## See Also

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
- [Integer overflow](integer-overflow.md)
  Detects overflow in arithmetic.
- [Invalid variable-length array](invalid-variable-length-array.md)
  Detects negative array bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/misaligned-pointer)*