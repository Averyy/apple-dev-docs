# OSAddAtomic16

**Framework**: Kernel  
**Kind**: func

16-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
SInt16 OSAddAtomic16(SInt32 amount, volatile SInt16 *address);
```

#### Return_value

The value before the addition

#### Discussion

The OSAddAtomic16 function adds the specified amount to the value at the specified address and returns the original value.

This function guarantees atomicity only with main system memory. It is specifically unsuitable for use on noncacheable memory such as that in devices; this function cannot guarantee atomicity, for example, on memory mapped from a PCI device. Previous incarnations of this function incorporated a memory barrier on systems with weakly-ordered memory architectures, but current versions contain no barriers.

## Parameters

- `address`: The 2-byte aligned address of the value to update atomically.

## See Also

- [OSAddAtomic](1576452-osaddatomic.md)
  32-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic8](1576483-osaddatomic8.md)
  8-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic64](1576451-osaddatomic64.md)
  64-bit atomic add operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576475-osaddatomic16)*