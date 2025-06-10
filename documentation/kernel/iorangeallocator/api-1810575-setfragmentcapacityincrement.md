# setFragmentCapacityIncrement

**Framework**: Kernel  
**Kind**: instm

Sets the count of fragments the free list will increase by when full.

## Declaration

```swift
virtual void setFragmentCapacityIncrement(
 UInt32count );
```

#### Overview

This method sets the number of extra fragments the free list will expand to when full. It defaults to the initial capacity.

## Parameters

- `count`: The number of fragments to increment the capacity by when the free list is full.

## See Also

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
- [withRange](iorangeallocator/1810621-withrange.md)
  Standard factory method for IORangeAllocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810575-setfragmentcapacityincrement)*