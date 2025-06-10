# OSIncrementAtomic

**Framework**: Kernel  
**Kind**: func

32-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
SInt32 OSIncrementAtomic(volatile SInt32 *address);
```

#### Return_value

The value before the increment.

#### Discussion

The OSIncrementAtomic function increments the value at the specified address by one and returns the original value.

This function guarantees atomicity only with main system memory. It is specifically unsuitable for use on noncacheable memory such as that in devices; this function cannot guarantee atomicity, for example, on memory mapped from a PCI device.

## Parameters

- `address`: The 4-byte aligned address of the value to update atomically.

## See Also

- [OSIncrementAtomic8](1576477-osincrementatomic8.md)
  8-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic16](1576484-osincrementatomic16.md)
  16-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic64](1576480-osincrementatomic64.md)
  64-bit increment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576460-osincrementatomic)*