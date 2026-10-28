# IOFireWireSerialBusProtocolTransport

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

SCSI Protocol Driver Family for FireWire SBP2 Devices.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFireWireSerialBusProtocolTransport : IOSCSIProtocolServices
```

## Overview

IOFireWireSerialBusProtocolTransport contains all the bus specific support for FireWire SBP2 compliant devices. To add vendor specific features or workarounds you will sub-class the appropriate methods of this family.

## Topics

### Miscellaneous
- [AbortSCSICommand](./iofirewireserialbusprotocoltransport/api-1813790-abortscsicommand.md)
  This method is intended to abort an in progress SCSI Task.
- [AllocateResources](./iofirewireserialbusprotocoltransport/api-1813792-allocateresources.md)
  Allocate Resources.
- [cleanUp](./iofirewireserialbusprotocoltransport/api-1813793-cleanup.md)
  cleanUp is called to tear down IOFireWireSerialBusProtocolTransport.
- [CoalesceSenseData](./iofirewireserialbusprotocoltransport/api-1813795-coalescesensedata.md)
  CoalesceSenseData convert a SBP-2 status block into a SPC-2 sense block.
- [CommandORBAccessor](./iofirewireserialbusprotocoltransport/api-1813797-commandorbaccessor.md)
  accessor function for fORB.
- [CompleteSCSITask](./iofirewireserialbusprotocoltransport/api-1813798-completescsitask.md)
  This qualifies and sets appropriate data then calls CommandCompleted.
- [CriticalOrbSubmission](./iofirewireserialbusprotocoltransport/api-1813800-criticalorbsubmission.md)
  xxx.
- [DeallocateResources](./iofirewireserialbusprotocoltransport/api-1813802-deallocateresources.md)
  Deallocate Resources.
- [finalize](./iofirewireserialbusprotocoltransport/api-1813804-finalize.md)
  See IOService for discussion.
- [free](./iofirewireserialbusprotocoltransport/api-1813806-free.md)
- [HandleProtocolServiceFeature](./iofirewireserialbusprotocoltransport/api-1813808-handleprotocolservicefeature.md)
  Handle specified feature supported by the protocol layer.
- [init](./iofirewireserialbusprotocoltransport/api-1813809-init.md)
  See IOService for discussion.
- [IsProtocolServiceSupported](./iofirewireserialbusprotocoltransport/api-1813810-isprotocolservicesupported.md)
  Determine is specified feature is supported by the protocol layer.
- [LoginCompletion](./iofirewireserialbusprotocoltransport/api-1813811-logincompletion.md)
  Completion routine for login complete.
- [LogoutCompletion](./iofirewireserialbusprotocoltransport/api-1813812-logoutcompletion.md)
  Completion routine for logout complete.
- [LunResetComplete](./iofirewireserialbusprotocoltransport/api-1813813-lunresetcomplete.md)
  Callback to submit Fetch Agent Reset.
- [SBP2LoginAccessor](./iofirewireserialbusprotocoltransport/api-1813814-sbp2loginaccessor.md)
  accessor function for fLogin.
- [SendSCSICommand](./iofirewireserialbusprotocoltransport/api-1813815-sendscsicommand.md)
  Prepare and send a SCSI command to the device.
- [SetCommandBuffers](./iofirewireserialbusprotocoltransport/api-1813816-setcommandbuffers.md)
  Method to set orb's buffers.
- [SetValidAutoSenseData](./iofirewireserialbusprotocoltransport/api-1813817-setvalidautosensedata.md)
  Set the auto sense data that was returned for a given SCSI Task.
- [start](./iofirewireserialbusprotocoltransport/api-1813818-start.md)
- [StatusNotify](./iofirewireserialbusprotocoltransport/api-1813819-statusnotify.md)
  This is our handler for status.
- [UnsolicitedStatusNotify](./iofirewireserialbusprotocoltransport/api-1813820-unsolicitedstatusnotify.md)
  This is our handler for unsolicited status.
### DataTypes
- [SBP2ClientOrbData](./iofirewireserialbusprotocoltransport/sbp2clientorbdata.md)
### Instance Methods
- [- AbortSCSICommand](./iofirewireserialbusprotocoltransport/api-1550722-abortscsicommand.md)
- [- AllocateResources](./iofirewireserialbusprotocoltransport/api-1550703-allocateresources.md)
- [- CoalesceSenseData](./iofirewireserialbusprotocoltransport/api-1550715-coalescesensedata.md)
- [- CommandORBAccessor](./iofirewireserialbusprotocoltransport/api-1550717-commandorbaccessor.md)
- [- CompleteSCSITask](./iofirewireserialbusprotocoltransport/api-1550708-completescsitask.md)
- [- ConnectToDevice](./iofirewireserialbusprotocoltransport/api-1550705-connecttodevice.md)
- [- CriticalOrbSubmission](./iofirewireserialbusprotocoltransport/api-1550714-criticalorbsubmission.md)
- [- DeallocateResources](./iofirewireserialbusprotocoltransport/api-1550690-deallocateresources.md)
- [- DisconnectFromDevice](./iofirewireserialbusprotocoltransport/api-1550691-disconnectfromdevice.md)
- [- FetchAgentResetComplete](./iofirewireserialbusprotocoltransport/api-1550683-fetchagentresetcomplete.md)
- [- HandleProtocolServiceFeature](./iofirewireserialbusprotocoltransport/api-1550695-handleprotocolservicefeature.md)
- [- IsDeviceCPUInDiskMode](./iofirewireserialbusprotocoltransport/api-1550713-isdevicecpuindiskmode.md)
- [- IsProtocolServiceSupported](./iofirewireserialbusprotocoltransport/api-1550692-isprotocolservicesupported.md)
- [- LoginCompletion](./iofirewireserialbusprotocoltransport/api-1550711-logincompletion.md)
- [- LogoutCompletion](./iofirewireserialbusprotocoltransport/api-1550689-logoutcompletion.md)
- [- LunResetComplete](./iofirewireserialbusprotocoltransport/api-1550706-lunresetcomplete.md)
- [- SBP2LoginAccessor](./iofirewireserialbusprotocoltransport/api-1550719-sbp2loginaccessor.md)
- [- SendSCSICommand](./iofirewireserialbusprotocoltransport/api-1550720-sendscsicommand.md)
- [- SetCommandBuffers](./iofirewireserialbusprotocoltransport/api-1550712-setcommandbuffers.md)
- [- SetValidAutoSenseData](./iofirewireserialbusprotocoltransport/api-1550681-setvalidautosensedata.md)
- [- StatusNotify](./iofirewireserialbusprotocoltransport/api-1550680-statusnotify.md)
- [- UnsolicitedStatusNotify](./iofirewireserialbusprotocoltransport/api-1550698-unsolicitedstatusnotify.md)
- [- cleanUp](./iofirewireserialbusprotocoltransport/api-1550702-cleanup.md)
- [- finalize](./iofirewireserialbusprotocoltransport/api-1550704-finalize.md)
- [- free](./iofirewireserialbusprotocoltransport/api-1550694-free.md)
- [- getMetaClass](./iofirewireserialbusprotocoltransport/api-1550682-getmetaclass.md)
- [- init](./iofirewireserialbusprotocoltransport/api-1550684-init.md)
- [- login](./iofirewireserialbusprotocoltransport/api-1550696-login.md)
- [- loginLost](./iofirewireserialbusprotocoltransport/api-1550693-loginlost.md)
- [- loginResumed](./iofirewireserialbusprotocoltransport/api-1550685-loginresumed.md)
- [- loginSuspended](./iofirewireserialbusprotocoltransport/api-1550709-loginsuspended.md)
- [- message](./iofirewireserialbusprotocoltransport/api-1550688-message.md)
- [- start](./iofirewireserialbusprotocoltransport/api-1550710-start.md)
- [- submitLogin](./iofirewireserialbusprotocoltransport/api-1550707-submitlogin.md)
- [- submitOrbFromQueue](./iofirewireserialbusprotocoltransport/api-1550723-submitorbfromqueue.md)
### Type Methods
- [+ ConnectToDeviceStatic](./iofirewireserialbusprotocoltransport/api-1550699-connecttodevicestatic.md)
- [+ CriticalOrbSubmissionStatic](./iofirewireserialbusprotocoltransport/api-1550718-criticalorbsubmissionstatic.md)
- [+ FetchAgentResetCompleteStatic](./iofirewireserialbusprotocoltransport/api-1550721-fetchagentresetcompletestatic.md)
- [+ LoginCompletionStatic](./iofirewireserialbusprotocoltransport/api-1550700-logincompletionstatic.md)
- [+ LogoutCompletionStatic](./iofirewireserialbusprotocoltransport/api-1550716-logoutcompletionstatic.md)
- [+ LunResetCompleteStatic](./iofirewireserialbusprotocoltransport/api-1550697-lunresetcompletestatic.md)
- [+ StatusNotifyStatic](./iofirewireserialbusprotocoltransport/api-1550686-statusnotifystatic.md)
- [+ UnsolicitedStatusNotifyStatic](./iofirewireserialbusprotocoltransport/api-1550701-unsolicitedstatusnotifystatic.md)

## Relationships

### Inherits From
- [IOSCSIProtocolServices](./ioscsiprotocolservices.md)

## See Also

### Interfaces
- [IOFireWireSBP2Target](./iofirewiresbp2target.md)
  Serves as bridge between IOFireWireUnit and IOFireWireLUN.
- [IOFireWireController](./iofirewirecontroller.md)
- [IOFireWireBus](./iofirewirebus.md)
  IOFireWireBus is a public class the provides access to general FireWire functionality...


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireserialbusprotocoltransport)*