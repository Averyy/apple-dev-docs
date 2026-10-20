# vLL128Shift

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

128-bit logical left shift.

**Availability**:
- macOS 10.5+

## Declaration

```c
vUInt32 vLL128Shift(vUInt32 vA, vUInt8 vShiftFactor);
```

#### Return Value

Returns the shifted vector.

#### Discussion

This function treats the entire 128-bit vector as a single value to shift.

## Parameters

- `vA`: The vector to shift.
- `vShiftFactor`: The number of bits to shift the vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1411104-vll128shift)*