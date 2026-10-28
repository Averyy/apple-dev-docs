# OSIncrementAtomic64

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

64-bit increment.

**Availability**:
- macOS 10.5+

## Declaration

```c
SInt64 OSIncrementAtomic64(volatile SInt64 *address);
```

## Discussion

See OSIncrementAtomic.

## See Also

### Increment
- [OSIncrementAtomic](./api-1576460-osincrementatomic.md)
  32-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic8](./api-1576477-osincrementatomic8.md)
  8-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic16](./api-1576484-osincrementatomic16.md)
  16-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576480-osincrementatomic64)*