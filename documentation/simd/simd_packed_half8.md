# simd_packed_half8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

## Declaration

```swift
typealias simd_packed_half8 = SIMD8<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(8))) simd_packed_half8;
```

#### Discussion

A vector of eight 16-bit floating-point numbers with relaxed alignment.

This type is not available in Metal. The alignment of this type is only that of the underlying scalar element type, so you can use it to load or store from an array of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_packed_half8)*