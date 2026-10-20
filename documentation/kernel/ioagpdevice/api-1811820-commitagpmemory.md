# commitAGPMemory

**Framework**: Kernel  
**Kind**: instm

Makes memory addressable by AGP transactions.

## Declaration

```cpp
virtual IOReturn commitAGPMemory(
 IOMemoryDescriptor *memory, 
 IOByteCount agpOffset, 
 IOOptionBits options = 0 );
```

#### Return Value

Returns an IOReturn code indicating success or failure.

#### Overview

Makes the memory described by the IOMemoryDescriptor object addressable by AGP by entering its pages into the GART array, given an offset into AGP space supplied by the caller (usually allocated by the AGP range allocator). It is the caller's responsibility to prepare non-kernel pageable memory before calling this method, with IOMemoryDescriptor::prepare.

## Parameters

- `memory`: A IOMemoryDescriptor object describing the memory to add to the GART.
- `agpOffset`: An offset into AGP space that the caller has allocated - usually allocated by the AGP range allocator.
- `options`: Pass kIOAGPGartInvalidate if the AGP target should invalidate any GART TLB.

## See Also

### Miscellaneous
- [createAGPSpace](./api-1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [destroyAGPSpace](./api-1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](./api-1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](./api-1811914-getagpspace.md)
  Returns the allocated AGP space.
- [getAGPStatus](./api-1811928-getagpstatus.md)
  Returns the current state of the AGP bus.
- [releaseAGPMemory](./api-1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811820-commitagpmemory)*