# SendSCSICommand

**Framework**: Kernel  
**Kind**: instm

Prepare and send a SCSI command to the device.

## Declaration

```swift
virtual bool SendSCSICommand (
 SCSITaskIdentifier request, 
 SCSIServiceResponse *serviceResponse, 
 SCSITaskStatus *taskStatus );
```

#### Return_value

If the command was sent to the device and is pending completion, the subclass should return true and return back the kSCSIServiceResponse_Request_In_Process response. If the command completes immediately with an error, the subclass will return true and return back the appropriate status. If the subclass is currently processing all the commands it can, the subclass will return false and the command will be resent next time CommandCompleted is called.

#### Overview

The incoming SCSITaskIdentifier gets turned into a IOFireWireSBP2ORB and is submitted to the SBP2 layer. See IOSCSIProtocolServices.h for more details regarding SendSCSICommand. Also see IOFireWireSBP2Lib.h for details regarding the IOFireWireSBP2ORB structure and the submitORB method.

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
- [SetCommandBuffers](iofirewireserialbusprotocoltransport/1813816-setcommandbuffers.md)
  Method to set orb's buffers.
- [SetValidAutoSenseData](iofirewireserialbusprotocoltransport/1813817-setvalidautosensedata.md)
  Set the auto sense data that was returned for a given SCSI Task.
- [start](iofirewireserialbusprotocoltransport/1813818-start.md)
- [StatusNotify](iofirewireserialbusprotocoltransport/1813819-statusnotify.md)
  This is our handler for status.
- [UnsolicitedStatusNotify](iofirewireserialbusprotocoltransport/1813820-unsolicitedstatusnotify.md)
  This is our handler for unsolicited status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireserialbusprotocoltransport/1813815-sendscsicommand)*