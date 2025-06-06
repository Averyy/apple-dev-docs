# IOFireWireSerialBusProtocolTransport

**Framework**: Kernel  
**Kind**: cl

SCSI Protocol Driver Family for FireWire SBP2 Devices.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireSerialBusProtocolTransport : IOSCSIProtocolServices
```

#### Overview

IOFireWireSerialBusProtocolTransport contains all the bus specific support for FireWire SBP2 compliant devices. To add vendor specific features or workarounds you will sub-class the appropriate methods of this family.

## Topics

### Miscellaneous
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
- [UnsolicitedStatusNotify](iofirewireserialbusprotocoltransport/1813820-unsolicitedstatusnotify.md)
  This is our handler for unsolicited status.
### DataTypes
- [SBP2ClientOrbData](iofirewireserialbusprotocoltransport/sbp2clientorbdata.md)
### Instance Methods
- [- AbortSCSICommand](iofirewireserialbusprotocoltransport/1550722-abortscsicommand.md)
- [- AllocateResources](iofirewireserialbusprotocoltransport/1550703-allocateresources.md)
- [- CoalesceSenseData](iofirewireserialbusprotocoltransport/1550715-coalescesensedata.md)
- [- CommandORBAccessor](iofirewireserialbusprotocoltransport/1550717-commandorbaccessor.md)
- [- CompleteSCSITask](iofirewireserialbusprotocoltransport/1550708-completescsitask.md)
- [- ConnectToDevice](iofirewireserialbusprotocoltransport/1550705-connecttodevice.md)
- [- CriticalOrbSubmission](iofirewireserialbusprotocoltransport/1550714-criticalorbsubmission.md)
- [- DeallocateResources](iofirewireserialbusprotocoltransport/1550690-deallocateresources.md)
- [- DisconnectFromDevice](iofirewireserialbusprotocoltransport/1550691-disconnectfromdevice.md)
- [- FetchAgentResetComplete](iofirewireserialbusprotocoltransport/1550683-fetchagentresetcomplete.md)
- [- HandleProtocolServiceFeature](iofirewireserialbusprotocoltransport/1550695-handleprotocolservicefeature.md)
- [- IsDeviceCPUInDiskMode](iofirewireserialbusprotocoltransport/1550713-isdevicecpuindiskmode.md)
- [- IsProtocolServiceSupported](iofirewireserialbusprotocoltransport/1550692-isprotocolservicesupported.md)
- [- LoginCompletion](iofirewireserialbusprotocoltransport/1550711-logincompletion.md)
- [- LogoutCompletion](iofirewireserialbusprotocoltransport/1550689-logoutcompletion.md)
- [- LunResetComplete](iofirewireserialbusprotocoltransport/1550706-lunresetcomplete.md)
- [- SBP2LoginAccessor](iofirewireserialbusprotocoltransport/1550719-sbp2loginaccessor.md)
- [- SendSCSICommand](iofirewireserialbusprotocoltransport/1550720-sendscsicommand.md)
- [- SetCommandBuffers](iofirewireserialbusprotocoltransport/1550712-setcommandbuffers.md)
- [- SetValidAutoSenseData](iofirewireserialbusprotocoltransport/1550681-setvalidautosensedata.md)
- [- StatusNotify](iofirewireserialbusprotocoltransport/1550680-statusnotify.md)
- [- UnsolicitedStatusNotify](iofirewireserialbusprotocoltransport/1550698-unsolicitedstatusnotify.md)
- [- cleanUp](iofirewireserialbusprotocoltransport/1550702-cleanup.md)
- [- finalize](iofirewireserialbusprotocoltransport/1550704-finalize.md)
- [- free](iofirewireserialbusprotocoltransport/1550694-free.md)
- [- getMetaClass](iofirewireserialbusprotocoltransport/1550682-getmetaclass.md)
- [- init](iofirewireserialbusprotocoltransport/1550684-init.md)
- [- login](iofirewireserialbusprotocoltransport/1550696-login.md)
- [- loginLost](iofirewireserialbusprotocoltransport/1550693-loginlost.md)
- [- loginResumed](iofirewireserialbusprotocoltransport/1550685-loginresumed.md)
- [- loginSuspended](iofirewireserialbusprotocoltransport/1550709-loginsuspended.md)
- [- message](iofirewireserialbusprotocoltransport/1550688-message.md)
- [- start](iofirewireserialbusprotocoltransport/1550710-start.md)
- [- submitLogin](iofirewireserialbusprotocoltransport/1550707-submitlogin.md)
- [- submitOrbFromQueue](iofirewireserialbusprotocoltransport/1550723-submitorbfromqueue.md)
### Type Methods
- [+ ConnectToDeviceStatic](iofirewireserialbusprotocoltransport/1550699-connecttodevicestatic.md)
- [+ CriticalOrbSubmissionStatic](iofirewireserialbusprotocoltransport/1550718-criticalorbsubmissionstatic.md)
- [+ FetchAgentResetCompleteStatic](iofirewireserialbusprotocoltransport/1550721-fetchagentresetcompletestatic.md)
- [+ LoginCompletionStatic](iofirewireserialbusprotocoltransport/1550700-logincompletionstatic.md)
- [+ LogoutCompletionStatic](iofirewireserialbusprotocoltransport/1550716-logoutcompletionstatic.md)
- [+ LunResetCompleteStatic](iofirewireserialbusprotocoltransport/1550697-lunresetcompletestatic.md)
- [+ StatusNotifyStatic](iofirewireserialbusprotocoltransport/1550686-statusnotifystatic.md)
- [+ UnsolicitedStatusNotifyStatic](iofirewireserialbusprotocoltransport/1550701-unsolicitedstatusnotifystatic.md)

## Relationships

### Inherits From
- [IOSCSIProtocolServices](ioscsiprotocolservices.md)

## See Also

- [IOFireWireSBP2Target](iofirewiresbp2target.md)
  Serves as bridge between IOFireWireUnit and IOFireWireLUN.
- [IOFireWireController](iofirewirecontroller.md)
- [IOFireWireBus](iofirewirebus.md)
  IOFireWireBus is a public class the provides access to general FireWire functionality...


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireserialbusprotocoltransport)*