# allocateRange

**Framework**: Kernel  
**Kind**: instm

Allocates from the free list, at a set offset.

## Declaration

```swift
virtual bool allocateRange(
 IORangeScalarstart, 
 IORangeScalarsize );
```

#### Return_value

Returns true if the allocation was successful, else false.

#### Overview

This method allocates a range from the free list, given a set offset passed in.

## Parameters

- `start`: The beginning of the range requested.
- `size`: The size of the range requested.

## See Also

- [allocate](iorangeallocator/1810255-allocate.md)
  Allocates from the free list, at any offset.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810314-allocaterange)*