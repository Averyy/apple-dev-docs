# OSDecrementAtomic8

**Framework**: Kernel  
**Kind**: func

8-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
SInt8 OSDecrementAtomic8(volatile SInt8 *address);
```

#### Return_value

The value before the decrement.

#### Discussion

The OSDecrementAtomic8 function decrements the value at the specified address by one and returns the original value.

This function guarantees atomicity only with main system memory. It is specifically unsuitable for use on noncacheable memory such as that in devices; this function cannot guarantee atomicity, for example, on memory mapped from a PCI device. Previous incarnations of this function incorporated a memory barrier on systems with weakly-ordered memory architectures, but current versions contain no barriers.

## Parameters

- `address`: The address of the value to update atomically.

## See Also

- [OSDecrementAtomic](1576455-osdecrementatomic.md)
  32-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic16](1576468-osdecrementatomic16.md)
  16-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic64](1576449-osdecrementatomic64.md)
  64-bit decrement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576458-osdecrementatomic8)*