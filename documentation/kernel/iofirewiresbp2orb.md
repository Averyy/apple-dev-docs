# IOFireWireSBP2ORB

**Framework**: Kernel  
**Kind**: cl

Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2Login.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireSBP2ORB : IOCommand
```

#### Overview

## Topics

### Miscellaneous
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
### Instance Methods
- [- allocateORB](iofirewiresbp2orb/1569110-allocateorb.md)
- [- allocatePageTable](iofirewiresbp2orb/1569092-allocatepagetable.md)
- [- allocateResources](iofirewiresbp2orb/1569070-allocateresources.md)
- [- allocateTimer](iofirewiresbp2orb/1569083-allocatetimer.md)
- [- calculateTransferSizeLog](iofirewiresbp2orb/1569082-calculatetransfersizelog.md)
- [- cancelTimer](iofirewiresbp2orb/1569103-canceltimer.md)
- [- completeBufferAddressSpace](iofirewiresbp2orb/1569080-completebufferaddressspace.md)
- [- deallocateBufferAddressSpace](iofirewiresbp2orb/1569115-deallocatebufferaddressspace.md)
- [- deallocateORB](iofirewiresbp2orb/1569130-deallocateorb.md)
- [- deallocatePageTable](iofirewiresbp2orb/1569108-deallocatepagetable.md)
- [- deallocateTimer](iofirewiresbp2orb/1569124-deallocatetimer.md)
- [- free](iofirewiresbp2orb/1569089-free.md)
- [- getCommandBufferDescriptor](iofirewiresbp2orb/1569072-getcommandbufferdescriptor.md)
- [- getCommandFlags](iofirewiresbp2orb/1569085-getcommandflags.md)
- [- getCommandGeneration](iofirewiresbp2orb/1569081-getcommandgeneration.md)
- [- getCommandTimeout](iofirewiresbp2orb/1569127-getcommandtimeout.md)
- [- getFetchAgentWriteRetries](iofirewiresbp2orb/1569084-getfetchagentwriteretries.md)
- [- getFetchAgentWriteRetryInterval](iofirewiresbp2orb/1569078-getfetchagentwriteretryinterval.md)
- [- getFireWireLUN](iofirewiresbp2orb/1569116-getfirewirelun.md)
- [- getFireWireUnit](iofirewiresbp2orb/1569093-getfirewireunit.md)
- [- getLogin](iofirewiresbp2orb/1569090-getlogin.md)
- [- getMaxPayloadSize](iofirewiresbp2orb/1569132-getmaxpayloadsize.md)
- [- getMetaClass](iofirewiresbp2orb/1569067-getmetaclass.md)
- [- getORBAddress](iofirewiresbp2orb/1569079-getorbaddress.md)
- [- getRefCon](iofirewiresbp2orb/1569107-getrefcon.md)
- [- getRefCon64](iofirewiresbp2orb/1569117-getrefcon64.md)
- [- initWithLogin](iofirewiresbp2orb/1569131-initwithlogin.md)
- [- isAppended](iofirewiresbp2orb/1569126-isappended.md)
- [- isTimerSet](iofirewiresbp2orb/1569099-istimerset.md)
- [- orbTimeout](iofirewiresbp2orb/1569113-orbtimeout.md)
- [- prepareBufferAddressSpace](iofirewiresbp2orb/1569066-preparebufferaddressspace.md)
- [- prepareFastStartPacket](iofirewiresbp2orb/1569112-preparefaststartpacket.md)
- [- prepareORBForExecution](iofirewiresbp2orb/1569097-prepareorbforexecution.md)
- [- release](iofirewiresbp2orb/1569091-release.md)
- [- releaseCommandBuffers](iofirewiresbp2orb/1569095-releasecommandbuffers.md)
- [- removeORB](iofirewiresbp2orb/1569119-removeorb.md)
- [- sendTimeoutNotification](iofirewiresbp2orb/1569071-sendtimeoutnotification.md)
- [- setBufferConstraints](iofirewiresbp2orb/1569073-setbufferconstraints.md)
- [- setCommandBlock](iofirewiresbp2orb/1569087-setcommandblock.md)
- [- setCommandBlock](iofirewiresbp2orb/3516727-setcommandblock.md)
- [- setCommandBuffers](iofirewiresbp2orb/1569101-setcommandbuffers.md)
- [- setCommandBuffersAsRanges](iofirewiresbp2orb/1569076-setcommandbuffersasranges.md)
- [- setCommandBuffersAsRanges64](iofirewiresbp2orb/1569068-setcommandbuffersasranges64.md)
- [- setCommandFlags](iofirewiresbp2orb/1569077-setcommandflags.md)
- [- setCommandGeneration](iofirewiresbp2orb/1569122-setcommandgeneration.md)
- [- setCommandTimeout](iofirewiresbp2orb/1569065-setcommandtimeout.md)
- [- setFetchAgentWriteRetries](iofirewiresbp2orb/1569074-setfetchagentwriteretries.md)
- [- setFetchAgentWriteRetryInterval](iofirewiresbp2orb/1569069-setfetchagentwriteretryinterval.md)
- [- setIsAppended](iofirewiresbp2orb/1569114-setisappended.md)
- [- setMaxPayloadSize](iofirewiresbp2orb/1569123-setmaxpayloadsize.md)
- [- setNextORBAddress](iofirewiresbp2orb/1569109-setnextorbaddress.md)
- [- setRefCon](iofirewiresbp2orb/1569088-setrefcon.md)
- [- setRefCon64](iofirewiresbp2orb/1569094-setrefcon64.md)
- [- setToDummy](iofirewiresbp2orb/1569129-settodummy.md)
- [- startTimer](iofirewiresbp2orb/1569098-starttimer.md)
### Type Methods
- [+ orbTimeoutStatic](iofirewiresbp2orb/1569125-orbtimeoutstatic.md)

## Relationships

### Inherits From
- [IOCommand](iocommand.md)

## See Also

- [IOFireWireSBP2Login](iofirewiresbp2login.md)
  Supplies the login maintenance and Normal Command ORB execution portions of the API.
- [IOFireWireSBP2ManagementORB](iofirewiresbp2managementorb.md)
  Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LUN interface.
- [FWSBP2FetchAgentWriteCallback](fwsbp2fetchagentwritecallback.md)
- [FWSBP2LoginCallback](fwsbp2logincallback.md)
- [FWSBP2LoginCompleteParams](fwsbp2logincompleteparams.md)
- [FWSBP2LoginCompleteParamsPtr](fwsbp2logincompleteparamsptr.md)
- [FWSBP2LoginResponse](fwsbp2loginresponse.md)
- [FWSBP2LoginResponsePtr](fwsbp2loginresponseptr.md)
- [FWSBP2LogoutCallback](fwsbp2logoutcallback.md)
- [FWSBP2LogoutCompleteParams](fwsbp2logoutcompleteparams.md)
- [FWSBP2LogoutCompleteParamsPtr](fwsbp2logoutcompleteparamsptr.md)
- [FWSBP2ManagementCallback](fwsbp2managementcallback.md)
- [FWSBP2NotifyCallback](fwsbp2notifycallback.md)
- [FWSBP2NotifyParams](fwsbp2notifyparams.md)
- [FWSBP2NotifyParamsPtr](fwsbp2notifyparamsptr.md)
- [FWSBP2ReconnectParams](fwsbp2reconnectparams.md)
- [FWSBP2ReconnectParamsPtr](fwsbp2reconnectparamsptr.md)
- [FWSBP2StatusBlock](fwsbp2statusblock.md)
- [FWSBP2StatusCallback](fwsbp2statuscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2orb)*