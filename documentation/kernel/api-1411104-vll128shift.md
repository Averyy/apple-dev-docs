# vLL128Shift

**Framework**: Kernel  
**Kind**: func

128-bit logical left shift.

**Availability**:
- macOS 10.5+

## Declaration

```swift
vUInt32 vLL128Shift(vUInt32 vA, vUInt8 vShiftFactor);
```

#### Return_value

Returns the shifted vector.

#### Discussion

This function treats the entire 128-bit vector as a single value to shift.

## Parameters

- `vA`: The vector to shift.
- `vShiftFactor`: The number of bits to shift the vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1411104-vll128shift)*