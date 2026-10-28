# DSPDoubleComplex

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

Used to hold a double-precision complex value.

**Availability**:
- macOS 10.13+

## Declaration

```c
typedef struct DSPDoubleComplex DSPDoubleComplex;
```

## Discussion

Double complex data are stored as ordered pairs of double-precision floating-point numbers. Because they are stored as ordered pairs, complex vectors require address strides that are multiples of two.

## Topics

### Fields
- [real](./dspdoublecomplex/api-1579982-real.md)
  The real part of the value.
- [imag](../Accelerate/dspdoublecomplex/imag.md)
  The imaginary part of the value.
### Instance Properties
- [imag](./dspdoublecomplex/api-1579996-imag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dspdoublecomplex)*