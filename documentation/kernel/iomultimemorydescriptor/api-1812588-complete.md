# complete

**Framework**: Kernel  
**Kind**: instm

Complete processing of the memory after an I/O transfer finishes.

## Declaration

```swift
virtual IOReturn complete(
 IODirection forDirection = forDirection);
```

#### Return_value

An IOReturn code.

#### Overview

This method should not be called unless a prepare was previously issued; the prepare() and complete() must occur in pairs, before and after an I/O transfer involving pageable memory.

## Parameters

- `forDirection`: The direction of the I/O just completed, or kIODirectionNone for the direction specified by the memory descriptor.

## See Also

- [getPhysicalSegment](iomultimemorydescriptor/1812610-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithDescriptors](iomultimemorydescriptor/1812635-initwithdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](iomultimemorydescriptor/1812660-prepare.md)
  Prepare the memory for an I/O transfer.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](iomultimemorydescriptor/1812685-withdescriptors.md)
  Create an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](iomultimemorydescriptor/1812714-withdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomultimemorydescriptor/1812588-complete)*