# OSDecrementAtomic64

**Framework**: Kernel  
**Kind**: func

64-bit decrement.

**Availability**:
- macOS 10.5+

## Declaration

```swift
SInt64 OSDecrementAtomic64(volatile SInt64 *address);
```

#### Discussion

See OSDecrementAtomic.

## See Also

- [OSDecrementAtomic](1576455-osdecrementatomic.md)
  32-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic8](1576458-osdecrementatomic8.md)
  8-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic16](1576468-osdecrementatomic16.md)
  16-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576449-osdecrementatomic64)*