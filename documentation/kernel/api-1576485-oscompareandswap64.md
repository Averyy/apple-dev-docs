# OSCompareAndSwap64

**Framework**: Kernel  
**Kind**: func

64-bit compare and swap operation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
Boolean OSCompareAndSwap64(UInt64 oldValue, UInt64 newValue, volatile UInt64 *address);
```

#### Discussion

See OSCompareAndSwap.

## See Also

- [OSCompareAndSwap](1576450-oscompareandswap.md)
  Compare and swap operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSCompareAndSwapPtr](1576461-oscompareandswapptr.md)
  Compare and swap operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576485-oscompareandswap64)*