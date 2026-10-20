# DSPComplex

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

Used to hold a complex value.

**Availability**:
- macOS 10.13+

## Declaration

```c
typedef struct DSPComplex DSPComplex;
```

#### Discussion

Complex data are stored as ordered pairs of floating-point numbers. Because they are stored as ordered pairs, complex vectors require address strides that are multiples of two. 

## Topics

### Fields
- [real](./dspcomplex/api-1579938-real.md)
  The real part of the value.
- [imag](../Accelerate/dspcomplex/imag.md)
  The imaginary part of the value.
### Instance Properties
- [imag](./dspcomplex/api-1579947-imag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dspcomplex)*