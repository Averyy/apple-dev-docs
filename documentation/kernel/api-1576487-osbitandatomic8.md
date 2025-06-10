# OSBitAndAtomic8

**Framework**: Kernel  
**Kind**: func

8-bit logical and operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
UInt8 OSBitAndAtomic8(UInt32 mask, volatile UInt8 *address);
```

#### Return_value

The value before the bitwise operation.

#### Discussion

The OSBitAndAtomic8 function logically ands the bits of the specified mask into the value at the specified address and returns the original value.

This function guarantees atomicity only with main system memory. It is specifically unsuitable for use on noncacheable memory such as that in devices; this function cannot guarantee atomicity, for example, on memory mapped from a PCI device. Additionally, this function incorporates a memory barrier on systems with weakly-ordered memory architectures.

## Parameters

- `mask`: The mask to logically and with the value.
- `address`: The address of the value to update atomically.

## See Also

- [OSBitAndAtomic](1576481-osbitandatomic.md)
  32-bit logical and operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitAndAtomic16](1576453-osbitandatomic16.md)
  16-bit logical and operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitOrAtomic](1576467-osbitoratomic.md)
  32-bit logical or operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitOrAtomic8](1576478-osbitoratomic8.md)
  8-bit logical or operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitOrAtomic16](1576466-osbitoratomic16.md)
  16-bit logical or operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitXorAtomic](1576476-osbitxoratomic.md)
  32-bit logical xor operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitXorAtomic8](1576459-osbitxoratomic8.md)
  8-bit logical xor operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitXorAtomic16](1576464-osbitxoratomic16.md)
  16-bit logical xor operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576487-osbitandatomic8)*