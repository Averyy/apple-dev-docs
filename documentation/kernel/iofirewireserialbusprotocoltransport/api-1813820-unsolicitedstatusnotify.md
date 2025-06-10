# UnsolicitedStatusNotify

**Framework**: Kernel  
**Kind**: instm

This is our handler for unsolicited status.

## Declaration

```swift
virtual void UnsolicitedStatusNotify (
 FWSBP2NotifyParamsPtr params );
```

#### Overview

After we have parsed and handled the unsolicited status we call enableUnsolicitedStatus. See IOFireWireSBP2Lib.h for details regarding the enableUnsolicitedStatus method.

## See Also

- [AbortSCSICommand](iofirewireserialbusprotocoltransport/1813790-abortscsicommand.md)
  This method is intended to abort an in progress SCSI Task.
- [AllocateResources](iofirewireserialbusprotocoltransport/1813792-allocateresources.md)
  Allocate Resources.
- [cleanUp](iofirewireserialbusprotocoltransport/1813793-cleanup.md)
  cleanUp is called to tear down IOFireWireSerialBusProtocolTransport.
- [CoalesceSenseData](iofirewireserialbusprotocoltransport/1813795-coalescesensedata.md)
  CoalesceSenseData convert a SBP-2 status block into a SPC-2 sense block.
- [CommandORBAccessor](iofirewireserialbusprotocoltransport/1813797-commandorbaccessor.md)
  accessor function for fORB.
- [CompleteSCSITask](iofirewireserialbusprotocoltransport/1813798-completescsitask.md)
  This qualifies and sets appropriate data then calls CommandCompleted.
- [CriticalOrbSubmission](iofirewireserialbusprotocoltransport/1813800-criticalorbsubmission.md)
  xxx.
- [DeallocateResources](iofirewireserialbusprotocoltransport/1813802-deallocateresources.md)
  Deallocate Resources.
- [finalize](iofirewireserialbusprotocoltransport/1813804-finalize.md)
  See IOService for discussion.
- [free](iofirewireserialbusprotocoltransport/1813806-free.md)
- [HandleProtocolServiceFeature](iofirewireserialbusprotocoltransport/1813808-handleprotocolservicefeature.md)
  Handle specified feature supported by the protocol layer.
- [init](iofirewireserialbusprotocoltransport/1813809-init.md)
  See IOService for discussion.
- [IsProtocolServiceSupported](iofirewireserialbusprotocoltransport/1813810-isprotocolservicesupported.md)
  Determine is specified feature is supported by the protocol layer.
- [LoginCompletion](iofirewireserialbusprotocoltransport/1813811-logincompletion.md)
  Completion routine for login complete.
- [LogoutCompletion](iofirewireserialbusprotocoltransport/1813812-logoutcompletion.md)
  Completion routine for logout complete.
- [LunResetComplete](iofirewireserialbusprotocoltransport/1813813-lunresetcomplete.md)
  Callback to submit Fetch Agent Reset.
- [SBP2LoginAccessor](iofirewireserialbusprotocoltransport/1813814-sbp2loginaccessor.md)
  accessor function for fLogin.
- [SendSCSICommand](iofirewireserialbusprotocoltransport/1813815-sendscsicommand.md)
  Prepare and send a SCSI command to the device.
- [SetCommandBuffers](iofirewireserialbusprotocoltransport/1813816-setcommandbuffers.md)
  Method to set orb's buffers.
- [SetValidAutoSenseData](iofirewireserialbusprotocoltransport/1813817-setvalidautosensedata.md)
  Set the auto sense data that was returned for a given SCSI Task.
- [start](iofirewireserialbusprotocoltransport/1813818-start.md)
- [StatusNotify](iofirewireserialbusprotocoltransport/1813819-statusnotify.md)
  This is our handler for status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireserialbusprotocoltransport/1813820-unsolicitedstatusnotify)*