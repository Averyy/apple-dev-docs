# OSTestAndSet

**Framework**: Kernel  
**Kind**: func

Bit test and set operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
Boolean OSTestAndSet(UInt32 bit, volatile UInt8 *startAddress);
```

#### Return_value

true if the bit was already set, false otherwise.

#### Discussion

This function guarantees atomicity only with main system memory. It is specifically unsuitable for use on noncacheable memory such as that in devices; this function cannot guarantee atomicity, for example, on memory mapped from a PCI device. Additionally, this function incorporates a memory barrier on systems with weakly-ordered memory architectures.

The OSTestAndSet function sets a single bit in a byte at a specified address. It returns true if the bit was already set, false otherwise.

## Parameters

- `bit`: The bit number in the range 0 through 7.
- `startAddress`: The address of the byte to update atomically.

## See Also

- [OSTestAndClear](1576463-ostestandclear.md)
  Bit test and clear operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576456-ostestandset)*