# getAGPStatus

**Framework**: Kernel  
**Kind**: instm

Returns the current state of the AGP bus.

## Declaration

```swift
virtual IOOptionBits getAGPStatus(
 IOOptionBits which = which );
```

#### Return_value

Returns mask of status bits for the AGP bus.

#### Overview

Returns state bits for the AGP bus. Only one type of status is currently defined.

## Parameters

- `which`: Type of status - only kIOAGPDefaultStatus is currently valid.

## See Also

- [commitAGPMemory](ioagpdevice/1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [createAGPSpace](ioagpdevice/1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [destroyAGPSpace](ioagpdevice/1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](ioagpdevice/1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](ioagpdevice/1811914-getagpspace.md)
  Returns the allocated AGP space.
- [releaseAGPMemory](ioagpdevice/1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811928-getagpstatus)*