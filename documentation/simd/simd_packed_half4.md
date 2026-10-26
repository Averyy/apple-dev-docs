# simd_packed_half4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

## Declaration

```swift
typealias simd_packed_half4 = SIMD4<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(4))) simd_packed_half4;
```

#### Discussion

A vector of four 16-bit floating-point numbers with relaxed alignment.

simd::packed::half4. The alignment of this type is that of the underlying scalar element type, so you can use it to load or store from an array of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_packed_half4)*