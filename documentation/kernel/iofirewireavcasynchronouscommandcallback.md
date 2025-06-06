# IOFireWireAVCAsynchronousCommandCallback

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*IOFireWireAVCAsynchronousCommandCallback)(void *pRefCon, IOFireWireAVCAsynchronousCommand *pCommandObject);
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcasynchronouscommandcallback)*