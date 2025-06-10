# IOSCSIProtocolServices

**Framework**: Kernel  
**Kind**: cl

This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOSCSIProtocolServices : IOSCSIProtocolInterface
```

## Topics

### Miscellaneous
- [AbortCommand](ioscsiprotocolservices/1809724-abortcommand.md)
  Deprecated. Do not use.
- [AbortSCSICommand](ioscsiprotocolservices/1809736-abortscsicommand.md)
  Pure virtual method subclasses must implement so that SCSITasks may be aborted.
- [AbortSCSITaskFromQueue](ioscsiprotocolservices/1809747-abortscsitaskfromqueue.md)
  Deprecated internal method.
- [AbortTask](ioscsiprotocolservices/1809759-aborttask.md)
  The Task Management function to allow the SCSI Application Layer client to request that a specific task be aborted.
- [AbortTaskSet](ioscsiprotocolservices/1809765-aborttaskset.md)
  The Task Management function to allow the SCSI Application Layer client to request that a complete task set be aborted.
- [AddSCSITaskToHeadOfQueue](ioscsiprotocolservices/1809777-addscsitasktoheadofqueue.md)
  Internal method called to add a SCSITask to the head of the processing queue.
- [AddSCSITaskToQueue](ioscsiprotocolservices/1809791-addscsitasktoqueue.md)
  Internal method called to add a SCSITask to the processing queue.
- [ClearACA](ioscsiprotocolservices/1809805-clearaca.md)
  The Task Management function to clear an Auto-Contingent Allegiance condition.
- [ClearTaskSet](ioscsiprotocolservices/1809813-cleartaskset.md)
  The Task Management function to clear a task set.
- [CommandCompleted](ioscsiprotocolservices/1809823-commandcompleted.md)
  Method subclass calls to complete a SCSITask.
- [CreateSCSITargetDevice](ioscsiprotocolservices/1809830-createscsitargetdevice.md)
  Used to create a SCSITargetDevice which will manage logical units.
- [EnsureAutosenseDescriptorExists](ioscsiprotocolservices/1809843-ensureautosensedescriptorexists.md)
  Internal method, not to be called by subclasses.
- [ExecuteCommand](ioscsiprotocolservices/1809854-executecommand.md)
  ExecuteCommand method will take a SCSI Task and transport it across the physical wire(s) to the device.
- [free](ioscsiprotocolservices/1809869-free.md)
  Frees data structures that were allocated during start().
- [GetAutosenseRequestedDataTransferCount](ioscsiprotocolservices/1809881-getautosenserequesteddatatransfe.md)
  Accessor method to retrieve the requested data transfer count for autosense data associated with the specified request.
- [GetCommandDescriptorBlock](ioscsiprotocolservices/1809892-getcommanddescriptorblock.md)
  Accessor method to retrieve the Command Descriptor Block associated with the specified request.
- [GetCommandDescriptorBlockSize](ioscsiprotocolservices/1809902-getcommanddescriptorblocksize.md)
  Accessor method to retrieve the Command Descriptor Block size associated with the specified request.
- [GetDataBuffer](ioscsiprotocolservices/1809915-getdatabuffer.md)
  Accessor method to retrieve the data buffer associated with the specified request.
- [GetDataBufferOffset](ioscsiprotocolservices/1809935-getdatabufferoffset.md)
  Accessor method to retrieve the data buffer offset associated with the specified request.
- [GetDataTransferDirection](ioscsiprotocolservices/1809946-getdatatransferdirection.md)
  Accessor method to retrieve the data transfer direction associated with the specified request.
- [GetInitialPowerState](ioscsiprotocolservices/1809959-getinitialpowerstate.md)
  This method is called once, right after InitializePowerManagement() in order to determine what state the device is initially in at startup time (usually the highest power mode).
- [GetLogicalUnitBytes](ioscsiprotocolservices/1809964-getlogicalunitbytes.md)
  Accessor method to retrieve the logical unit bytes associated with the specified request.
- [GetLogicalUnitNumber](ioscsiprotocolservices/1809972-getlogicalunitnumber.md)
  Accessor method to retrieve the logical unit number associated with the specified request.
- [GetProtocolLayerReference](ioscsiprotocolservices/1809980-getprotocollayerreference.md)
  Accessor method to retrieve the protocol layer reference.
- [GetRealizedDataTransferCount](ioscsiprotocolservices/1809989-getrealizeddatatransfercount.md)
  Accessor method to retrieve the realized data transfer count associated with the specified request.
- [GetRequestedDataTransferCount](ioscsiprotocolservices/1809996-getrequesteddatatransfercount.md)
  Accessor method to retrieve the requested data transfer count associated with the specified request.
- [GetTaskAttribute](ioscsiprotocolservices/1810005-gettaskattribute.md)
  Accessor method to retrieve the SCSITaskAttribute associated with the specified request.
- [GetTaskExecutionMode](ioscsiprotocolservices/1810017-gettaskexecutionmode.md)
  Internal method used to retrieve the task execution mode.
- [GetTaskState](ioscsiprotocolservices/1810028-gettaskstate.md)
  Accessor method to retrieve the SCSITaskState associated with the specified request.
- [GetTimeoutDuration](ioscsiprotocolservices/1810038-gettimeoutduration.md)
  Accessor method to retrieve the timeout duration in milliseconds associated with the specified request.
- [HandleAbortTask](ioscsiprotocolservices/1810051-handleaborttask.md)
  HandleAbortTask instructs the Protocol Services driver to abort the task.
- [HandleAbortTaskSet](ioscsiprotocolservices/1810062-handleaborttaskset.md)
  HandleAbortTaskSet instructs the Protocol Services driver to abort the task set.
- [HandleCheckPowerState](ioscsiprotocolservices/1810080-handlecheckpowerstate.md)
  Method called to check if the device is in the correct power state for an I/O.
- [HandleClearACA](ioscsiprotocolservices/1810093-handleclearaca.md)
  HandleClearACA instructs the Protocol Services driver to clear an auto-contingent allegiance.
- [HandleClearTaskSet](ioscsiprotocolservices/1810105-handlecleartaskset.md)
  HandleClearTaskSet instructs the Protocol Services driver to clear the task set.
- [HandleLogicalUnitReset](ioscsiprotocolservices/1810119-handlelogicalunitreset.md)
  HandleLogicalUnitReset instructs the Protocol Services driver to reset the logical unit.
- [HandlePowerChange](ioscsiprotocolservices/1810127-handlepowerchange.md)
  This method is called to handle a power change.
- [HandlePowerOff](ioscsiprotocolservices/1810144-handlepoweroff.md)
  Convenience method for a protocol service driver to handle a power off call (called on the way to sleep).
- [HandlePowerOn](ioscsiprotocolservices/1810154-handlepoweron.md)
  Convenience method for a protocol service driver to handle a power on call (called on the way back up from sleep).
- [HandleProtocolServiceFeature](ioscsiprotocolservices/1810168-handleprotocolservicefeature.md)
  HandleProtocolServiceFeature instructs the Protocol Services driver to perform the necessary tasks for the indicated feature.
- [HandleTargetReset](ioscsiprotocolservices/1810176-handletargetreset.md)
  HandleTargetReset instructs the Protocol Services driver to reset the target.
- [init](ioscsiprotocolservices/1810187-init.md)
  Standard init method for all IORegistryEntry subclasses.
- [InitializePowerManagement](ioscsiprotocolservices/1810204-initializepowermanagement.md)
  Subclasses call this method to initialize power management.
- [IsProtocolServiceSupported](ioscsiprotocolservices/1810217-isprotocolservicesupported.md)
  IsProtocolServiceSupported will return true if the specified feature is supported by the protocol layer.
- [LogicalUnitReset](ioscsiprotocolservices/1810234-logicalunitreset.md)
  The Task Management function to reset a logical unit.
- [ProcessCompletedTask](ioscsiprotocolservices/1810248-processcompletedtask.md)
  Internal method called to process completed SCSITasks.
- [RegisterSCSITaskCompletionRoutine](ioscsiprotocolservices/1810264-registerscsitaskcompletionroutin.md)
  Used by IOSCSITargetDevice to register a completion routine.
- [RejectSCSITasksCurrentlyQueued](ioscsiprotocolservices/1810276-rejectscsitaskscurrentlyqueued.md)
  Internal method called to reject currently enqueued SCSITasks.
- [RejectTask](ioscsiprotocolservices/1810289-rejecttask.md)
  Internal method called to reject a particular SCSITask.
- [RetrieveNextSCSITaskFromQueue](ioscsiprotocolservices/1810300-retrievenextscsitaskfromqueue.md)
  Internal method called to retrieve the next SCSITask to process.
- [SendNotification_DeviceRemoved](ioscsiprotocolservices/1810317-sendnotification_deviceremoved.md)
  Method called by subclasses when a device is physically removed from the bus.
- [SendNotification_VerifyDeviceState](ioscsiprotocolservices/1810332-sendnotification_verifydevicesta.md)
  Method called by subclasses when a device state needs to be re-verified due to some bus condition which may have changed the device state.
- [SendSCSICommand](ioscsiprotocolservices/1810345-sendscsicommand.md)
  Pure virtual method subclasses must implement in order to send SCSITasks on the wire.
- [SendSCSITasksFromQueue](ioscsiprotocolservices/1810363-sendscsitasksfromqueue.md)
  Internal method called to start processing SCSITasks.
- [SetAutoSenseData(SCSITaskIdentifier, SCSI_Sense_Data *)](ioscsiprotocolservices/1810382-setautosensedata.md)
  Accessor method to set the autosense data. NOTE: This method is deprecated.
- [SetAutoSenseData(SCSITaskIdentifier, SCSI_Sense_Data *, UInt8)](ioscsiprotocolservices/1810397-setautosensedata.md)
  Accessor method to set the autosense data.
- [SetProtocolLayerReference](ioscsiprotocolservices/1810411-setprotocollayerreference.md)
  Accessor method to set the protocol layer reference.
- [SetRealizedDataTransferCount](ioscsiprotocolservices/1810431-setrealizeddatatransfercount.md)
  Accessor method to set the realized (actual) data transfer count associated with the specified request.
- [SetTaskExecutionMode](ioscsiprotocolservices/1810455-settaskexecutionmode.md)
  Internal method used to set the task execution mode.
- [SetTaskState](ioscsiprotocolservices/1810476-settaskstate.md)
  Accessor method to set the SCSITaskState associated with the specified request.
- [start](ioscsiprotocolservices/1810514-start.md)
  During an IOService object's instantiation, starts the IOService object that has been selected to run on the provider.
- [TargetReset](ioscsiprotocolservices/1810537-targetreset.md)
  The Task Management function to reset a target device.
- [TicklePowerManager](ioscsiprotocolservices/1810572-ticklepowermanager.md)
  Internal method. Do not use.
### Instance Methods
- [- AbortCommand](ioscsiprotocolservices/1509516-abortcommand.md)
- [- AbortSCSICommand](ioscsiprotocolservices/1509523-abortscsicommand.md)
- [- AbortSCSITaskFromQueue](ioscsiprotocolservices/1509532-abortscsitaskfromqueue.md)
- [- AbortTask](ioscsiprotocolservices/1509469-aborttask.md)
- [- AbortTaskSet](ioscsiprotocolservices/1509555-aborttaskset.md)
- [- AddSCSITaskToHeadOfQueue](ioscsiprotocolservices/1509548-addscsitasktoheadofqueue.md)
- [- AddSCSITaskToQueue](ioscsiprotocolservices/1509468-addscsitasktoqueue.md)
- [- ClearACA](ioscsiprotocolservices/1509499-clearaca.md)
- [- ClearTaskSet](ioscsiprotocolservices/1509486-cleartaskset.md)
- [- CommandCompleted](ioscsiprotocolservices/1509542-commandcompleted.md)
- [- CreateSCSITargetDevice](ioscsiprotocolservices/1509451-createscsitargetdevice.md)
- [- EnsureAutosenseDescriptorExists](ioscsiprotocolservices/1509514-ensureautosensedescriptorexists.md)
- [- ExecuteCommand](ioscsiprotocolservices/1509557-executecommand.md)
- [- GetAutosenseRequestedDataTransferCount](ioscsiprotocolservices/1509552-getautosenserequesteddatatransfe.md)
- [- GetCommandDescriptorBlock](ioscsiprotocolservices/1509478-getcommanddescriptorblock.md)
- [- GetCommandDescriptorBlockSize](ioscsiprotocolservices/1509487-getcommanddescriptorblocksize.md)
- [- GetDataBuffer](ioscsiprotocolservices/1509473-getdatabuffer.md)
- [- GetDataBufferOffset](ioscsiprotocolservices/1509488-getdatabufferoffset.md)
- [- GetDataTransferDirection](ioscsiprotocolservices/1509529-getdatatransferdirection.md)
- [- GetInitialPowerState](ioscsiprotocolservices/1509539-getinitialpowerstate.md)
- [- GetLogicalUnitBytes](ioscsiprotocolservices/1509509-getlogicalunitbytes.md)
- [- GetLogicalUnitNumber](ioscsiprotocolservices/1509490-getlogicalunitnumber.md)
- [- GetProtocolLayerReference](ioscsiprotocolservices/1509452-getprotocollayerreference.md)
- [- GetRealizedDataTransferCount](ioscsiprotocolservices/1509483-getrealizeddatatransfercount.md)
- [- GetRequestedDataTransferCount](ioscsiprotocolservices/1509512-getrequesteddatatransfercount.md)
- [- GetTaskAttribute](ioscsiprotocolservices/1509503-gettaskattribute.md)
- [- GetTaskExecutionMode](ioscsiprotocolservices/1509482-gettaskexecutionmode.md)
- [- GetTaskState](ioscsiprotocolservices/1509554-gettaskstate.md)
- [- GetTimeoutDuration](ioscsiprotocolservices/1509479-gettimeoutduration.md)
- [- HandleAbortTask](ioscsiprotocolservices/1509457-handleaborttask.md)
- [- HandleAbortTaskSet](ioscsiprotocolservices/1509459-handleaborttaskset.md)
- [- HandleCheckPowerState](ioscsiprotocolservices/1509517-handlecheckpowerstate.md)
- [- HandleClearACA](ioscsiprotocolservices/1509493-handleclearaca.md)
- [- HandleClearTaskSet](ioscsiprotocolservices/1509518-handlecleartaskset.md)
- [- HandleLogicalUnitReset](ioscsiprotocolservices/1509540-handlelogicalunitreset.md)
- [- HandlePowerChange](ioscsiprotocolservices/1509462-handlepowerchange.md)
- [- HandlePowerOff](ioscsiprotocolservices/1509450-handlepoweroff.md)
- [- HandlePowerOn](ioscsiprotocolservices/1509550-handlepoweron.md)
- [- HandleProtocolServiceFeature](ioscsiprotocolservices/1509558-handleprotocolservicefeature.md)
- [- HandleTargetReset](ioscsiprotocolservices/1509551-handletargetreset.md)
- [- InitializePowerManagement](ioscsiprotocolservices/1509527-initializepowermanagement.md)
- [- IsProtocolServiceSupported](ioscsiprotocolservices/1509521-isprotocolservicesupported.md)
- [- LogicalUnitReset](ioscsiprotocolservices/1509536-logicalunitreset.md)
- [- ProcessCompletedTask](ioscsiprotocolservices/1509505-processcompletedtask.md)
- [- RegisterSCSITaskCompletionRoutine](ioscsiprotocolservices/1509511-registerscsitaskcompletionroutin.md)
- [- RejectSCSITasksCurrentlyQueued](ioscsiprotocolservices/1509507-rejectscsitaskscurrentlyqueued.md)
- [- RejectTask](ioscsiprotocolservices/1509449-rejecttask.md)
- [- RetrieveNextSCSITaskFromQueue](ioscsiprotocolservices/1509515-retrievenextscsitaskfromqueue.md)
- [- SendNotification_DeviceRemoved](ioscsiprotocolservices/1509460-sendnotification_deviceremoved.md)
- [- SendNotification_VerifyDeviceState](ioscsiprotocolservices/1509475-sendnotification_verifydevicesta.md)
- [- SendSCSICommand](ioscsiprotocolservices/1509525-sendscsicommand.md)
- [- SendSCSITasksFromQueue](ioscsiprotocolservices/1509520-sendscsitasksfromqueue.md)
- [- SetAutoSenseData](ioscsiprotocolservices/1509471-setautosensedata.md)
- [- SetAutoSenseData](ioscsiprotocolservices/3516769-setautosensedata.md)
- [- SetProtocolLayerReference](ioscsiprotocolservices/1509454-setprotocollayerreference.md)
- [- SetRealizedDataTransferCount](ioscsiprotocolservices/1509491-setrealizeddatatransfercount.md)
- [- SetTaskExecutionMode](ioscsiprotocolservices/1509533-settaskexecutionmode.md)
- [- SetTaskState](ioscsiprotocolservices/1509531-settaskstate.md)
- [- TargetReset](ioscsiprotocolservices/1509484-targetreset.md)
- [- TicklePowerManager](ioscsiprotocolservices/1509545-ticklepowermanager.md)
- [- free](ioscsiprotocolservices/1509497-free.md)
- [- getMetaClass](ioscsiprotocolservices/1509463-getmetaclass.md)
- [- init](ioscsiprotocolservices/1509534-init.md)
- [- start](ioscsiprotocolservices/1509456-start.md)

## Relationships

### Inherits From
- [IOSCSIProtocolInterface](ioscsiprotocolinterface.md)

## See Also

- [IOReducedBlockServices](ioreducedblockservices.md)
- [IOSCSIPeripheralDeviceNub](ioscsiperipheraldevicenub.md)
- [IOSCSIPrimaryCommandsDevice](ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolInterface](ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprotocolservices)*