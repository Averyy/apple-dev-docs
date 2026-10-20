# destroyAGPSpace

**Framework**: Kernel  
**Kind**: instm

Destroys the AGP space, and disables AGP transactions on the primary and secondary.

## Declaration

```cpp
virtual IOReturn destroyAGPSpace(
 void );
```

#### Overview

This method should be called by the driver to shutdown AGP transactions and release resources.

## See Also

### Miscellaneous
- [commitAGPMemory](./api-1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [createAGPSpace](./api-1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](./api-1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](./api-1811914-getagpspace.md)
  Returns the allocated AGP space.
- [getAGPStatus](./api-1811928-getagpstatus.md)
  Returns the current state of the AGP bus.
- [releaseAGPMemory](./api-1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811870-destroyagpspace)*