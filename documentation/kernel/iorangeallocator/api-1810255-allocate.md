# allocate

**Framework**: Kernel  
**Kind**: instm

Allocates from the free list, at any offset.

## Declaration

```swift
virtual bool allocate(
 IORangeScalar size, 
 IORangeScalar *result, 
 IORangeScalar alignment = 0 );
```

#### Return_value

Returns true if the allocation was successful, else false.

#### Overview

This method allocates a range from the free list. The alignment will default to the alignment set when the allocator was created or may be set here.

## Parameters

- `size`: The size of the range requested.
- `result`: The beginning of the range allocated is returned here on success.
- `alignment`: If zero is passed, default to the allocators alignment, otherwise pass an alignment required for the allocation, for example 4096 to page align.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810255-allocate)*