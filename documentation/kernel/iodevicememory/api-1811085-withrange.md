# withRange

**Framework**: Kernel  
**Kind**: instm

Constructs an IODeviceMemory instance, describing one physical range.

## Declaration

```swift
static IODeviceMemory * withRange( 
 IOPhysicalAddressaddress, 
 IOPhysicalLengthwithLength );
```

#### Return_value

Returns the created IODeviceMemory on success, to be released by the caller, or zero on failure.

#### Overview

This method creates an IODeviceMemory instance for one physical range passed as a physical address and length. It just calls IOMemoryDescriptor::withPhysicalAddress.

## Parameters

- `address`: The physical address of the first byte in the memory.
- `withLength`: The length of memory.

## See Also

- [arrayFromList](iodevicememory/1811066-arrayfromlist.md)
  Constructs an OSArray of IODeviceMemory instances, each describing one physical range, and a tag value.
- [withSubRange](iodevicememory/1811112-withsubrange.md)
  Constructs an IODeviceMemory instance, describing a subset of an existing IODeviceMemory range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodevicememory/1811085-withrange)*