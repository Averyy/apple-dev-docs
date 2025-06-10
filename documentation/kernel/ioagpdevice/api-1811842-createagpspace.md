# createAGPSpace

**Framework**: Kernel  
**Kind**: instm

Allocates the AGP space, and enables AGP transactions on the primary and secondary.

## Declaration

```swift
virtual IOReturn createAGPSpace(
 IOOptionBitsoptions, 
 IOPhysicalAddress *address, 
 IOPhysicalLength *length );
```

#### Return_value

Returns an IOReturn code indicating success or failure.

#### Overview

This method should be called by the driver for the AGP primary device to set the size of the space and enable AGP transactions. It will destroy any AGP space currently allocated.

## Parameters

- `options`: No options are currently defined, pass zero.
- `address`: The physical range allocated for the AGP space is passed back to the caller.
- `length`: An in/out parameter - the caller sets the devices maximum AGP addressing and the actual size created is passed back.

## See Also

- [commitAGPMemory](ioagpdevice/1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [destroyAGPSpace](ioagpdevice/1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](ioagpdevice/1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](ioagpdevice/1811914-getagpspace.md)
  Returns the allocated AGP space.
- [getAGPStatus](ioagpdevice/1811928-getagpstatus.md)
  Returns the current state of the AGP bus.
- [releaseAGPMemory](ioagpdevice/1811943-releaseagpmemory.md)
  Releases memory addressable by AGP transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811842-createagpspace)*