# IOSCSIProtocolServices

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOSCSIProtocolServices : IOSCSIProtocolInterface
```

## Topics

### Miscellaneous
- [AbortCommand](./ioscsiprotocolservices/api-1809724-abortcommand.md)
  Deprecated. Do not use.
- [AbortSCSICommand](./ioscsiprotocolservices/api-1809736-abortscsicommand.md)
  Pure virtual method subclasses must implement so that SCSITasks may be aborted.
- [AbortSCSITaskFromQueue](./ioscsiprotocolservices/api-1809747-abortscsitaskfromqueue.md)
  Deprecated internal method.
- [AbortTask](./ioscsiprotocolservices/api-1809759-aborttask.md)
  The Task Management function to allow the SCSI Application Layer client to request that a specific task be aborted.
- [AbortTaskSet](./ioscsiprotocolservices/api-1809765-aborttaskset.md)
  The Task Management function to allow the SCSI Application Layer client to request that a complete task set be aborted.
- [AddSCSITaskToHeadOfQueue](./ioscsiprotocolservices/api-1809777-addscsitasktoheadofqueue.md)
  Internal method called to add a SCSITask to the head of the processing queue.
- [AddSCSITaskToQueue](./ioscsiprotocolservices/api-1809791-addscsitasktoqueue.md)
  Internal method called to add a SCSITask to the processing queue.
- [ClearACA](./ioscsiprotocolservices/api-1809805-clearaca.md)
  The Task Management function to clear an Auto-Contingent Allegiance condition.
- [ClearTaskSet](./ioscsiprotocolservices/api-1809813-cleartaskset.md)
  The Task Management function to clear a task set.
- [CommandCompleted](./ioscsiprotocolservices/api-1809823-commandcompleted.md)
  Method subclass calls to complete a SCSITask.
- [CreateSCSITargetDevice](./ioscsiprotocolservices/api-1809830-createscsitargetdevice.md)
  Used to create a SCSITargetDevice which will manage logical units.
- [EnsureAutosenseDescriptorExists](./ioscsiprotocolservices/api-1809843-ensureautosensedescriptorexists.md)
  Internal method, not to be called by subclasses.
- [ExecuteCommand](./ioscsiprotocolservices/api-1809854-executecommand.md)
  ExecuteCommand method will take a SCSI Task and transport it across the physical wire(s) to the device.
- [free](./ioscsiprotocolservices/api-1809869-free.md)
  Frees data structures that were allocated during start().
- [GetAutosenseRequestedDataTransferCount](./ioscsiprotocolservices/api-1809881-getautosenserequesteddatatransfe.md)
  Accessor method to retrieve the requested data transfer count for autosense data associated with the specified request.
- [GetCommandDescriptorBlock](./ioscsiprotocolservices/api-1809892-getcommanddescriptorblock.md)
  Accessor method to retrieve the Command Descriptor Block associated with the specified request.
- [GetCommandDescriptorBlockSize](./ioscsiprotocolservices/api-1809902-getcommanddescriptorblocksize.md)
  Accessor method to retrieve the Command Descriptor Block size associated with the specified request.
- [GetDataBuffer](./ioscsiprotocolservices/api-1809915-getdatabuffer.md)
  Accessor method to retrieve the data buffer associated with the specified request.
- [GetDataBufferOffset](./ioscsiprotocolservices/api-1809935-getdatabufferoffset.md)
  Accessor method to retrieve the data buffer offset associated with the specified request.
- [GetDataTransferDirection](./ioscsiprotocolservices/api-1809946-getdatatransferdirection.md)
  Accessor method to retrieve the data transfer direction associated with the specified request.
- [GetInitialPowerState](./ioscsiprotocolservices/api-1809959-getinitialpowerstate.md)
  This method is called once, right after InitializePowerManagement() in order to determine what state the device is initially in at startup time (usually the highest power mode).
- [GetLogicalUnitBytes](./ioscsiprotocolservices/api-1809964-getlogicalunitbytes.md)
  Accessor method to retrieve the logical unit bytes associated with the specified request.
- [GetLogicalUnitNumber](./ioscsiprotocolservices/api-1809972-getlogicalunitnumber.md)
  Accessor method to retrieve the logical unit number associated with the specified request.
- [GetProtocolLayerReference](./ioscsiprotocolservices/api-1809980-getprotocollayerreference.md)
  Accessor method to retrieve the protocol layer reference.
- [GetRealizedDataTransferCount](./ioscsiprotocolservices/api-1809989-getrealizeddatatransfercount.md)
  Accessor method to retrieve the realized data transfer count associated with the specified request.
- [GetRequestedDataTransferCount](./ioscsiprotocolservices/api-1809996-getrequesteddatatransfercount.md)
  Accessor method to retrieve the requested data transfer count associated with the specified request.
- [GetTaskAttribute](./ioscsiprotocolservices/api-1810005-gettaskattribute.md)
  Accessor method to retrieve the SCSITaskAttribute associated with the specified request.
- [GetTaskExecutionMode](./ioscsiprotocolservices/api-1810017-gettaskexecutionmode.md)
  Internal method used to retrieve the task execution mode.
- [GetTaskState](./ioscsiprotocolservices/api-1810028-gettaskstate.md)
  Accessor method to retrieve the SCSITaskState associated with the specified request.
- [GetTimeoutDuration](./ioscsiprotocolservices/api-1810038-gettimeoutduration.md)
  Accessor method to retrieve the timeout duration in milliseconds associated with the specified request.
- [HandleAbortTask](./ioscsiprotocolservices/api-1810051-handleaborttask.md)
  HandleAbortTask instructs the Protocol Services driver to abort the task.
- [HandleAbortTaskSet](./ioscsiprotocolservices/api-1810062-handleaborttaskset.md)
  HandleAbortTaskSet instructs the Protocol Services driver to abort the task set.
- [HandleCheckPowerState](./ioscsiprotocolservices/api-1810080-handlecheckpowerstate.md)
  Method called to check if the device is in the correct power state for an I/O.
- [HandleClearACA](./ioscsiprotocolservices/api-1810093-handleclearaca.md)
  HandleClearACA instructs the Protocol Services driver to clear an auto-contingent allegiance.
- [HandleClearTaskSet](./ioscsiprotocolservices/api-1810105-handlecleartaskset.md)
  HandleClearTaskSet instructs the Protocol Services driver to clear the task set.
- [HandleLogicalUnitReset](./ioscsiprotocolservices/api-1810119-handlelogicalunitreset.md)
  HandleLogicalUnitReset instructs the Protocol Services driver to reset the logical unit.
- [HandlePowerChange](./ioscsiprotocolservices/api-1810127-handlepowerchange.md)
  This method is called to handle a power change.
- [HandlePowerOff](./ioscsiprotocolservices/api-1810144-handlepoweroff.md)
  Convenience method for a protocol service driver to handle a power off call (called on the way to sleep).
- [HandlePowerOn](./ioscsiprotocolservices/api-1810154-handlepoweron.md)
  Convenience method for a protocol service driver to handle a power on call (called on the way back up from sleep).
- [HandleProtocolServiceFeature](./ioscsiprotocolservices/api-1810168-handleprotocolservicefeature.md)
  HandleProtocolServiceFeature instructs the Protocol Services driver to perform the necessary tasks for the indicated feature.
- [HandleTargetReset](./ioscsiprotocolservices/api-1810176-handletargetreset.md)
  HandleTargetReset instructs the Protocol Services driver to reset the target.
- [init](./ioscsiprotocolservices/api-1810187-init.md)
  Standard init method for all IORegistryEntry subclasses.
- [InitializePowerManagement](./ioscsiprotocolservices/api-1810204-initializepowermanagement.md)
  Subclasses call this method to initialize power management.
- [IsProtocolServiceSupported](./ioscsiprotocolservices/api-1810217-isprotocolservicesupported.md)
  IsProtocolServiceSupported will return true if the specified feature is supported by the protocol layer.
- [LogicalUnitReset](./ioscsiprotocolservices/api-1810234-logicalunitreset.md)
  The Task Management function to reset a logical unit.
- [ProcessCompletedTask](./ioscsiprotocolservices/api-1810248-processcompletedtask.md)
  Internal method called to process completed SCSITasks.
- [RegisterSCSITaskCompletionRoutine](./ioscsiprotocolservices/api-1810264-registerscsitaskcompletionroutin.md)
  Used by IOSCSITargetDevice to register a completion routine.
- [RejectSCSITasksCurrentlyQueued](./ioscsiprotocolservices/api-1810276-rejectscsitaskscurrentlyqueued.md)
  Internal method called to reject currently enqueued SCSITasks.
- [RejectTask](./ioscsiprotocolservices/api-1810289-rejecttask.md)
  Internal method called to reject a particular SCSITask.
- [RetrieveNextSCSITaskFromQueue](./ioscsiprotocolservices/api-1810300-retrievenextscsitaskfromqueue.md)
  Internal method called to retrieve the next SCSITask to process.
- [SendNotification_DeviceRemoved](./ioscsiprotocolservices/api-1810317-sendnotification_deviceremoved.md)
  Method called by subclasses when a device is physically removed from the bus.
- [SendNotification_VerifyDeviceState](./ioscsiprotocolservices/api-1810332-sendnotification_verifydevicesta.md)
  Method called by subclasses when a device state needs to be re-verified due to some bus condition which may have changed the device state.
- [SendSCSICommand](./ioscsiprotocolservices/api-1810345-sendscsicommand.md)
  Pure virtual method subclasses must implement in order to send SCSITasks on the wire.
- [SendSCSITasksFromQueue](./ioscsiprotocolservices/api-1810363-sendscsitasksfromqueue.md)
  Internal method called to start processing SCSITasks.
- [SetAutoSenseData(SCSITaskIdentifier, SCSI_Sense_Data *)](./ioscsiprotocolservices/api-1810382-setautosensedata.md)
  Accessor method to set the autosense data. NOTE: This method is deprecated.
- [SetAutoSenseData(SCSITaskIdentifier, SCSI_Sense_Data *, UInt8)](./ioscsiprotocolservices/api-1810397-setautosensedata.md)
  Accessor method to set the autosense data.
- [SetProtocolLayerReference](./ioscsiprotocolservices/api-1810411-setprotocollayerreference.md)
  Accessor method to set the protocol layer reference.
- [SetRealizedDataTransferCount](./ioscsiprotocolservices/api-1810431-setrealizeddatatransfercount.md)
  Accessor method to set the realized (actual) data transfer count associated with the specified request.
- [SetTaskExecutionMode](./ioscsiprotocolservices/api-1810455-settaskexecutionmode.md)
  Internal method used to set the task execution mode.
- [SetTaskState](./ioscsiprotocolservices/api-1810476-settaskstate.md)
  Accessor method to set the SCSITaskState associated with the specified request.
- [start](./ioscsiprotocolservices/api-1810514-start.md)
  During an IOService object's instantiation, starts the IOService object that has been selected to run on the provider.
- [TargetReset](./ioscsiprotocolservices/api-1810537-targetreset.md)
  The Task Management function to reset a target device.
- [TicklePowerManager](./ioscsiprotocolservices/api-1810572-ticklepowermanager.md)
  Internal method. Do not use.
### Instance Methods
- [- AbortCommand](./ioscsiprotocolservices/api-1509516-abortcommand.md)
- [- AbortSCSICommand](./ioscsiprotocolservices/api-1509523-abortscsicommand.md)
- [- AbortSCSITaskFromQueue](./ioscsiprotocolservices/api-1509532-abortscsitaskfromqueue.md)
- [- AbortTask](./ioscsiprotocolservices/api-1509469-aborttask.md)
- [- AbortTaskSet](./ioscsiprotocolservices/api-1509555-aborttaskset.md)
- [- AddSCSITaskToHeadOfQueue](./ioscsiprotocolservices/api-1509548-addscsitasktoheadofqueue.md)
- [- AddSCSITaskToQueue](./ioscsiprotocolservices/api-1509468-addscsitasktoqueue.md)
- [- ClearACA](./ioscsiprotocolservices/api-1509499-clearaca.md)
- [- ClearTaskSet](./ioscsiprotocolservices/api-1509486-cleartaskset.md)
- [- CommandCompleted](./ioscsiprotocolservices/api-1509542-commandcompleted.md)
- [- CreateSCSITargetDevice](./ioscsiprotocolservices/api-1509451-createscsitargetdevice.md)
- [- EnsureAutosenseDescriptorExists](./ioscsiprotocolservices/api-1509514-ensureautosensedescriptorexists.md)
- [- ExecuteCommand](./ioscsiprotocolservices/api-1509557-executecommand.md)
- [- GetAutosenseRequestedDataTransferCount](./ioscsiprotocolservices/api-1509552-getautosenserequesteddatatransfe.md)
- [- GetCommandDescriptorBlock](./ioscsiprotocolservices/api-1509478-getcommanddescriptorblock.md)
- [- GetCommandDescriptorBlockSize](./ioscsiprotocolservices/api-1509487-getcommanddescriptorblocksize.md)
- [- GetDataBuffer](./ioscsiprotocolservices/api-1509473-getdatabuffer.md)
- [- GetDataBufferOffset](./ioscsiprotocolservices/api-1509488-getdatabufferoffset.md)
- [- GetDataTransferDirection](./ioscsiprotocolservices/api-1509529-getdatatransferdirection.md)
- [- GetInitialPowerState](./ioscsiprotocolservices/api-1509539-getinitialpowerstate.md)
- [- GetLogicalUnitBytes](./ioscsiprotocolservices/api-1509509-getlogicalunitbytes.md)
- [- GetLogicalUnitNumber](./ioscsiprotocolservices/api-1509490-getlogicalunitnumber.md)
- [- GetProtocolLayerReference](./ioscsiprotocolservices/api-1509452-getprotocollayerreference.md)
- [- GetRealizedDataTransferCount](./ioscsiprotocolservices/api-1509483-getrealizeddatatransfercount.md)
- [- GetRequestedDataTransferCount](./ioscsiprotocolservices/api-1509512-getrequesteddatatransfercount.md)
- [- GetTaskAttribute](./ioscsiprotocolservices/api-1509503-gettaskattribute.md)
- [- GetTaskExecutionMode](./ioscsiprotocolservices/api-1509482-gettaskexecutionmode.md)
- [- GetTaskState](./ioscsiprotocolservices/api-1509554-gettaskstate.md)
- [- GetTimeoutDuration](./ioscsiprotocolservices/api-1509479-gettimeoutduration.md)
- [- HandleAbortTask](./ioscsiprotocolservices/api-1509457-handleaborttask.md)
- [- HandleAbortTaskSet](./ioscsiprotocolservices/api-1509459-handleaborttaskset.md)
- [- HandleCheckPowerState](./ioscsiprotocolservices/api-1509517-handlecheckpowerstate.md)
- [- HandleClearACA](./ioscsiprotocolservices/api-1509493-handleclearaca.md)
- [- HandleClearTaskSet](./ioscsiprotocolservices/api-1509518-handlecleartaskset.md)
- [- HandleLogicalUnitReset](./ioscsiprotocolservices/api-1509540-handlelogicalunitreset.md)
- [- HandlePowerChange](./ioscsiprotocolservices/api-1509462-handlepowerchange.md)
- [- HandlePowerOff](./ioscsiprotocolservices/api-1509450-handlepoweroff.md)
- [- HandlePowerOn](./ioscsiprotocolservices/api-1509550-handlepoweron.md)
- [- HandleProtocolServiceFeature](./ioscsiprotocolservices/api-1509558-handleprotocolservicefeature.md)
- [- HandleTargetReset](./ioscsiprotocolservices/api-1509551-handletargetreset.md)
- [- InitializePowerManagement](./ioscsiprotocolservices/api-1509527-initializepowermanagement.md)
- [- IsProtocolServiceSupported](./ioscsiprotocolservices/api-1509521-isprotocolservicesupported.md)
- [- LogicalUnitReset](./ioscsiprotocolservices/api-1509536-logicalunitreset.md)
- [- ProcessCompletedTask](./ioscsiprotocolservices/api-1509505-processcompletedtask.md)
- [- RegisterSCSITaskCompletionRoutine](./ioscsiprotocolservices/api-1509511-registerscsitaskcompletionroutin.md)
- [- RejectSCSITasksCurrentlyQueued](./ioscsiprotocolservices/api-1509507-rejectscsitaskscurrentlyqueued.md)
- [- RejectTask](./ioscsiprotocolservices/api-1509449-rejecttask.md)
- [- RetrieveNextSCSITaskFromQueue](./ioscsiprotocolservices/api-1509515-retrievenextscsitaskfromqueue.md)
- [- SendNotification_DeviceRemoved](./ioscsiprotocolservices/api-1509460-sendnotification_deviceremoved.md)
- [- SendNotification_VerifyDeviceState](./ioscsiprotocolservices/api-1509475-sendnotification_verifydevicesta.md)
- [- SendSCSICommand](./ioscsiprotocolservices/api-1509525-sendscsicommand.md)
- [- SendSCSITasksFromQueue](./ioscsiprotocolservices/api-1509520-sendscsitasksfromqueue.md)
- [- SetAutoSenseData](./ioscsiprotocolservices/api-1509471-setautosensedata.md)
- [- SetAutoSenseData](./ioscsiprotocolservices/api-3516769-setautosensedata.md)
- [- SetProtocolLayerReference](./ioscsiprotocolservices/api-1509454-setprotocollayerreference.md)
- [- SetRealizedDataTransferCount](./ioscsiprotocolservices/api-1509491-setrealizeddatatransfercount.md)
- [- SetTaskExecutionMode](./ioscsiprotocolservices/api-1509533-settaskexecutionmode.md)
- [- SetTaskState](./ioscsiprotocolservices/api-1509531-settaskstate.md)
- [- TargetReset](./ioscsiprotocolservices/api-1509484-targetreset.md)
- [- TicklePowerManager](./ioscsiprotocolservices/api-1509545-ticklepowermanager.md)
- [- free](./ioscsiprotocolservices/api-1509497-free.md)
- [- getMetaClass](./ioscsiprotocolservices/api-1509463-getmetaclass.md)
- [- init](./ioscsiprotocolservices/api-1509534-init.md)
- [- start](./ioscsiprotocolservices/api-1509456-start.md)

## Relationships

### Inherits From
- [IOSCSIProtocolInterface](./ioscsiprotocolinterface.md)

## See Also

### Base Types
- [IOReducedBlockServices](./ioreducedblockservices.md)
- [IOSCSIPeripheralDeviceNub](./ioscsiperipheraldevicenub.md)
- [IOSCSIPrimaryCommandsDevice](./ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolInterface](./ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprotocolservices)*