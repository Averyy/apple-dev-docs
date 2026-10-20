# setMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

Add a portion of an IOMemoryDescriptor to the IOInterleavedMemoryDescriptor.

## Declaration

```cpp
virtual bool setMemoryDescriptor(
 IOMemoryDescriptor *descriptor, 
 IOByteCountoffset, 
 IOByteCountlength );
```

#### Return Value

Returns true the portion was successfully added.

#### Overview

This method adds the portion of an IOMemoryDescriptor described by the offset and length parameters to the end of the IOInterleavedMemoryDescriptor. A single IOMemoryDescriptor may be added as many times as there is room for it. The offset and length must describe a portion entirely within the IOMemoryDescriptor.

## Parameters

- `descriptor`: An IOMemoryDescriptor to be added to the IOInterleavedMemoryDescriptor. Its direction must be compatible with that of the IOInterleavedMemoryDescriptor.
- `offset`: The offset into the IOMemoryDescriptor of the portion that will be added to the virtualized buffer.
- `length`: The length of the portion of the IOMemoryDescriptor to be added to the virtualized buffer.

## See Also

### Miscellaneous
- [clearMemoryDescriptors](./api-1812566-clearmemorydescriptors.md)
  Clear all of the IOMemoryDescriptors currently contained in and reset the IOInterleavedMemoryDescriptor.
- [complete](./api-1812579-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](./api-1812587-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithCapacity](./api-1812598-initwithcapacity.md)
  Initialize an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](./api-1812608-prepare.md)
  Prepare the memory for an I/O transfer.
- [withCapacity](./api-1812626-withcapacity.md)
  Create an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerleavedmemorydescriptor/1812618-setmemorydescriptor)*