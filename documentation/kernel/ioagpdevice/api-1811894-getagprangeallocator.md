# getAGPRangeAllocator

**Framework**: Kernel  
**Kind**: instm

Accessor to obtain the AGP range allocator.

## Declaration

```swift
virtual IORangeAllocator * getAGPRangeAllocator(
 void );
```

#### Return_value

Returns a pointer to the range allocator for the AGP space.

#### Overview

To allocate ranges in AGP space, obtain a range allocator for the space with this method. It is retained while the space is created (until destroyAGPSpace is called) and should not be released by the caller.

## See Also

- [commitAGPMemory](ioagpdevice/1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [createAGPSpace](ioagpdevice/1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [destroyAGPSpace](ioagpdevice/1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPSpace](ioagpdevice/1811914-getagpspace.md)
  Returns the allocated AGP space.
- [getAGPStatus](ioagpdevice/1811928-getagpstatus.md)
  Returns the current state of the AGP bus.
- [releaseAGPMemory](ioagpdevice/1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811894-getagprangeallocator)*