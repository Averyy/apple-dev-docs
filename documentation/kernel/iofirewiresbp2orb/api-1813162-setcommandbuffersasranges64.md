# setCommandBuffersAsRanges64

**Framework**: Kernel  
**Kind**: instm

Creates a page table from a list of 64 bit ranges.

## Declaration

```swift
IOReturn setCommandBuffersAsRanges64(
 IOAddressRange *ranges, 
 uint64_t withCount, 
 IODirection withDirection, 
 task_t withTask, 
 uint64_t offset = 0, 
 uint64_t length = 0);
```

#### Return_value

Returns KIOReturnSuccess if the page table was written successfully.

#### Overview

Creates a page table with the given parameters. Any addresses mapped by this method must remain valid until setCommandBuffers is called again or releaseCommandBuffers is called. The SBP2 services do not release references to the command buffers just because the command has completed. This is a 64 bit compatible version of setCommandBuffersAsRanges.

## Parameters

- `ranges`: An array of ranges representing the data to be transfered.
- `withCount`: The number of ranges in the ranges array.
- `withDirection`: An IODirection indicating the direction of data transfer.
- `withTask`: The task that these adressses reside in.
- `offset`: Offset in bytes into data to begin writing table at.
- `length`: Number of bytes of data to map from offset.

## See Also

- [allocatePageTable](iofirewiresbp2orb/1812982-allocatepagetable.md)
  Allocates memory for the page table.
- [deallocatePageTable](iofirewiresbp2orb/1812989-deallocatepagetable.md)
  Frees up memory allocated for the page table.
- [getCommandBufferDescriptor](iofirewiresbp2orb/1812997-getcommandbufferdescriptor.md)
  Returns the memory descriptor representing the command buffer.
- [getCommandFlags](iofirewiresbp2orb/1813002-getcommandflags.md)
  Sets configuration flags for the ORB.
- [getCommandGeneration](iofirewiresbp2orb/1813010-getcommandgeneration.md)
  Gets the command generation.
- [getCommandTimeout](iofirewiresbp2orb/1813017-getcommandtimeout.md)
  Gets the timeout of the ORB.
- [getLogin](iofirewiresbp2orb/1813023-getlogin.md)
  Gets the login associated with this ORB.
- [getMaxPayloadSize](iofirewiresbp2orb/1813031-getmaxpayloadsize.md)
  Gets max payload size for the ORB.
- [getORBAddress](iofirewiresbp2orb/1813039-getorbaddress.md)
  Returns the FireWire address of this ORB.
- [getRefCon](iofirewiresbp2orb/1813049-getrefcon.md)
  Returns the refCon set with setRefCon.
- [getRefCon64](iofirewiresbp2orb/1813059-getrefcon64.md)
  Returns the 64 bit refCon set with setRefCon64.
- [release](iofirewiresbp2orb/1813072-release.md)
  Primary implementation of the release mechanism.
- [releaseCommandBuffers](iofirewiresbp2orb/1813085-releasecommandbuffers.md)
  Releases SBP2's reference to the command buffers.
- [setBufferConstraints](iofirewiresbp2orb/1813096-setbufferconstraints.md)
  Configures page table generation parameters
- [setCommandBlock(IOMemoryDescriptor *)](iofirewiresbp2orb/1813109-setcommandblock.md)
  Sets the command block portion of the ORB.
- [setCommandBlock(void *, UInt32)](iofirewiresbp2orb/1813121-setcommandblock.md)
  Sets the command block portion of the ORB.
- [setCommandBuffers](iofirewiresbp2orb/1813129-setcommandbuffers.md)
  Creates a page table from a list of ranges.
- [setCommandBuffersAsRanges(IOMemoryDescriptor *, UInt32, UInt32)](iofirewiresbp2orb/1813141-setcommandbuffersasranges.md)
  Creates a page table from a list of ranges.
- [setCommandBuffersAsRanges(IOVirtualRange *, UInt32, IODirection, task_t, UInt32, UInt32)](iofirewiresbp2orb/1813149-setcommandbuffersasranges.md)
  Creates a page table from a list of ranges.
- [setCommandFlags](iofirewiresbp2orb/1813178-setcommandflags.md)
  Sets configuration flags for the ORB.
- [setCommandGeneration](iofirewiresbp2orb/1813197-setcommandgeneration.md)
  Sets the command generation.
- [setCommandTimeout](iofirewiresbp2orb/1813211-setcommandtimeout.md)
  Sets the timeout of the ORB.
- [setMaxPayloadSize](iofirewiresbp2orb/1813231-setmaxpayloadsize.md)
  Sets max payload size for the ORB.
- [setRefCon](iofirewiresbp2orb/1813244-setrefcon.md)
  Sets the ORB refCon.
- [setRefCon64](iofirewiresbp2orb/1813262-setrefcon64.md)
  Sets the ORB refCon as a 64 bit value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2orb/1813162-setcommandbuffersasranges64)*