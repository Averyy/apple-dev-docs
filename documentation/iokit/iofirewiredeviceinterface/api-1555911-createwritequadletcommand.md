# CreateWriteQuadletCommand

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Create a quadlet write command object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOFireWireLibCommandRef (*CreateWriteQuadletCommand)(IOFireWireLibDeviceRef self, io_object_t device, const FWAddress *addr, UInt32 quads[], UInt32 numQuads, IOFireWireLibCommandCallback callback, Boolean failOnReset, UInt32 generation, void *inRefCon, REFIID iid);
```

## Return Value

An IOFireWireLibCommandRef interface. See IOFireWireLibCommandRef.

## Parameters

- `self`: The device interface to use.
- `device`: The service (representing an attached FireWire device) to which to write. For 48-bit, device relative addressing, pass the service used to create the device interface. This can be obtained by calling GetDevice(). For 64-bit absolute addressing, pass 0. Other values are unsupported. Setting the callback value to nil defaults to synchronous execution.
- `addr`: Command target address
- `quads`: An array of quadlets containing quadlets to be written
- `numQuads`: Number of quadlets to write
- `callback`: Command completion callback. Setting the callback value to nil defaults to synchronous execution.
- `failOnReset`: Pass true if the command should only be executed during the FireWire bus generation specified in 'generation'. Pass false to ignore the generation parameter. The generation can be obtained by calling GetBusGeneration(). Must be 'true' when using 64-bit addressing.
- `generation`: The FireWire bus generation during which the command should be executed. Ignored if failOnReset is false. Must be a valid generation number when using 64-bit absolute addressing.

## See Also

### Miscellaneous
- [AddCallbackDispatcherToRunLoop](./api-1555795-addcallbackdispatchertorunloop.md)
  Installs the proper run loop event source to allow callbacks to function. This method must be called before callback notifications for this interface or any interfaces created using this interface can function.
- [AddCallbackDispatcherToRunLoopForMode](./api-1556024-addcallbackdispatchertorunloopfo.md)
  Add a run loop event source to allow IOFireWireLib callbacks to function.
- [AddIsochCallbackDispatcherToRunLoop(IOFireWireLibDeviceRef, CFRunLoopRef)](./addisochcallbackdispatchertorunloop_iofirewirelibdeviceref_cfrunloopref.md)
  This function adds an event source for the isochronous callback dispatcher to the specified CFRunLoop. Isochronous related callbacks will not function before this function is called. This functions is similar to AddCallbackDispatcherToRunLoop. The passed CFRunLoop can be different from that passed to AddCallbackDispatcherToRunLoop.
- [AddIsochCallbackDispatcherToRunLoop(IOFireWireLibDeviceRef, CFRunLoopRef, CFStringRef)](./addisochcallbackdispatchertorunloop_iofirewirelibdeviceref_cfrunloopref_cfstringref.md)
  Add a run loop event source to allow IOFireWireLib isoch callbacks to function.
- [AddIsochCallbackDispatcherToRunLoopForMode](./api-1556060-addisochcallbackdispatchertorunl.md)
  Add a run loop event source to allow IOFireWireLib isoch callbacks to function.
- [AllocateIRMBandwidthInGeneration](./api-1555639-allocateirmbandwidthingeneration.md)
  Attempt to allocate some isochronous bandwidth from the IRM
- [AllocateIRMChannelInGeneration](./api-1556022-allocateirmchannelingeneration.md)
  Attempt to allocate an isochronous channel from the IRM
- [BusReset](./api-1555967-busreset.md)
  Cause a bus reset
- [ClientCommandIsComplete](./api-1555827-clientcommandiscomplete.md)
  This function must be called from callback routines once they have completed processing a callback. This function only applies to callbacks which take an IOFireWireLibDeviceRef (i.e. bus reset), parameter.
- [ClipMaxRec2K](./api-1555805-clipmaxrec2k.md)
- [Close](./api-1555865-close.md)
  Release exclusive access to the device
- [CompareSwap](./api-1555677-compareswap.md)
  Perform synchronous lock operation
- [CompareSwap64](./api-1556045-compareswap64.md)
  Perform synchronous lock operation
- [CreateAsyncStreamCommand](./api-1555791-createasyncstreamcommand.md)
  Create a command object for sending Async Stream packets
- [CreateAsyncStreamListener](./api-1556037-createasyncstreamlistener.md)
  Creates a async stream listener object and returns an interface to it.
- [CreateCompareSwapCommand](./api-1555628-createcompareswapcommand.md)
  Create a quadlet compare/swap command object.
- [CreateCompareSwapCommand64](./api-1555976-createcompareswapcommand64.md)
  Create a quadlet compare/swap command object and initialize it with 64-bit values.
- [CreateConfigDirectoryWithIOObject](./api-1555662-createconfigdirectorywithioobjec.md)
  This function can be used to create a config directory object and a corresponding interface from an opaque IOObject reference. Some configuration directory interface methods may return an io_object_t instead of an IOFireWireLibConfigDirectoryRef. Use this function to obtain an IOFireWireLibConfigDirectoryRef from an io_object_t.
- [CreateDCLCommandPool](./api-1556103-createdclcommandpool.md)
  Creates a command pool object and returns an interface to it. The command pool can be used to build DCL programs.
- [CreateInitialUnitsPseudoAddressSpace](./api-1555616-createinitialunitspseudoaddresss.md)
  Creates a pseudo address space in initial units space.
- [CreateIRMAllocation](./api-1555779-createirmallocation.md)
  Attempt to create an IRM allocation that persists accross bus-resets.
- [CreateIsochChannel](./api-1555848-createisochchannel.md)
  Creates an isochronous channel object and returns an interface to it. An isochronous channel object is an abstract entity used to represent a FireWire isochronous channel.
- [CreateLocalIsochPort](./api-1555942-createlocalisochport.md)
  Creates a local isochronous port object and returns an interface to it. A local isochronous port object is an abstract entity used to represent a talking or listening endpoint in the local machine.
- [CreateLocalIsochPortWithOptions](./api-1555850-createlocalisochportwithoptions.md)
  Create a local isoch port
- [CreateLocalUnitDirectory](./api-1555879-createlocalunitdirectory.md)
  Creates a local unit directory object and returns an interface to it. An instance of a unit directory object corresponds to an instance of a unit directory in the local machine's configuration ROM.
- [CreateNuDCLPool](./api-1556069-createnudclpool.md)
- [CreatePHYCommand](./api-1555711-createphycommand.md)
  Create a command object for sending a PHY packet
- [CreatePHYPacketListener](./api-1555737-createphypacketlistener.md)
  Create a listener object for receiving PHY packets
- [CreatePhysicalAddressSpace](./api-1555762-createphysicaladdressspace.md)
  Creates a physical address space object and returns an interface to it. This will create a physical address space on the local machine.
- [CreatePseudoAddressSpace](./api-1555763-createpseudoaddressspace.md)
  Creates a pseudo address space object and returns an interface to it. This will create a pseudo address space (software-backed) on the local machine.
- [CreateReadCommand](./api-1555878-createreadcommand.md)
  Create a block read command object.
- [CreateReadQuadletCommand](./api-1555734-createreadquadletcommand.md)
  Create a quadlet read command object.
- [CreateRemoteIsochPort](./api-1555591-createremoteisochport.md)
  Creates a remote isochronous port object and returns an interface to it. A remote isochronous port object is an abstract entity used to represent a remote talker or listener device on an isochronous channel.
- [CreateVectorCommand](./api-1555689-createvectorcommand.md)
  Create a vector command object.
- [CreateWriteCommand](./api-1556011-createwritecommand.md)
  Create a block write command object.
- [FireBugMsg](./api-1556115-firebugmsg.md)
- [FireLog](./api-1555664-firelog.md)
  Logs string to in-kernel debug buffer
- [GetBusCycleTime](./api-1555783-getbuscycletime.md)
  Get bus and cycle time.
- [GetBusGeneration](./api-1555685-getbusgeneration.md)
  Get bus generation number.
- [GetConfigDirectory](./api-1555703-getconfigdirectory.md)
  Creates a config directory object and returns an interface to it. The created config directory object represents the config directory in the remote device or unit to which the creating device interface is attached.
- [GetCycleTime](./api-1556046-getcycletime.md)
  Get bus cycle time.
- [GetCycleTimeAndUpTime](./api-1556114-getcycletimeanduptime.md)
  Get bus cycle time and cpu uptime.
- [GetDebugProperty](./api-1555661-getdebugproperty.md)
- [GetDevice](./api-1556065-getdevice.md)
  Get the IOKit service to which this interface is connected.
- [GetGenerationAndNodeID](./api-1555619-getgenerationandnodeid.md)
  (Obsolete) Get bus generation and remote device node ID.
- [GetIRMNodeID](./api-1555834-getirmnodeid.md)
- [GetIsochAsyncPort](./api-1556053-getisochasyncport.md)
  Returns the notification port used for async and isoch callbacks
- [GetLocalNodeID](./api-1555846-getlocalnodeid.md)
  (Obsolete) Get local node ID.
- [GetLocalNodeIDWithGeneration](./api-1556009-getlocalnodeidwithgeneration.md)
  Get node ID of local machine.
- [GetRefCon](./api-1555727-getrefcon.md)
  Get user reference value set on this interface
- [GetRemoteNodeID](./api-1555732-getremotenodeid.md)
  Get node ID of device to which this interface is attached.
- [GetResetTime](./api-1555894-getresettime.md)
  Get time since last bus reset.
- [GetSessionRef](./api-1555977-getsessionref.md)
- [GetSpeedBetweenNodes](./api-1556026-getspeedbetweennodes.md)
  Get the maximum transfer speed between nodes 'srcNodeID' and 'destNodeID'.
- [GetSpeedToNode](./api-1555893-getspeedtonode.md)
  Get maximum transfer speed to device to which this interface is attached.
- [InterfaceIsInited](./api-1555816-interfaceisinited.md)
  Determine whether interface has been properly inited.
- [NotificationIsOn](./api-1555632-notificationison.md)
  Determine whether callback notifications for this interface are currently active
- [Open](./api-1555622-open.md)
  Open the connected device for exclusive access. When you have the device open using this method, all accesses by other clients of this device will be denied until Close() is called.
- [OpenWithSessionRef](./api-1555885-openwithsessionref.md)
  An open function which allows this interface to have access to the device when already opened. The service which has already opened the device must be able to provide an IOFireWireSessionRef.
- [PrintDCLProgram](./api-1555718-printdclprogram.md)
  Walk a DCL program linked list and print its contents
- [Read](./api-1556023-read.md)
  Perform synchronous block read
- [ReadQuadlet](./api-1555961-readquadlet.md)
  Perform synchronous quadlet read
- [ReleaseIRMBandwidthInGeneration](./api-1555755-releaseirmbandwidthingeneration.md)
  Attempt to release some isochronous bandwidth from the IRM
- [ReleaseIRMChannelInGeneration](./api-1555975-releaseirmchannelingeneration.md)
  Attempt to release an isochronous channel from the IRM
- [RemoveCallbackDispatcherFromRunLoop](./api-1555798-removecallbackdispatcherfromrunl.md)
  Reverses the effects of AddCallbackDispatcherToRunLoop(). This method removes the run loop event source that was added to the specified run loop preventing any future callbacks from being called
- [RemoveIsochCallbackDispatcherFromRunLoop](./api-1556054-removeisochcallbackdispatcherfro.md)
  Removes an IOFireWireLib-added run loop event source.
- [Seize](./api-1555960-seize.md)
  Seize control of device/unit
- [SetBusResetDoneHandler](./api-1555870-setbusresetdonehandler.md)
  Sets the callback that should be called after a bus reset has occurred and reconfiguration of the bus has been completed. This function will only be called once per bus reset.
- [SetBusResetHandler](./api-1555938-setbusresethandler.md)
  Sets the callback that should be called when a bus reset occurs. Note that this callback can be called multiple times before the bus reset done handler is called. (f.ex., multiple bus resets might occur before bus reconfiguration has completed.)
- [SetRefCon](./api-1555746-setrefcon.md)
  Set user reference value on this interface
- [TurnOffNotification](./api-1555902-turnoffnotification.md)
  Deactivates and callbacks specified for this device interface. Reverses the effects of TurnOnNotification()
- [TurnOnNotification](./api-1556081-turnonnotification.md)
  Activates any callbacks specified for this device interface. Only works after AddCallbackDispatcherToRunLoop has been called. See also AddIsochCallbackDispatcherToRunLoop().
- [Write](./api-1556028-write.md)
  Perform synchronous block write
- [WriteQuadlet](./api-1555743-writequadlet.md)
  Perform synchronous quadlet write


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiredeviceinterface/1555911-createwritequadletcommand)*