# simd_packed_half32

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

## Declaration

```swift
typealias simd_packed_half32 = SIMD32<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(32))) simd_packed_half32;
```

## Discussion

A vector of thirty-two 16-bit floating-point numbers with relaxed alignment.

This type is not available in Metal. The alignment of this type is only that of the underlying scalar element type, so you can use it to load or store from an array of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_packed_half32)*