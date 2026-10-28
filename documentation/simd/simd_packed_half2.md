# simd_packed_half2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

## Declaration

```swift
typealias simd_packed_half2 = SIMD2<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(2))) simd_packed_half2;
```

## Discussion

A vector of two 16-bit floating-point numbers with relaxed alignment.

simd::packed::half2. The alignment of this type is that of the underlying scalar element type, so you can use it to load or store from an array of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_packed_half2)*