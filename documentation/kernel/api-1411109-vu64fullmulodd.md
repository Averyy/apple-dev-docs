# vU64FullMulOdd

**Framework**: Kernel  
**Kind**: func

Unsigned 64-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.

**Availability**:
- macOS 10.0+

## Declaration

```swift
vUInt32 vU64FullMulOdd(vUInt32 vA, vUInt32 vB);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1411109-vu64fullmulodd)*