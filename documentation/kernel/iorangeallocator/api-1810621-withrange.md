# withRange

**Framework**: Kernel  
**Kind**: instm

Standard factory method for IORangeAllocator.

## Declaration

```swift
static IORangeAllocator * withRange(
 IORangeScalar endOfRange, 
 IORangeScalar defaultAlignment = 0, 
 UInt32 capacity = 0, 
 IOOptionBits options = 0 );
```

#### Return_value

Returns the new IORangeAllocator instance, to be released by the caller, or zero on failure.

#### Overview

This method allocates and initializes an IORangeAllocator and optionally sets the free list to contain one fragment, from zero to an endOfRange parameter. The capacity in terms of free fragments and locking options are set for the instance.

## Parameters

- `endOfRange`: If the free list is to contain an initial fragment, set endOfRange to the last offset in the range, ie. size - 1, to create a free fragment for the range zero to endOfRange inclusive. If zero is passed the free list will be initialized empty, and can be populated with calls to the deallocate method.
- `defaultAlignment`: If this parameter is non-zero it specifies a required alignment for all allocations, for example pass 256 to align allocations on 256 byte boundaries. Zero or one specify unaligned allocations.
- `capacity`: Sets the initial size of the free list in number of non-contiguous fragments. This value is also used for the capacityIncrement.
- `options`: Pass kLocking if the instance can be used by multiple threads.

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
- [setFragmentCapacityIncrement](iorangeallocator/1810575-setfragmentcapacityincrement.md)
  Sets the count of fragments the free list will increase by when full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iorangeallocator/1810621-withrange)*