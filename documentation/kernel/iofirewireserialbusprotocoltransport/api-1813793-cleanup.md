# cleanUp

**Framework**: Kernel  
**Kind**: instm

cleanUp is called to tear down IOFireWireSerialBusProtocolTransport.

## Declaration

```cpp
virtual void cleanUp (
 void );
```

## Overview

cleanUp is called when we receive a kIOFWMessageServiceIsRequestingClose message or if we fail our initialization.

## See Also

### Miscellaneous
- [AbortSCSICommand](./api-1813790-abortscsicommand.md)
  This method is intended to abort an in progress SCSI Task.
- [AllocateResources](./api-1813792-allocateresources.md)
  Allocate Resources.
- [CoalesceSenseData](./api-1813795-coalescesensedata.md)
  CoalesceSenseData convert a SBP-2 status block into a SPC-2 sense block.
- [CommandORBAccessor](./api-1813797-commandorbaccessor.md)
  accessor function for fORB.
- [CompleteSCSITask](./api-1813798-completescsitask.md)
  This qualifies and sets appropriate data then calls CommandCompleted.
- [CriticalOrbSubmission](./api-1813800-criticalorbsubmission.md)
  xxx.
- [DeallocateResources](./api-1813802-deallocateresources.md)
  Deallocate Resources.
- [finalize](./api-1813804-finalize.md)
  See IOService for discussion.
- [free](./api-1813806-free.md)
- [HandleProtocolServiceFeature](./api-1813808-handleprotocolservicefeature.md)
  Handle specified feature supported by the protocol layer.
- [init](./api-1813809-init.md)
  See IOService for discussion.
- [IsProtocolServiceSupported](./api-1813810-isprotocolservicesupported.md)
  Determine is specified feature is supported by the protocol layer.
- [LoginCompletion](./api-1813811-logincompletion.md)
  Completion routine for login complete.
- [LogoutCompletion](./api-1813812-logoutcompletion.md)
  Completion routine for logout complete.
- [LunResetComplete](./api-1813813-lunresetcomplete.md)
  Callback to submit Fetch Agent Reset.
- [SBP2LoginAccessor](./api-1813814-sbp2loginaccessor.md)
  accessor function for fLogin.
- [SendSCSICommand](./api-1813815-sendscsicommand.md)
  Prepare and send a SCSI command to the device.
- [SetCommandBuffers](./api-1813816-setcommandbuffers.md)
  Method to set orb's buffers.
- [SetValidAutoSenseData](./api-1813817-setvalidautosensedata.md)
  Set the auto sense data that was returned for a given SCSI Task.
- [start](./api-1813818-start.md)
- [StatusNotify](./api-1813819-statusnotify.md)
  This is our handler for status.
- [UnsolicitedStatusNotify](./api-1813820-unsolicitedstatusnotify.md)
  This is our handler for unsolicited status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireserialbusprotocoltransport/1813793-cleanup)*