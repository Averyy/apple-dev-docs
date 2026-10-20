# IOSCSIPrimaryCommandsDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOSCSIPrimaryCommandsDevice : IOSCSIProtocolInterface
```

## Topics

### Instance Methods
- [- AbortCommand](./ioscsiprimarycommandsdevice/api-1556524-abortcommand.md)
- [- AbortTask](./ioscsiprimarycommandsdevice/api-1556515-aborttask.md)
- [- AbortTaskSet](./ioscsiprimarycommandsdevice/api-1556562-aborttaskset.md)
- [- CheckPowerConditionsModePage](./ioscsiprimarycommandsdevice/api-1556567-checkpowerconditionsmodepage.md)
- [- ClampPowerState](./ioscsiprimarycommandsdevice/api-1556526-clamppowerstate.md)
- [- ClearACA](./ioscsiprimarycommandsdevice/api-1556522-clearaca.md)
- [- ClearNotReadyStatus](./ioscsiprimarycommandsdevice/api-1556465-clearnotreadystatus.md)
- [- ClearPowerOnReset](./ioscsiprimarycommandsdevice/api-1556583-clearpoweronreset.md)
- [- ClearTaskSet](./ioscsiprimarycommandsdevice/api-1556530-cleartaskset.md)
- [- ExecuteCommand](./ioscsiprimarycommandsdevice/api-1556545-executecommand.md)
- [- GatedWaitForTask](./ioscsiprimarycommandsdevice/api-1556493-gatedwaitfortask.md)
- [- GetANSIVersion](./ioscsiprimarycommandsdevice/api-1556554-getansiversion.md)
- [- GetApplicationLayerReference](./ioscsiprimarycommandsdevice/api-1556502-getapplicationlayerreference.md)
- [- GetAutoSenseData](./ioscsiprimarycommandsdevice/api-1556588-getautosensedata.md)
- [- GetAutoSenseData](./ioscsiprimarycommandsdevice/api-3516757-getautosensedata.md)
- [- GetAutoSenseDataSize](./ioscsiprimarycommandsdevice/api-1556468-getautosensedatasize.md)
- [- GetCMDQUE](./ioscsiprimarycommandsdevice/api-1556556-getcmdque.md)
- [- GetDataBuffer](./ioscsiprimarycommandsdevice/api-1556532-getdatabuffer.md)
- [- GetDataTransferDirection](./ioscsiprimarycommandsdevice/api-1556527-getdatatransferdirection.md)
- [- GetDeviceCharacteristicsDictionary](./ioscsiprimarycommandsdevice/api-1556558-getdevicecharacteristicsdictiona.md)
- [- GetModeSense](./ioscsiprimarycommandsdevice/api-1556474-getmodesense.md)
- [- GetNumberOfPowerStateTransitions](./ioscsiprimarycommandsdevice/api-1556539-getnumberofpowerstatetransitions.md)
- [- GetProductString](./ioscsiprimarycommandsdevice/api-1556520-getproductstring.md)
- [- GetProtocolCharacteristicsDictionary](./ioscsiprimarycommandsdevice/api-1556560-getprotocolcharacteristicsdictio.md)
- [- GetProtocolDriver](./ioscsiprimarycommandsdevice/api-1556594-getprotocoldriver.md)
- [- GetRealizedDataTransferCount](./ioscsiprimarycommandsdevice/api-1556571-getrealizeddatatransfercount.md)
- [- GetRequestedDataTransferCount](./ioscsiprimarycommandsdevice/api-1556552-getrequesteddatatransfercount.md)
- [- GetRetryCount](./ioscsiprimarycommandsdevice/api-1556490-getretrycount.md)
- [- GetRevisionString](./ioscsiprimarycommandsdevice/api-1556536-getrevisionstring.md)
- [- GetSCSITask](./ioscsiprimarycommandsdevice/api-1556514-getscsitask.md)
- [- GetServiceResponse](./ioscsiprimarycommandsdevice/api-1556548-getserviceresponse.md)
- [- GetTaggedTaskIdentifier](./ioscsiprimarycommandsdevice/api-1556481-gettaggedtaskidentifier.md)
- [- GetTaskAttribute](./ioscsiprimarycommandsdevice/api-1556595-gettaskattribute.md)
- [- GetTaskState](./ioscsiprimarycommandsdevice/api-1556480-gettaskstate.md)
- [- GetTaskStatus](./ioscsiprimarycommandsdevice/api-1556500-gettaskstatus.md)
- [- GetTimeoutDuration](./ioscsiprimarycommandsdevice/api-1556547-gettimeoutduration.md)
- [- GetUniqueTagID](./ioscsiprimarycommandsdevice/api-1556533-getuniquetagid.md)
- [- GetVendorString](./ioscsiprimarycommandsdevice/api-1556541-getvendorstring.md)
- [- HandleIncrementOutstandingCommandsCount](./ioscsiprimarycommandsdevice/api-1556513-handleincrementoutstandingcomman.md)
- [- HandleProtocolServiceFeature](./ioscsiprimarycommandsdevice/api-1556473-handleprotocolservicefeature.md)
- [- INQUIRY](./ioscsiprimarycommandsdevice/api-1556549-inquiry.md)
- [- INQUIRY](./ioscsiprimarycommandsdevice/api-3516758-inquiry.md)
- [- IncrementOutstandingCommandsCount](./ioscsiprimarycommandsdevice/api-1556507-incrementoutstandingcommandscoun.md)
- [- InitializeDeviceSupport](./ioscsiprimarycommandsdevice/api-1556544-initializedevicesupport.md)
- [- IsDeviceAccessEnabled](./ioscsiprimarycommandsdevice/api-1556471-isdeviceaccessenabled.md)
- [- IsDeviceAccessSuspended](./ioscsiprimarycommandsdevice/api-1556508-isdeviceaccesssuspended.md)
- [- IsMemoryDescriptorValid](./ioscsiprimarycommandsdevice/api-1556505-ismemorydescriptorvalid.md)
- [- IsMemoryDescriptorValid](./ioscsiprimarycommandsdevice/api-3516759-ismemorydescriptorvalid.md)
- [- IsParameterValid](./ioscsiprimarycommandsdevice/api-1556550-isparametervalid.md)
- [- IsParameterValid](./ioscsiprimarycommandsdevice/api-3516760-isparametervalid.md)
- [- IsParameterValid](./ioscsiprimarycommandsdevice/api-3516761-isparametervalid.md)
- [- IsParameterValid](./ioscsiprimarycommandsdevice/api-3516762-isparametervalid.md)
- [- IsProtocolAccessEnabled](./ioscsiprimarycommandsdevice/api-1556581-isprotocolaccessenabled.md)
- [- IsProtocolServiceSupported](./ioscsiprimarycommandsdevice/api-1556529-isprotocolservicesupported.md)
- [- LOG_SELECT](./ioscsiprimarycommandsdevice/api-1556487-log_select.md)
- [- LOG_SENSE](./ioscsiprimarycommandsdevice/api-1556568-log_sense.md)
- [- LogicalUnitReset](./ioscsiprimarycommandsdevice/api-1556462-logicalunitreset.md)
- [- MODE_SELECT_10](./ioscsiprimarycommandsdevice/api-1556589-mode_select_10.md)
- [- MODE_SELECT_6](./ioscsiprimarycommandsdevice/api-1556494-mode_select_6.md)
- [- MODE_SENSE_10](./ioscsiprimarycommandsdevice/api-1556538-mode_sense_10.md)
- [- MODE_SENSE_6](./ioscsiprimarycommandsdevice/api-1556517-mode_sense_6.md)
- [- MapINQUIRYDataToIconFile](./ioscsiprimarycommandsdevice/api-1556519-mapinquirydatatoiconfile.md)
- [- PERSISTENT_RESERVE_IN](./ioscsiprimarycommandsdevice/api-1556592-persistent_reserve_in.md)
- [- PERSISTENT_RESERVE_OUT](./ioscsiprimarycommandsdevice/api-1556555-persistent_reserve_out.md)
- [- PREVENT_ALLOW_MEDIUM_REMOVAL](./ioscsiprimarycommandsdevice/api-1556591-prevent_allow_medium_removal.md)
- [- READ_BUFFER](./ioscsiprimarycommandsdevice/api-1556575-read_buffer.md)
- [- RECEIVE](./ioscsiprimarycommandsdevice/api-1556516-receive.md)
- [- RECEIVE_DIAGNOSTICS_RESULTS](./ioscsiprimarycommandsdevice/api-1556478-receive_diagnostics_results.md)
- [- RELEASE_10](./ioscsiprimarycommandsdevice/api-1556570-release_10.md)
- [- RELEASE_6](./ioscsiprimarycommandsdevice/api-1556565-release_6.md)
- [- REPORT_DEVICE_IDENTIFIER](./ioscsiprimarycommandsdevice/api-1556528-report_device_identifier.md)
- [- REPORT_LUNS](./ioscsiprimarycommandsdevice/api-1556543-report_luns.md)
- [- REQUEST_SENSE](./ioscsiprimarycommandsdevice/api-1556466-request_sense.md)
- [- RESERVE_10](./ioscsiprimarycommandsdevice/api-1556489-reserve_10.md)
- [- RESERVE_6](./ioscsiprimarycommandsdevice/api-1556535-reserve_6.md)
- [- ReleasePowerStateClamp](./ioscsiprimarycommandsdevice/api-1556510-releasepowerstateclamp.md)
- [- ReleaseSCSITask](./ioscsiprimarycommandsdevice/api-1556503-releasescsitask.md)
- [- ResetForNewTask](./ioscsiprimarycommandsdevice/api-1556586-resetfornewtask.md)
- [- ResumeDeviceSupport](./ioscsiprimarycommandsdevice/api-1556491-resumedevicesupport.md)
- [- RetrieveINQUIRYData](./ioscsiprimarycommandsdevice/api-1556551-retrieveinquirydata.md)
- [- SEND](./ioscsiprimarycommandsdevice/api-1556585-send.md)
- [- SEND_DIAGNOSTICS](./ioscsiprimarycommandsdevice/api-1556477-send_diagnostics.md)
- [- SET_DEVICE_IDENTIFIER](./ioscsiprimarycommandsdevice/api-1556467-set_device_identifier.md)
- [- SendCommand](./ioscsiprimarycommandsdevice/api-1556511-sendcommand.md)
- [- SendCommand](./ioscsiprimarycommandsdevice/api-3516763-sendcommand.md)
- [- SetANSIVersion](./ioscsiprimarycommandsdevice/api-1556485-setansiversion.md)
- [- SetApplicationLayerReference](./ioscsiprimarycommandsdevice/api-1556563-setapplicationlayerreference.md)
- [- SetAutosenseCommand](./ioscsiprimarycommandsdevice/api-1556475-setautosensecommand.md)
- [- SetCMDQUE](./ioscsiprimarycommandsdevice/api-1556553-setcmdque.md)
- [- SetCommandDescriptorBlock](./ioscsiprimarycommandsdevice/api-1556506-setcommanddescriptorblock.md)
- [- SetCommandDescriptorBlock](./ioscsiprimarycommandsdevice/api-3516764-setcommanddescriptorblock.md)
- [- SetCommandDescriptorBlock](./ioscsiprimarycommandsdevice/api-3516765-setcommanddescriptorblock.md)
- [- SetCommandDescriptorBlock](./ioscsiprimarycommandsdevice/api-3516766-setcommanddescriptorblock.md)
- [- SetDataBuffer](./ioscsiprimarycommandsdevice/api-1556518-setdatabuffer.md)
- [- SetDataTransferDirection](./ioscsiprimarycommandsdevice/api-1556509-setdatatransferdirection.md)
- [- SetRealizedDataTransferCount](./ioscsiprimarycommandsdevice/api-1556593-setrealizeddatatransfercount.md)
- [- SetRequestedDataTransferCount](./ioscsiprimarycommandsdevice/api-1556582-setrequesteddatatransfercount.md)
- [- SetServiceResponse](./ioscsiprimarycommandsdevice/api-1556580-setserviceresponse.md)
- [- SetTaggedTaskIdentifier](./ioscsiprimarycommandsdevice/api-1556476-settaggedtaskidentifier.md)
- [- SetTaskAttribute](./ioscsiprimarycommandsdevice/api-1556574-settaskattribute.md)
- [- SetTaskCompletionCallback](./ioscsiprimarycommandsdevice/api-1556573-settaskcompletioncallback.md)
- [- SetTaskState](./ioscsiprimarycommandsdevice/api-1556534-settaskstate.md)
- [- SetTaskStatus](./ioscsiprimarycommandsdevice/api-1556483-settaskstatus.md)
- [- SetTimeoutDuration](./ioscsiprimarycommandsdevice/api-1556525-settimeoutduration.md)
- [- StartDeviceSupport](./ioscsiprimarycommandsdevice/api-1556479-startdevicesupport.md)
- [- StopDeviceSupport](./ioscsiprimarycommandsdevice/api-1556482-stopdevicesupport.md)
- [- SuspendDeviceSupport](./ioscsiprimarycommandsdevice/api-1556469-suspenddevicesupport.md)
- [- TEST_UNIT_READY](./ioscsiprimarycommandsdevice/api-1556495-test_unit_ready.md)
- [- TargetReset](./ioscsiprimarycommandsdevice/api-1556464-targetreset.md)
- [- TaskCompletedNotification](./ioscsiprimarycommandsdevice/api-1556590-taskcompletednotification.md)
- [- TaskCompletion](./ioscsiprimarycommandsdevice/api-1556504-taskcompletion.md)
- [- TerminateDeviceSupport](./ioscsiprimarycommandsdevice/api-1556579-terminatedevicesupport.md)
- [- VerifyDeviceState](./ioscsiprimarycommandsdevice/api-1556542-verifydevicestate.md)
- [- WRITE_BUFFER](./ioscsiprimarycommandsdevice/api-1556564-write_buffer.md)
- [- free](./ioscsiprimarycommandsdevice/api-1556523-free.md)
- [- getMetaClass](./ioscsiprimarycommandsdevice/api-1556584-getmetaclass.md)
- [- init](./ioscsiprimarycommandsdevice/api-1556488-init.md)
- [- message](./ioscsiprimarycommandsdevice/api-1556486-message.md)
- [- setAggressiveness](./ioscsiprimarycommandsdevice/api-1556561-setaggressiveness.md)
- [- start](./ioscsiprimarycommandsdevice/api-1556557-start.md)
- [- stop](./ioscsiprimarycommandsdevice/api-1556531-stop.md)
### Type Methods
- [+ ServerKeyswitchCallback](./ioscsiprimarycommandsdevice/api-1556540-serverkeyswitchcallback.md)
- [+ TaskCallback](./ioscsiprimarycommandsdevice/api-1556576-taskcallback.md)
- [+ sGetOwnerForTask](./ioscsiprimarycommandsdevice/api-1556572-sgetownerfortask.md)
- [+ sIncrementOutstandingCommandsCount](./ioscsiprimarycommandsdevice/api-1556546-sincrementoutstandingcommandscou.md)
- [+ sWaitForTask](./ioscsiprimarycommandsdevice/api-1556498-swaitfortask.md)

## Relationships

### Inherits From
- [IOSCSIProtocolInterface](./ioscsiprotocolinterface.md)

## See Also

### Base Types
- [IOReducedBlockServices](./ioreducedblockservices.md)
- [IOSCSIPeripheralDeviceNub](./ioscsiperipheraldevicenub.md)
- [IOSCSIProtocolServices](./ioscsiprotocolservices.md)
  This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).
- [IOSCSIProtocolInterface](./ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprimarycommandsdevice)*