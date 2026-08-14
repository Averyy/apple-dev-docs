# vS64FullMulOdd

**Framework**: Kernel  
**Kind**: func

Signed 64-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.

**Availability**:
- macOS 10.0+

## Declaration

```swift
vSInt32 vS64FullMulOdd(vSInt32 vA, vSInt32 vB);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1411122-vs64fullmulodd)*