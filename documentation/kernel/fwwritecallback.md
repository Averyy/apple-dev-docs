# FWWriteCallback

**Framework**: Kernel  
**Kind**: tdef

Callback called when a write request packet is received for a 'virtual' firewire address.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef UInt32 (*FWWriteCallback)(void *refcon, UInt16 nodeID, IOFWSpeed & speed, FWAddress addr, UInt32 len, const void *buf, IOFWRequestRefCon requestRefcon);
```

#### Return_value

return: kFWResponseComplete = 0, OK kFWResponseConflictError = 4, Resource conflict, may retry kFWResponseDataError = 5, Data not available kFWResponseTypeError = 6, Operation not supported kFWResponseAddressError = 7 Address not valid in target device

## Parameters

- `device`: is the node originating the request
- `speed`: is the FireWire speed of the request, update it if you need to control the speed of the reply, otherwise the response will be the same speed.
- `addr`: is the address the device is requesting to write to
- `len`: is the number of bytes to write
- `buf`: contains the packet data
- `requestRefcon`: refcon Can be queried for extra info about the request, using IOFireWireController::isLockRequest(), isQuadRequest()

## See Also

- [IOFWDuplicateGUIDRec](iofwduplicateguidrec.md)
- [IOFWARxReqIntCompleteHandler](iofwarxreqintcompletehandler.md)
- [IOFWAVCAsyncCommandState](iofwavcasynccommandstate.md)
- [IOFWAVCPlugTypes](iofwavcplugtypes.md)
- [IOFWAVCProtocolUserClientAsyncCommandCodes](iofwavcprotocoluserclientasynccommandcodes.md)
- [IOFWAVCProtocolUserClientCommandCodes](iofwavcprotocoluserclientcommandcodes.md)
- [IOFWAVCSubunitPlugMessages](iofwavcsubunitplugmessages.md)
- [IOFWAVCUserClientAsyncCommandCodes](iofwavcuserclientasynccommandcodes.md)
- [IOFWAVCUserClientCommandCodes](iofwavcuserclientcommandcodes.md)
- [IOFWCmdQ](iofwcmdq.md)
  Structure for head of a queue of IOFWCommands
- [IOFWDCLNotificationType](iofwdclnotificationtype.md)
- [IOFWIsochPortOptions](iofwisochportoptions.md)
- [IOFWIsochResourceFlags](iofwisochresourceflags.md)
- [IOFWNodeScan](iofwnodescan.md)
- [IOFWPhysicalAccessMode](iofwphysicalaccessmode.md)
- [IOFWReadFlags](iofwreadflags.md)
- [IOFWRequestRefCon](iofwrequestrefcon.md)
- [IOFWSBP2UserClientCommandCodes](iofwsbp2userclientcommandcodes.md)
- [IOFWSecurityMode](iofwsecuritymode.md)
- [IOFWSpeed](iofwspeed.md)
- [IOFWWriteFlags](iofwwriteflags.md)
- [IOFireWireAVCAsynchronousCommandCallback](iofirewireavcasynchronouscommandcallback.md)
- [IOFireWireAVCSubunitPlugHandlerCallback](iofirewireavcsubunitplughandlercallback.md)
- [IOFireWireAVCTargetCommandHandlerCallback](iofirewireavctargetcommandhandlercallback.md)
- [IOFireWirePCRCallback](iofirewirepcrcallback.md)
  Callback called after a successful lock transaction to a plug.
- [IOFireWireSessionRef](iofirewiresessionref.md)
- [IOAVCCommandResponse](ioavccommandresponse.md)
- [IOAVCFrameFields](ioavcframefields.md)
- [IOAVCOpcodes](ioavcopcodes.md)
- [IOAVCUnitTypes](ioavcunittypes.md)
- [FWAddress](fwaddress.md)
- [FWAddressPtr](fwaddressptr.md)
- [FWAsyncPHYCallback](fwasyncphycallback.md)
- [FWAsyncStreamCallback](fwasyncstreamcallback.md)
- [FWAsyncStreamReceiveCallback](fwasyncstreamreceivecallback.md)
- [FWBusCallback](fwbuscallback.md)
- [FWClientCommandID](fwclientcommandid.md)
- [FWDeviceCallback](fwdevicecallback.md)
- [FWIsochChannelForceStopNotificationProc](fwisochchannelforcestopnotificationproc.md)
- [FWIsochChannelForceStopNotificationProcPtr](fwisochchannelforcestopnotificationprocptr.md)
- [FWMultiIsochReceiveListenerCallback](fwmultiisochreceivelistenercallback.md)
- [FWPHYPacketCallback](fwphypacketcallback.md)
- [FWReadCallback](fwreadcallback.md)
  Callback called when a read request packet is received for a 'virtual' firewire address.
- [FWSegment](fwsegment.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fwwritecallback)*