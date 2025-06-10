# setCommandFlags

**Framework**: Kernel  
**Kind**: instm

Sets configuration flags for the ORB.

## Declaration

```swift
virtual void setCommandFlags(
 UInt32flags );
```

#### Overview

Sets the configuration flags for the ORB. These can be any of the following:

kFWSBP2CommandCompleteNotify - Set the notify bit as specified in SBP2 standard. Set to receive completion/timeout notification on this ORB. You almost always want to set this.

kFWSBP2CommandTransferDataFromTarget - Transfer direction as specified in SBP2 standard. Set if data is to be written by the device into the host's memory.

kFWSBP2CommandImmediate - Immediate Append. ORB address will be written to fetch agent and not chained. It is only legal to have one immediate ORB in progress at a time.

kFWSBP2CommandNormalORB - ORB format 0 - Format specified by SBP2 standard. Set this for most ORBs.

kFWSBP2CommandReservedORB - ORB format 1 - Format reserved by SBP2 standard for future standardization.

kFWSBP2CommandVendorORB - ORB format 2 - Format specified by SBP2 standard for vendor dependent ORBs.

kFWSBP2CommandDummyORB - ORB format 3 - Format specified by SBP2 standard for placeholder ORBs.

kFWSBP2CommandCheckGeneration - If set upon submitORB, the ORB will only be appended if generation set with setCommandGeneration() matches the current generation. Pretty much all SBP2 drivers need sophisticated logic to track login state, so this is generally not used.

kFWSBP2CommandFixedSize - Do not allocate more memory for page table if needed. If there is not enough space in the currently allocated page table, the setCommandBuffers call will fail. This is important to set if your device is the backing store, as we don't want to cause memory allocations on the paging path.

kFWSBP2CommandVirtualORBs - Normally ORBs are backed by physical address spaces. Setting this flag makes this ORB backed by a pseudo address space. This can make ORBs easier to see in a bus trace. Virtual ORBs will have an address in the form of ffcX.XXXX.0000.0000. Pseudo address space backed ORBs are slower, so you won't want to set for deployment builds.

## Parameters

- `flags`: The flags to be set.

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
- [setCommandBuffersAsRanges64](iofirewiresbp2orb/1813162-setcommandbuffersasranges64.md)
  Creates a page table from a list of 64 bit ranges.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2orb/1813178-setcommandflags)*