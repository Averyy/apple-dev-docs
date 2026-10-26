# simd_packed_half16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

## Declaration

```swift
typealias simd_packed_half16 = SIMD16<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(16))) simd_packed_half16;
```

#### Discussion

A vector of sixteen 16-bit floating-point numbers with relaxed alignment.

This type is not available in Metal. The alignment of this type is only that of the underlying scalar element type, so you can use it to load or store from an array of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_packed_half16)*