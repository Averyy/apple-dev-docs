# IOFireWirePseudoAddressSpaceReadHandler

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

This callback is called to handle read requests to pseudo address spaces. This function should fill in the specified area in the pseudo address space backing store and call ClientCommandIsComplete with the specified command ID

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef UInt32 (*IOFireWirePseudoAddressSpaceReadHandler)(IOFireWireLibPseudoAddressSpaceRef addressSpace, FWClientCommandID commandID, UInt32 packetLen, UInt32 packetOffset, UInt16 srcNodeID, UInt32 destAddressHi, UInt32 destAddressLo, void *refCon);
```

## Parameters

- `addressSpace`: The address space to which the request is being made
- `commandID`: An FWClientCommandID which should be passed to ClientCommandIsComplete when the buffer has been filled in
- `packetLen`: number of bytes requested
- `packetOffset`: number of bytes from beginning of address space backing store
- `srcNodeID`: nodeID of the requester
- `destAddressHi`: high 16 bits of destination address on this computer
- `destAddressLo`: low 32 bits of destination address on this computer
- `refCon`: user specified reference number passed in when the address space was created

## See Also

### Callbacks
- [IOFireWireBusResetDoneHandler](./iofirewirebusresetdonehandler.md)
  Called when a bus reset has occured and FireWire has completed configuring the bus.
- [IOFireWireBusResetHandler](./iofirewirebusresethandler.md)
  Called when a bus reset has occured, but before FireWire has completed configuring the bus.
- [IOFireWireLibCommandCallback](./iofirewirelibcommandcallback.md)
  Callback called when an asynchronous command has completed executing
- [IOFireWireLibIRMAllocationLostNotificationProc](./iofirewirelibirmallocationlostnotificationproc.md)
  Callback called when an IOFireWireLibIRMAllocationRef fails to reclaim IRM resources after a bus-reset
- [IOFireWireLibPHYPacketCallback](./iofirewirelibphypacketcallback.md)
  Callback called to handle incoming PHY packets
- [IOFireWireLibPHYPacketSkippedCallback](./iofirewirelibphypacketskippedcallback.md)
  Callback called when incoming packets have been dropped from the internal queue
- [IOFireWirePseudoAddressSpaceSkippedPacketHandler](./iofirewirepseudoaddressspaceskippedpackethandler.md)
  Callback called when incoming packets have been dropped from the internal queue
- [IOFireWirePseudoAddressSpaceWriteHandler](./iofirewirepseudoaddressspacewritehandler.md)
  Callback called to handle write requests to a pseudo address space.
- [IOFWAsyncStreamListenerHandler](./iofwasyncstreamlistenerhandler.md)
  Callback called to handle Async Stream packets.
- [IOFWAsyncStreamListenerSkippedPacketHandler](./iofwasyncstreamlistenerskippedpackethandler.md)
  Callback called when incoming packets have been dropped from the internal queue


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirepseudoaddressspacereadhandler)*