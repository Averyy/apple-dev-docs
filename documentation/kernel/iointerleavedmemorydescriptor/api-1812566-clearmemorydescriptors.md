# clearMemoryDescriptors

**Framework**: Kernel  
**Kind**: instm

Clear all of the IOMemoryDescriptors currently contained in and reset the IOInterleavedMemoryDescriptor.

## Declaration

```swift
virtual void clearMemoryDescriptors(
 IODirection direction = direction );
```

#### Overview

Clears each IOMemoryDescriptor by completing (if needed) and releasing. The IOInterleavedMemoryDescriptor is then reset and may accept new descriptors up to the capacity specified when it was created.

## Parameters

- `direction`: An I/O direction to be associated with the descriptor, which may affect the operation of the prepare and complete methods on some architectures.

## See Also

- [complete](iointerleavedmemorydescriptor/1812579-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](iointerleavedmemorydescriptor/1812587-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithCapacity](iointerleavedmemorydescriptor/1812598-initwithcapacity.md)
  Initialize an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](iointerleavedmemorydescriptor/1812608-prepare.md)
  Prepare the memory for an I/O transfer.
- [setMemoryDescriptor](iointerleavedmemorydescriptor/1812618-setmemorydescriptor.md)
  Add a portion of an IOMemoryDescriptor to the IOInterleavedMemoryDescriptor.
- [withCapacity](iointerleavedmemorydescriptor/1812626-withcapacity.md)
  Create an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerleavedmemorydescriptor/1812566-clearmemorydescriptors)*