# DSPComplex

**Framework**: Kernel  
**Kind**: tdef

Used to hold a complex value.

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef struct DSPComplex DSPComplex;
```

#### Discussion

Complex data are stored as ordered pairs of floating-point numbers. Because they are stored as ordered pairs, complex vectors require address strides that are multiples of two. 

## Topics

### Fields
- [real](dspcomplex/1579938-real.md)
  The real part of the value.
- [imag](../accelerate/dspcomplex/imag.md)
  The imaginary part of the value.
### Instance Properties
- [imag](dspcomplex/1579947-imag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/dspcomplex)*