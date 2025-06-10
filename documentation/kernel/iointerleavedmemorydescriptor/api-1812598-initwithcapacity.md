# initWithCapacity

**Framework**: Kernel  
**Kind**: instm

Initialize an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.

## Declaration

```swift
virtual bool initWithCapacity(
 IOByteCountcapacity, 
 IODirectiondirection );
```

#### Return_value

The created IOInterleavedMemoryDescriptor on success, to be released by the caller, or zero on failure.

#### Overview

This method initializes an IOInterleavedMemoryDescriptor for memory consisting of portions of a number of other IOMemoryDescriptors, chained end-to-end (in the order they appear in the array) to represent a single contiguous memory buffer.

## Parameters

- `capacity`: The maximum number of IOMemoryDescriptors that may be subsequently added to this IOInterleavedMemoryDescriptor.
- `direction`: An I/O direction to be associated with the descriptor, which may affect the operation of the prepare and complete methods on some architectures.

## See Also

- [clearMemoryDescriptors](iointerleavedmemorydescriptor/1812566-clearmemorydescriptors.md)
  Clear all of the IOMemoryDescriptors currently contained in and reset the IOInterleavedMemoryDescriptor.
- [complete](iointerleavedmemorydescriptor/1812579-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](iointerleavedmemorydescriptor/1812587-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [prepare](iointerleavedmemorydescriptor/1812608-prepare.md)
  Prepare the memory for an I/O transfer.
- [setMemoryDescriptor](iointerleavedmemorydescriptor/1812618-setmemorydescriptor.md)
  Add a portion of an IOMemoryDescriptor to the IOInterleavedMemoryDescriptor.
- [withCapacity](iointerleavedmemorydescriptor/1812626-withcapacity.md)
  Create an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerleavedmemorydescriptor/1812598-initwithcapacity)*