# setCommandFlags

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets configuration flags for the ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setCommandFlags)(void *self, UInt32 flags);
```

#### Discussion

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

- `self`: Pointer to IOFireWireSBP2LibORBInterface.
- `flags`: The flags to be set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590533-setcommandflags)*