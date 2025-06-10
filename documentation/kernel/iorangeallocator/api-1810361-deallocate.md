# deallocate

**Framework**: Kernel  
**Kind**: instm

Deallocates a range to the free list.

## Declaration

```swift
virtual void deallocate(
 IORangeScalarstart, 
 IORangeScalarsize );
```

#### Overview

This method deallocates a range to the free list, given a the start offset and length passed in.

## Parameters

- `start`: The beginning of the range requested.
- `size`: Returns the size of the range requested.

## See Also

- [allocate](iorangeallocator/1810255-allocate.md)
  Allocates from the free list, at any offset.
- [allocateRange](iorangeallocator/1810314-allocaterange.md)
  Allocates from the free list, at a set offset.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810361-deallocate)*