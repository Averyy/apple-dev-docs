# withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)

**Framework**: Kernel  
**Kind**: instm

Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.

## Declaration

```swift
virtual bool initWithDescriptors( 
 IOMemoryDescriptor **descriptors, 
 UInt32 withCount, 
 IODirection withDirection, 
 bool asReference = false );
```

#### Return_value

The created IOMultiMemoryDescriptor on success, to be released by the caller, or zero on failure.

#### Overview

This method initializes an IOMultiMemoryDescriptor for memory consisting of a number of other IOMemoryDescriptors, chained end-to-end (in the order they appear in the array) to represent a single contiguous memory buffer. Passing the descriptor array as a reference will avoid an extra allocation.

## Parameters

- `descriptors`: An array of IOMemoryDescriptors which make up the memory to be described.
- `withCount`: The object count for the descriptors array.
- `withDirection`: An I/O direction to be associated with the descriptor, which may affect the operation of the prepare and complete methods on some architectures.
- `asReference`: If false, the IOMultiMemoryDescriptor object will make a copy of the descriptors array, otherwise, the array will be used in situ, avoiding an extra allocation.

## See Also

- [complete](iomultimemorydescriptor/1812588-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](iomultimemorydescriptor/1812610-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithDescriptors](iomultimemorydescriptor/1812635-initwithdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](iomultimemorydescriptor/1812660-prepare.md)
  Prepare the memory for an I/O transfer.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](iomultimemorydescriptor/1812685-withdescriptors.md)
  Create an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomultimemorydescriptor/1812714-withdescriptors)*