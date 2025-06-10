# getFragmentCapacity

**Framework**: Kernel  
**Kind**: instm

Accessor to return the number of free fragments in the range.

## Declaration

```swift
virtual UInt32 getFragmentCapacity(
 void );
```

#### Return_value

Returns the current capacity of free fragment list.

#### Overview

This method returns the current capacity of the free fragment list.

## See Also

- [allocate](iorangeallocator/1810255-allocate.md)
  Allocates from the free list, at any offset.
- [allocateRange](iorangeallocator/1810314-allocaterange.md)
  Allocates from the free list, at a set offset.
- [deallocate](iorangeallocator/1810361-deallocate.md)
  Deallocates a range to the free list.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810407-getfragmentcapacity)*