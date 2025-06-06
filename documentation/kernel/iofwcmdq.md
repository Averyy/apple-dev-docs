# IOFWCmdQ

**Framework**: Kernel  
**Kind**: tag

Structure for head of a queue of IOFWCommands

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct IOFWCmdQ {
    ...
};
```

## Topics

### Fields
- [fHead](iofwcmdq/1563782-fhead.md)
  Points to the head of the queue, or NULL if queue is empty
- [fTail](iofwcmdq/1563843-ftail.md)
  Points to the tail of the queue, or NULL if queue is empty
- [headChanged](iofwcmdq/1813007-headchanged.md)
  called when head command is changed, or the command itself changes state.

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
- [FWWriteCallback](fwwritecallback.md)
  Callback called when a write request packet is received for a 'virtual' firewire address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwcmdq)*