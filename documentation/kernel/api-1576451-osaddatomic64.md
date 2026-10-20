# OSAddAtomic64

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

64-bit atomic add operation.

**Availability**:
- macOS 10.5+

## Declaration

```c
SInt64 OSAddAtomic64(SInt64 theAmount, volatile SInt64 *address);
```

#### Discussion

See OSAddAtomic.

## See Also

### Additions
- [OSAddAtomic](./api-1576452-osaddatomic.md)
  32-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic8](./api-1576483-osaddatomic8.md)
  8-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic16](./api-1576475-osaddatomic16.md)
  16-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576451-osaddatomic64)*