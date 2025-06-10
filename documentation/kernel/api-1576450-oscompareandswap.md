# OSCompareAndSwap

**Framework**: Kernel  
**Kind**: func

Compare and swap operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
Boolean OSCompareAndSwap(UInt32 oldValue, UInt32 newValue, volatile UInt32 *address);
```

#### Return_value

true if newValue was written to the address.

#### Discussion

The OSCompareAndSwap function compares the value at the specified address with oldVal. The value of newValue is written to the address only if oldValue and the value at the address are equal. OSCompareAndSwap returns true if newValue is written to the address; otherwise, it returns false.

This function guarantees atomicity only with main system memory. It is specifically unsuitable for use on noncacheable memory such as that in devices; this function cannot guarantee atomicity, for example, on memory mapped from a PCI device. Additionally, this function incorporates a memory barrier on systems with weakly-ordered memory architectures.

## Parameters

- `oldValue`: The value to compare at address.
- `newValue`: The value to write to address if oldValue compares true.
- `address`: The 4-byte aligned address of the data to update atomically.

## See Also

- [OSCompareAndSwap64](1576485-oscompareandswap64.md)
  64-bit compare and swap operation.
- [OSCompareAndSwapPtr](1576461-oscompareandswapptr.md)
  Compare and swap operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1576450-oscompareandswap)*