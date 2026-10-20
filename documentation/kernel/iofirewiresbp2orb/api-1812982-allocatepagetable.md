# allocatePageTable

**Framework**: Kernel  
**Kind**: instm

Allocates memory for the page table.

## Declaration

```cpp
virtual IOReturn allocatePageTable(
 UInt32entryCount );
```

#### Overview

Page table allocation is handle automatically by the ORB, except if the kFWSBP2CommandFixedSize flags is set. In this case we will fail to write a page table if we need more page table space than we have already. This method is exposed so these drivers can preallocate as much page table as they need. This is useful if your driver is part of the paging path and cannot allow allocations to occur.

## Parameters

- `entryCount`: number of entries of page table to be allocated.

## See Also

### Miscellaneous
- [deallocatePageTable](./api-1812989-deallocatepagetable.md)
  Frees up memory allocated for the page table.
- [getCommandBufferDescriptor](./api-1812997-getcommandbufferdescriptor.md)
  Returns the memory descriptor representing the command buffer.
- [getCommandFlags](./api-1813002-getcommandflags.md)
  Sets configuration flags for the ORB.
- [getCommandGeneration](./api-1813010-getcommandgeneration.md)
  Gets the command generation.
- [getCommandTimeout](./api-1813017-getcommandtimeout.md)
  Gets the timeout of the ORB.
- [getLogin](./api-1813023-getlogin.md)
  Gets the login associated with this ORB.
- [getMaxPayloadSize](./api-1813031-getmaxpayloadsize.md)
  Gets max payload size for the ORB.
- [getORBAddress](./api-1813039-getorbaddress.md)
  Returns the FireWire address of this ORB.
- [getRefCon](./api-1813049-getrefcon.md)
  Returns the refCon set with setRefCon.
- [getRefCon64](./api-1813059-getrefcon64.md)
  Returns the 64 bit refCon set with setRefCon64.
- [release](./api-1813072-release.md)
  Primary implementation of the release mechanism.
- [releaseCommandBuffers](./api-1813085-releasecommandbuffers.md)
  Releases SBP2's reference to the command buffers.
- [setBufferConstraints](./api-1813096-setbufferconstraints.md)
  Configures page table generation parameters
- [setCommandBlock(IOMemoryDescriptor *)](./api-1813109-setcommandblock.md)
  Sets the command block portion of the ORB.
- [setCommandBlock(void *, UInt32)](./api-1813121-setcommandblock.md)
  Sets the command block portion of the ORB.
- [setCommandBuffers](./api-1813129-setcommandbuffers.md)
  Creates a page table from a list of ranges.
- [setCommandBuffersAsRanges(IOMemoryDescriptor *, UInt32, UInt32)](./api-1813141-setcommandbuffersasranges.md)
  Creates a page table from a list of ranges.
- [setCommandBuffersAsRanges(IOVirtualRange *, UInt32, IODirection, task_t, UInt32, UInt32)](./api-1813149-setcommandbuffersasranges.md)
  Creates a page table from a list of ranges.
- [setCommandBuffersAsRanges64](./api-1813162-setcommandbuffersasranges64.md)
  Creates a page table from a list of 64 bit ranges.
- [setCommandFlags](./api-1813178-setcommandflags.md)
  Sets configuration flags for the ORB.
- [setCommandGeneration](./api-1813197-setcommandgeneration.md)
  Sets the command generation.
- [setCommandTimeout](./api-1813211-setcommandtimeout.md)
  Sets the timeout of the ORB.
- [setMaxPayloadSize](./api-1813231-setmaxpayloadsize.md)
  Sets max payload size for the ORB.
- [setRefCon](./api-1813244-setrefcon.md)
  Sets the ORB refCon.
- [setRefCon64](./api-1813262-setrefcon64.md)
  Sets the ORB refCon as a 64 bit value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2orb/1812982-allocatepagetable)*