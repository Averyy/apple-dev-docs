# getFreeCount

**Framework**: Kernel  
**Kind**: instm

Totals the sizes of the free fragments.

## Declaration

```cpp
virtual IORangeScalar getFreeCount(
 void );
```

## Return Value

Returns the total of the free fragments sizes.

## Overview

This method returns the total of the sizes of the fragments on the free list.

## See Also

### Miscellaneous
- [allocate](./api-1810255-allocate.md)
  Allocates from the free list, at any offset.
- [allocateRange](./api-1810314-allocaterange.md)
  Allocates from the free list, at a set offset.
- [deallocate](./api-1810361-deallocate.md)
  Deallocates a range to the free list.
- [getFragmentCapacity](./api-1810407-getfragmentcapacity.md)
  Accessor to return the number of free fragments in the range.
- [getFragmentCount](./api-1810456-getfragmentcount.md)
  Accessor to return the number of free fragments in the range.
- [init](./api-1810534-init.md)
  Standard initializer for IORangeAllocator.
- [setFragmentCapacityIncrement](./api-1810575-setfragmentcapacityincrement.md)
  Sets the count of fragments the free list will increase by when full.
- [withRange](./api-1810621-withrange.md)
  Standard factory method for IORangeAllocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810490-getfreecount)*