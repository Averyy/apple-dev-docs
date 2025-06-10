# withSubRange

**Framework**: Kernel  
**Kind**: instm

Constructs an IODeviceMemory instance, describing a subset of an existing IODeviceMemory range.

## Declaration

```swift
static IODeviceMemory * withSubRange( 
 IODeviceMemory *of, 
 IOPhysicalAddressoffset, 
 IOPhysicalLengthlength );
```

#### Return_value

Returns the created IODeviceMemory on success, to be released by the caller, or zero on failure.

#### Overview

This method creates an IODeviceMemory instance for a subset of an existing IODeviceMemory range, passed as a physical address offset and length. It just calls IOMemoryDescriptor::withSubRange.

## Parameters

- `of`: The parent IODeviceMemory of which a subrange is to be used for the new descriptor, which will be retained by the subrange IODeviceMemory.
- `offset`: A byte offset into the parent's memory.
- `length`: The length of the subrange.

## See Also

- [arrayFromList](iodevicememory/1811066-arrayfromlist.md)
  Constructs an OSArray of IODeviceMemory instances, each describing one physical range, and a tag value.
- [withRange](iodevicememory/1811085-withrange.md)
  Constructs an IODeviceMemory instance, describing one physical range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodevicememory/1811112-withsubrange)*