# arrayFromList

**Framework**: Kernel  
**Kind**: instm

Constructs an OSArray of IODeviceMemory instances, each describing one physical range, and a tag value.

## Declaration

```swift
static OSArray * arrayFromList( 
 InitElement list[], 
 IOItemCount count );
```

#### Return_value

Returns a created OSArray of IODeviceMemory objects, to be released by the caller, or zero on failure.

#### Overview

This method creates IODeviceMemory instances for each physical range passed in an IODeviceMemory::InitElement array. Each element consists of a physical address, length and tag value for the IODeviceMemory. The instances are returned as a created OSArray.

## Parameters

- `list`: An array of IODeviceMemory::InitElement structures.
- `count`: The number of elements in the list.

## See Also

- [withRange](iodevicememory/1811085-withrange.md)
  Constructs an IODeviceMemory instance, describing one physical range.
- [withSubRange](iodevicememory/1811112-withsubrange.md)
  Constructs an IODeviceMemory instance, describing a subset of an existing IODeviceMemory range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodevicememory/1811066-arrayfromlist)*