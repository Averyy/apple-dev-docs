# IORangeAllocator

**Framework**: Kernel  
**Kind**: cl

A utility class to manage allocations from a range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IORangeAllocator : OSObject
```

#### Overview

The IORangeAllocator class provides functions for allocating ranges, at a fixed or any offset, and freeing them back to a free list. It is useful for describing ranges of memory or address space without requiring storage in the memory - information describing the free elements is kept elsewhere. Ranges are described by a start offset and a size. IORangeAllocator is optionally protected against multithreaded access.

## Topics

### Miscellaneous
- [allocate](iorangeallocator/1810255-allocate.md)
  Allocates from the free list, at any offset.
- [allocateRange](iorangeallocator/1810314-allocaterange.md)
  Allocates from the free list, at a set offset.
- [deallocate](iorangeallocator/1810361-deallocate.md)
  Deallocates a range to the free list.
- [getFragmentCapacity](iorangeallocator/1810407-getfragmentcapacity.md)
  Accessor to return the number of free fragments in the range.
- [getFragmentCount](iorangeallocator/1810456-getfragmentcount.md)
  Accessor to return the number of free fragments in the range.
- [getFreeCount](iorangeallocator/1810490-getfreecount.md)
  Totals the sizes of the free fragments.
- [init](iorangeallocator/1810534-init.md)
  Standard initializer for IORangeAllocator.
- [setFragmentCapacityIncrement](iorangeallocator/1810575-setfragmentcapacityincrement.md)
  Sets the count of fragments the free list will increase by when full.
- [withRange](iorangeallocator/1810621-withrange.md)
  Standard factory method for IORangeAllocator.
### Instance Methods
- [- allocElement](iorangeallocator/1527740-allocelement.md)
- [- allocate](iorangeallocator/1527746-allocate.md)
- [- allocateRange](iorangeallocator/1527748-allocaterange.md)
- [- deallocElement](iorangeallocator/1527752-deallocelement.md)
- [- deallocate](iorangeallocator/1527758-deallocate.md)
- [- free](iorangeallocator/1527750-free.md)
- [- getFragmentCapacity](iorangeallocator/1527765-getfragmentcapacity.md)
- [- getFragmentCount](iorangeallocator/1527751-getfragmentcount.md)
- [- getFreeCount](iorangeallocator/1527760-getfreecount.md)
- [- getMetaClass](iorangeallocator/1527763-getmetaclass.md)
- [- init](iorangeallocator/1527756-init.md)
- [- serialize](iorangeallocator/1527761-serialize.md)
- [- setFragmentCapacityIncrement](iorangeallocator/1527742-setfragmentcapacityincrement.md)
### Type Methods
- [+ withRange](iorangeallocator/1527754-withrange.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOMalloc](1575326-iomalloc.md)
  Allocates general purpose, wired memory in the kernel map.
- [IOMallocAligned](1575291-iomallocaligned.md)
  Allocates wired memory in the kernel map, with an alignment restriction.
- [IOMallocPageable](1575327-iomallocpageable.md)
  Allocates pageable memory in the kernel map.
- [IOMallocZero](3074962-iomalloczero.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator)*