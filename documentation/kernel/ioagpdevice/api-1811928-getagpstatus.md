# getAGPStatus

**Framework**: Kernel  
**Kind**: instm

Returns the current state of the AGP bus.

## Declaration

```cpp
virtual IOOptionBits getAGPStatus(
 IOOptionBits which = which );
```

## Return Value

Returns mask of status bits for the AGP bus.

## Overview

Returns state bits for the AGP bus. Only one type of status is currently defined.

## Parameters

- `which`: Type of status - only kIOAGPDefaultStatus is currently valid.

## See Also

### Miscellaneous
- [commitAGPMemory](./api-1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [createAGPSpace](./api-1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [destroyAGPSpace](./api-1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](./api-1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](./api-1811914-getagpspace.md)
  Returns the allocated AGP space.
- [releaseAGPMemory](./api-1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811928-getagpstatus)*