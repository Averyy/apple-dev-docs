# prepare

**Framework**: Kernel  
**Kind**: instm

Prepare the memory for an I/O transfer.

## Declaration

```cpp
virtual IOReturn prepare(
 IODirection forDirection = forDirection);
```

## Return Value

An IOReturn code.

## Overview

This involves paging in the memory, if necessary, and wiring it down for the duration of the transfer. The complete() method completes the processing of the memory after the I/O transfer finishes. This method needn't called for non-pageable memory.

## Parameters

- `forDirection`: The direction of the I/O just completed, or kIODirectionNone for the direction specified by the memory descriptor.

## See Also

### Miscellaneous
- [complete](./api-1812588-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](./api-1812610-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithDescriptors](./api-1812635-initwithdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](./api-1812685-withdescriptors.md)
  Create an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](./api-1812714-withdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomultimemorydescriptor/1812660-prepare)*